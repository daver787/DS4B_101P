# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 7 (Plotnine): Plot Automation ----

# Imports
import pandas as pd
import numpy as np
import scipy as sp

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
       kind         = 'timestamp',
       wide_format  = True
    )\
    .arima_forecast(
       h  = 12,
       sp = 12 
    )      


# 1.0 FORECAST VISUALIZATION ----

# Step 1: Data preparation for Plot

df_prepped = arima_forecast_df\
   .melt(
      id_vars    = ['category_1','order_date','ci_low', 'ci_hi'],
      value_vars = ['value', 'prediction'],
      var_name   = '.variable',
      value_name = '.value'
   )\
   .rename({".value":"value"}, axis = 1)
   # /
   # .assign(
   #    order_date = lambda x : x['order_date'].dt.to_timestamp()
   # )    

# Step 2: Plotting
(
ggplot(
   mapping = aes(x = 'order_date', y = 'value', color = '.variable'),
   data    = df_prepped
)
   + geom_ribbon(
      aes(ymin = 'ci_low', ymax = 'ci_hi'),
      alpha = 0.2,
      color = None)
   + geom_line()
   + facet_wrap('category_1', ncol = 1, scales = 'free_y')
)
# 2.0 PLOTTING AUTOMATION ----
# - Make plot_forecast()

# Function Development 
        

# Testing 










