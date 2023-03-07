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
    data        = arima_forecast_df,
    id_column   = 'category_2',
    date_column = 'order_date'
    )


# 2.0 WRITE TO DATABASE ----

def write_forecast_to_database(
    data, id_column, date_column, 
    conn_string = "sqlite:///00_database/bike_orders_database.sqlite",
    table_name  = "forecast",
    if_exists   = "fail",
    **kwargs
):
    # Prepare the data
    df = prep_forecast_data_for_update(
    data        = data,
    id_column   = id_column,
    date_column = date_column
    )
       
    # Check format for SQL Database   
    df['date'] = df['date'].dt.to_timestamp()
    
    sql_dtype = {
        "id"         : sql.String(),
        "date"       : sql.String(),
        "value"      : sql.Numeric(),
        "prediction" : sql.Numeric(),
        "ci_low"     : sql.Numeric(),
        "ci_hi"      : sql.Numeric()     
    }
    
    # Connect to the Database
    
    engine = sql.create_engine(conn_string)
    
    conn = engine.connect()
    
    df.to_sql(
        con       = conn,
        name      = table_name,
        if_exists = if_exists,
        dtype     = sql_dtype,
        index     = False
        #**kwargs
        )
    # Close the connection
    conn.close()
    
    pass
    
write_forecast_to_database(
    data        = arima_forecast_df,
    id_column   = "category_2",
    date_column = "order_date",
    table_name  = "forecast_2",
    if_exists   = "replace"
    )

sql.Table("forecast_2",sql.MetaData(conn)).drop()

# 3.0 READ FROM DATABASE ----

def read_forecast_from_database(
    conn_string = "sqlite:///00_database/bike_orders_database.sqlite",
    table_name  = "forecast",
    **kwargs
):
   
   # Connect to Database
   engine = sql.create_engine(conn_string)
    
   conn = engine.connect()
    
   # Read from Table
   
   df = pd.read_sql(
       f"SELECT * from {table_name}",
               con         = conn,
               parse_dates = ['date']
               )
   
   # Close Connection 
   conn.close()
   
   return df

read_forecast_from_database(table_name = "forecast")