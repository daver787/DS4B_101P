# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 6 (Sktime): ARIMA Automation ----

# Imports

import pandas as pd
import numpy as np

from my_pandas_extensions.database import collect_data
from my_pandas_extensions.timeseries import summarize_by_time
from sktime.forecasting.arima import AutoARIMA
from tqdm import tqdm


# Workflow
df = collect_data()

bike_sales_m_df = df\
    .summarize_by_time(
        date_column  = "order_date",
        value_column = "total_price",
        rule         = "M",
        kind         = "period" 
    )
    
bike_sales_cat2_m_df = df\
    .summarize_by_time(
        date_column  = "order_date",
        value_column = "total_price",
        groups       = ["category_2"],
        rule         = "M",
        kind         ="period"
    ) 


# FUNCTION DEVELOPMENT ----
# - arima_forecast(): Generates ARIMA forecasts for one or more time series.


data = bike_sales_cat2_m_df

def arima_forecast(
    data, h = 12, sp = 12, alpha = 0.05,
    suppress_warnings = True,
    *args, **kwargs
    ):
   
   #Checks
   
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
       
       
       print(forecaster)
 
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
    return model_results_df

arima_forecast(data, h =12, sp = 12)