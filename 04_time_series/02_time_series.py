# DS4B 101-P: PYTHON FOR BUSINESS ANALYSIS ----
# Module 4 (Time Series): Working with Time Series Data ----

# IMPORTS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from my_pandas_extensions.database import collect_data

# DATA

df = collect_data()

# 1.0 DATE BASICS

df['order_date']


# Conversion

type('2011-01-07')
pd.to_datetime('2011-01-07').to_period(freq ="W").to_timestamp()

# Accessing elements

# Months

df.order_date.dt.month
df.order_date.dt.month_name()

# Days

df.order_date.dt.day
df.order_date.dt.day_name()


#Year
df.order_date.dt.year

# DATE MATH

import datetime

today = datetime.date.today()

pd.to_datetime(today + pd.Timedelta("1 day"))

df.order_date + pd.Timedelta("1Y")

df.order_date + pd.Timedelta("30 min")

# Duration

today = datetime.date.today()

one_year_from_today = today + pd.Timedelta("1Y")

(one_year_from_today - today)/pd.Timedelta("1W")

pd.Timedelta(one_year_from_today - today)/np.timedelta64(1,"M")

pd.Timedelta(one_year_from_today - today)/pd.Timedelta("1M")

# DATE SEQUENCES


pd.date_range(
    start   =  pd.to_datetime("2011-01"),
    periods = 10,
    freq    = "2D"
)

pd.date_range(
    start   =  pd.to_datetime("2011-01"),
    end     =  pd.to_datetime("2011-12-31"),
    freq    = "1W"
)


# PERIODS
# - Periods represent timestamps that fall within an interval using a frequency.
# - IMPORTANT: {sktime} requires periods to model univariate time series


# Convert to Time Stamp

df.order_date.dt.to_period(freq = "D")

df.order_date.dt.to_period(freq = "W")

df.order_date.dt.to_period(freq = "M")

df.order_date.dt.to_period(freq = "Q")

df.order_date.dt.to_period(freq = "Y")

# Get the Frequency

df.order_date.dt.to_period(freq = "Q").dt.freq

df.order_date.dt.to_period(freq = "Y").dt.freq

#Conversion to Timestamp

df.order_date.dt.to_period(freq = "M").dt.to_timestamp()

df.order_date.dt.to_period(freq = "Q").dt.to_timestamp()

# TIME-BASED GROUPING (RESAMPLING)
# - The beginning of our Summarize by Time Function

# Single Time Series. Using kind = "timestamp"

bike_sales_m_df = df[['order_date', 'total_price']]\
    .set_index('order_date')\
    .resample("M", kind = "period")\
    .sum()\
    .reset_index()\
    .assign(order_date = lambda x: x.order_date.dt.to_timestamp())        
    
bike_sales_m_df           

# Grouped Time Series. Using kind = "period"
# We had trouble with overlapping time stamps,
# which required an extra step to convert to period. 

bike_sales_cat2_m_wide_df = df[['category_2', 'order_date', 'total_price']]\
    .set_index('order_date')\
    .groupby('category_2')\
    .resample('M')\
    .agg(np.sum)\
    .unstack('category_2')\
    .reset_index()\
    .assign(order_date = lambda x: x['order_date'].dt.to_period())\
    .set_index('order_date')                            
        
bike_sales_cat2_m_wide_df

# MEASURING CHANGE

# Difference from Previous Timestamp

#  - Single (No Groups)



#  - Multiple Groups: Key is to use wide format with apply




#  - Difference from First Timestamp




# CUMULATIVE CALCULATIONS



# ROLLING CALCULATIONS

# Single

# Groups - Can't use assign(), we'll use merging




