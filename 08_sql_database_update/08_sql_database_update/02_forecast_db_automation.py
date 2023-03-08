# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 8 (SQL Database Update): Forecast Automation ----

# IMPORTS ----
import pandas as pd
import numpy as np

from my_pandas_extensions.database import (
    collect_data, 
    write_forecast_to_database,
    read_forecast_from_database
)

from my_pandas_extensions.timeseries import summarize_by_time
from my_pandas_extensions.forecasting import arima_forecast, plot_forecast

df = collect_data()

# 1.0 SUMMARIZE AND FORECAST ----


# 1.1 Total Revenue ----

df\
    .summarize_by_time(
        date_column  = 'order_date',
        value_column = 'total_price',
        rule         = 'M',
        kind         = 'period'
    )\
    .arima_forecast(
        h  = 12,
        sp = 12
    )\
    .assign(id = 'Total Revenue')    


# 1.2 Revenue by Category 1 ----


# 1.3 Revenue by Category 2 ----


# 1.4 Revenue by Customer ----


# 2.0 UPDATE DATABASE ----


# 2.1 Write to Database ----


# 2.2 Read from Database ----
