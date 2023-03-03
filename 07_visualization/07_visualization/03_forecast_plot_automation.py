# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 7 (Plotnine): Plot Automation ----

# Imports
import pandas as pd
import numpy as np

from plotnine import *
from mizani.formatters import dollar_format

from my_pandas_extensions.database import collect_data
from my_pandas_extensions.timeseries import summarize_by_time
from my_pandas_extensions.forecasting import arima_forecast

# Workflow until now

df = collect_data()

arima_forecast_df = df\
    .summarize_by_time(
       date_column  =  'order_date',
       value_column =  'total_price',
       groups       = 'category_1',
       rule         = 'M',
       kind         = 'period',
       wide_format  = True
    )\
    .arima_forecast(
       h  = 12,
       sp = 12 
    )      


# 1.0 FORECAST VISUALIZATION ----

# Step 1: Data preparation for Plot


# Step 2: Plotting





# 2.0 PLOTTING AUTOMATION ----
# - Make plot_forecast()

# Function Development 
        

# Testing 










