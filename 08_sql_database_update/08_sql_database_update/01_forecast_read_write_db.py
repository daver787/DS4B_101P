# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 8 (SQL Database Update): Forecast Write and Read Functions ----

# IMPORTS ----

import sqlalchemy as sql
import pandas as pd
import numpy as np

from my_pandas_extensions.database import collect_data
from my_pandas_extensions.timeseries import summarize_by_time
from my_pandas_extensions.forecasting import arima_forecast, plot_forecast

df = collect_data()

# WORKFLOW ----
# - Until Module 07: Visualization

arima_forecast_df = df\
    .summarize_by_time(
        date_column  = 'order_date',
        value_column = 'total_price',
        groups       = 'category_2',
        rule         = 'M',
        agg_func     = np.sum,
        kind         = 'period',
        wide_format  = True,
        fillna       = 0
    )\
    .arima_forecast(
        h                 = 12,
        sp                = 12,
        suppress_warnings = True,
        alpha             = 0.05
    )    
    
arima_forecast_df\
    .plot_forecast(
        id_column   = 'category_2',
        date_column = 'order_date',
        facet_ncol  = 3
    )    

# DATABASE UPDATE FUNCTIONS ----


# 1.0 PREPARATION FUNCTIONS ----

arima_forecast_df\
    .rename(
        {
            'category_2': 'id',
            'order_date': 'date'
    }, 
        axis = 1
        )

def prep_forecast_data_for_update(
    data, id_column, date_column
):
    # Format the column names
    df = data\
        .rename(
            {
                id_column   : 'id',
                date_column : 'date'
            }, 
            axis = 1
            )
    # Validate correct columns
    
    required_col_names = ['id', 'date', 'value','prediction', 'ci_low', 'ci_hi']
    
    if not all(pd.Series(required_col_names).isin(df.columns)):
        col_text = ", ".join(required_col_names)
        raise Exception(f'Columns must contain: {col_text}')
    
    return(df)

prep_forecast_data_for_update(
    data        = arima_forecast_df.drop('ci_low', axis = 1),
    id_column   = 'category_2',
    date_column = 'order_date'
    )


# 2.0 WRITE TO DATABASE ----


# 3.0 READ FROM DATABASE ----

