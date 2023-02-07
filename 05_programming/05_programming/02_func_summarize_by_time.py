# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 5 (Programming): Functions ----

# Imports

import pandas as pd
import numpy as np
from pandas.core import groupby

from my_pandas_extensions.database import collect_data

df = collect_data()

# WHAT WE WANT TO STREAMLINE

rule ='D'
data = df

df[['category_2', 'order_date', 'total_price']] \
    .set_index('order_date') \
    .groupby('category_2') \
    .resample(rule, kind = 'period') \
    .agg(np.sum) \
    .unstack("category_2") \
    .reset_index() \
    .assign(order_date = lambda x: x['order_date'].dt.to_period()) \
    .set_index("order_date")

# BUILDING SUMMARIZE BY TIME
def summarize_by_time(
    data, date_column,value_column,
                      groups      = None,
                      rule        = 'D',
                      agg_func    = np.sum,
                      kind        = 'timestamp',
                      wide_format = True,
                      fillna      = 0,
                      *args,
                      **kwargs):
    # CHECKS
    if type(value_column) is not list:
        value_column = [value_column]
    
    # BODY
    
    # Handle date column
    data = data.set_index(date_column)
    
    # Handle groupby
    if groups is not None:
        data = data.groupby(groups)
        
    # Handle resample
    data = data.resample(
        rule = rule,
        kind = kind
        
    )
    # Handle the aggregration
    function_list = [agg_func] * len(value_column)
    agg_dict      = dict(zip(value_column, function_list))

    data = data\
        .agg(
        func = agg_dict,
        *args,
        **kwargs
    ) 
    
    # Handle Pivot Wider
    if wide_format:
        if groups is not None:
            data = data.unstack(groups)
            if (kind == "period"):
                data.index = data.index.to_period()
                
    data = data.fillna(value = fillna)         
           
    
    return data
    
summarize_by_time(
    data         = df, 
    date_column  = 'order_date',
    value_column = 'total_price',
    groups       = ['category_1', 'category_2'],
    rule         = 'M',
    kind         = 'period',
    agg_func     = np.sum,
    wide_format  = True,
    fillna       = 0
    )

# ADDING TO OUR TIME SERIES MODULE

