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
   
    for col in tqdm(df.columns, min_interval = 0):
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

    return None

arima_forecast(data, h =12, sp = 12)