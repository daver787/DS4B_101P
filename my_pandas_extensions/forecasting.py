
# Imports

import pandas as pd
import numpy as np
import pandas_flavor as pf
from sktime.forecasting.arima import AutoARIMA
from tqdm import tqdm


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