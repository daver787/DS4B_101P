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
from sktime.utils.plotting import plot_series

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

bike_sales_m_df.plot()

bike_sales_m_df

y = bike_sales_m_df['total_price']

forecaster = AutoARIMA(sp = 12)

forecaster.fit(y)

# Prediction
h = 24
forecaster.predict(fh = np.arange(1, h+1))

# Confidence Intervals
predictions_series, conf_int_df = forecaster.predict(
    fh              = np.arange(1,h+1),
    return_pred_int = True,
    alpha           = 0.05
    )

# type(predictions_ci_tuple)

# predictions_ci_tuple[1]

predictions_series
conf_int_df

# Visualize
# ?plot_series

plot_series(
    y,
    predictions_series,
    conf_int_df['lower'],
    conf_int_df['upper'],
    labels=['actual', 'predictions','ci_lower','ci_upper']
    )

# 3.0 MULTIPLE TIME SERIES FORCAST (LOOP) ----


