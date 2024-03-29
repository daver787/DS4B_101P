
# Imports

import pandas as pd
import numpy as np
import pandas_flavor as pf
from my_pandas_extensions.database import convert_to_datetime
from sktime.forecasting.arima import AutoARIMA
from tqdm import tqdm

# Plotting Imports
from plotnine import *
from mizani.formatters import dollar_format
from plydata.cat_tools import cat_reorder


# - arima_forecast(): Generates ARIMA forecasts for one or more time series.

@pf.register_dataframe_method
def arima_forecast(
    data, h = 12, sp = 12, alpha = 0.05,
    suppress_warnings = True,
    *args, **kwargs
    ):
    """    Generates ARIMA forecasts for one or more time series.
    Args:
        data (Pandas Data Frame): 
            Data must be in wide format. 
            Data must have a time-series index 
            that is a pandas period.
        h (int): 
            The forecast horizon
        sp (int): 
            The seasonal period
        alpha (float, optional): 
            Contols the confidence interval. 
            alpha = 1 - 95% (CI).
            Defaults to 0.05.
        suppress_warnings (bool, optional): 
            Suppresses ARIMA feedback during automated model training. 
            Defaults to True.
        args: Passed to sktime.forecasting.arima.AutoARIMA
        kwargs: Passed to sktime.forecasting.arima.AutoARIMA
    Returns:
        Pandas Data Frame:
            - A single time series contains columns: value, prediction, ci_lo, and ci_hi
            - Multiple time series will be returned stacked by group
    """
   #Checks
  
   
    if (type(h) is not int):
       raise Exception("`h` must be an integer.")
   
    if (type(sp) is not int):
       raise Exception("`sp` must be an integer.")
   
    if (type(data) is not pd.DataFrame):
        raise Exception("`data` must be a DataFrame")
   
   
   # Handle inputs ----
    df = data
   
   #FOR LOOP ----
    model_results_dict ={}
   
    for col in tqdm(df.columns, mininterval = 0):
       # Series Extraction
       y = df[col]
       
   #Modeling
       forecaster = AutoARIMA(
       sp                = sp,
       suppress_warnings = suppress_warnings,
       *args,
       **kwargs
        )
    
       forecaster.fit(y)
       
 
   #Prediction and Confidence Intervals 
   
       predictions, conf_int_df = forecaster.predict(
        fh              = np.arange(1,h+1),
        return_pred_int = True,
        alpha           = alpha
        )

    #Combine into data frame
       ret = pd.concat([y, predictions, conf_int_df], axis = 1)
       ret.columns = ["value", "prediction", "ci_low", "ci_hi"]
       
     
     # Update dictionary
       model_results_dict[col] = ret  
    
    # Stack Each Dict Element on Top of Each Other
    
    model_results_df = pd.concat(
        model_results_dict,
        axis = 0
        )   
    
    nms = [*df.columns.names, *df.index.names]
    
    model_results_df.index.names = nms
    
    #Reset Index
    ret = model_results_df.reset_index()
    
    cols_to_keep = ~ret.columns.str.startswith("level_")
    
    ret = ret.iloc[:, cols_to_keep]
    
    return ret


@pf.register_dataframe_method
def plot_forecast(
   data,
   id_column,
   date_column,
   ribbon_alpha = 0.2,
   facet_ncol   = 1,
   facet_scales = 'free_y',
   date_labels  = '%Y',
   date_breaks  = '1 year',
   wspace       = 0.25,
   figure_size  = (16,8),
   title        = 'Forecast Plot',
   xlab         = 'Date',
   ylab         = 'Revenue'
   
   
):
    """Automates the forecast visualization
    Args:
        data (DataFrame): A pandas data frame that is the output
            of the arima_forecast() function.  
        id_column (str): [description]
        date_column (str): The timestamp column.
        facet_ncol (int, optional): Number of faceting columns. Defaults to 1.
        facet_scales (str, optional): One of None, "free", "free_y", "free_x". Defaults to "free_y".
        date_labels (str, optional): The strftime format for the x-axis date label. Defaults to "%Y".
        date_breaks (str, optional): Locations for the date breaks on the x-axis. Defaults to "1 year".
        ribbon_alpha (float, optional): The opacity of the confidence intervals. Defaults to 0.2.
        wspace (float, optional): The whitespace to include between subplots. Defaults to 0.25.
        figure_size (tuple, optional): The aspect ratio for the plot. Defaults to (16,8).
        title (str, optional): The plot title. Defaults to "Forecast Plot".
        xlab (str, optional): The x-axis label. Defaults to "Date".
        ylab (str, optional): The y-axis label. Defaults to "Revenue".
    Returns:
        [gglot]: Returns a plotnine ggplot object
    """
   
    required_columns = [id_column, date_column, 'value', 'prediction', 'ci_low', 'ci_hi']
   
   
   # Data Wrangling
    df_prepped = data\
        .loc[:, required_columns]\
        .melt(
                id_vars    = [id_column, date_column,'ci_low', 'ci_hi'],
                value_vars = ['value', 'prediction'],
                var_name   = '.variable',
                value_name = '.value'
            )\
        .rename({".value":"value"}, axis = 1)
   
   # Handle the Categorical Conversion
    df_prepped[id_column] = cat_reorder(
       c         = df_prepped[id_column],
       x         = df_prepped['value'],
       fun       = np.mean,
       ascending = False
       )
    
    # Checking for period, convert to datetime64
    df_prepped = convert_to_datetime(df_prepped, date_column)  
          
    #Preparing the Plot
    
    #Geometries
    g = ggplot(
    mapping = aes(x = date_column, y = 'value', color = '.variable'),
    data    = df_prepped
     )\
    + geom_ribbon(
       aes(ymin = 'ci_low', ymax = 'ci_hi'),
       alpha = ribbon_alpha,
       color = None)\
    + geom_line()\
    + facet_wrap(id_column, ncol = facet_ncol, scales = facet_scales)
    
    
    #Scales
    g = g\
    + scale_x_datetime(date_labels = date_labels, date_breaks = date_breaks)\
    + scale_y_continuous(labels = dollar_format(big_mark = ',', digits = 0))\
    + scale_color_manual(values = ['red', '#2c3e50'])
    
    #Theme and Labels
    g = g\
    + theme_minimal()\
    + theme(
       legend_position = 'none',
       subplots_adjust = {'wspace':wspace},
       figure_size     = figure_size
    )\
    + labs(
       title = title,
       x     = xlab,
       y     = ylab
    ) 
    return g       
