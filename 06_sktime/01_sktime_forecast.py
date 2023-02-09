# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 6 (Sktime): Introduction to Forecasting ----

# Imports

import pandas as pd
import numpy as np

from my_pandas_extensions.database import collect_data
from my_pandas_extensions.timeseries import summarize_by_time

df = collect_data()

# Sktime Imports
from sktime.forecasting.arima import AutoARIMA

#?AutoARIMA

# 1.0 DATA SUMMARIZATIONS ----

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

# 2.0 SINGLE TIME SERIES FORECAST ----






# 3.0 MULTIPLE TIME SERIES FORCAST (LOOP) ----


