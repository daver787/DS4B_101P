# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# JUMPSTART (Module 1): First Sales Analysis with Python ----

# Important VSCode Set Up:
#   1. Select a Python Interpreter: ds4b_101p
#   2. Delete terminals to start a fresh Python Terminal session

# 1.0 Load Libraries 

# Core Python Data Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Plotting
from plotnine import (
    ggplot, aes,
    geom_col, geom_line, geom_smooth,
    facet_wrap,
    scale_y_continuous, scale_x_datetime,
    labs,
    theme, theme_minimal, theme_matplotlib
    )

from mizani.breaks import date_breaks

from mizani.formatters import date_format, currency_format

# Misc
from os import mkdir, getcwd
from rich import pretty
pretty.install()

# 2.0 Importing Data Files ----

# help(pd.read_excel)
# - Use "q" to quit
bikes_df = pd.read_excel("00_data_raw/bikes.xlsx")

bikes_df

bikeshops_df = pd.read_excel("./00_data_raw/bikeshops.xlsx")

bikeshops_df

orderlines_df = pd.read_excel(
   io         =  "./00_data_raw/orderlines.xlsx",
   converters = {'order.date': str}
    )

orderlines_df

orderlines_df.info()
# 3.0 Examining Data ----

bikes_df.head(10)

orderlines_df

bikeshops_df

s = bikes_df['description']
freq_count_series = s.value_counts()
freq_count_series.nlargest(5)

top5_bikes_series = bikes_df['description'].value_counts().nlargest(5)

fig = top5_bikes_series.plot(kind = 'barh').invert_yaxis()
fig
plt.show()

# 4.0 Joining Data ----

bike_orderlines_joined_df = orderlines_df\
    .drop(columns ='Unnamed: 0', axis = 1) \
    .merge(
        right     = bikes_df,
        how       = 'left',
        left_on   = 'product.id',
        right_on  = 'bike.id') \
    .merge(
        right     = bikeshops_df,
        how       = 'left',
        left_on   = 'customer.id',
        right_on  = 'bikeshop.id'
    )            

bike_orderlines_joined_df

# 5.0 Wrangling Data ----

# * No copy

df = bike_orderlines_joined_df

# * Copy

df2 = bike_orderlines_joined_df.copy()

df
df2

# * Handle Dates

df['order.date']

df['order.date'] = pd.to_datetime(df['order.date'])

df.info()

# * Show Effect: Copy vs No Copy

bike_orderlines_joined_df.info()

# * Text Columns

df.description

df.location

df.T

# * Splitting Description into category_1, category_2, and frame_material
"Mountain - Over Mountain - Carbon".split(" - ")

temp_df  = df['description'].str.split(pat = ' - ', expand = True)

df['category.1']     = temp_df[0]
df['category.2']     = temp_df[1]
df['frame.material'] = temp_df[2]

# * Splitting Location into City and State

temp_df = df['location'].str.split(', ',  expand = True)
df['city']  = temp_df[0]
df['state'] = temp_df[1]
# * Price Extended

df['total.price'] = df['quantity'] * df['price']
df.sort_values('total.price', ascending = False)

# * Reorganizing
cols_to_keep_list = [
   'order.id', 
   'order.line',
   'order.date',
   'model',
   'quantity', 
   'price',
   'total.price',
   'bikeshop.name', 
   'location',
   'category.1',
   'category.2',
   'frame.material',
   'city',
   'state'   
]
df = df[cols_to_keep_list]

# * Renaming columns

'order.date'.replace('.','_')

df.columns = df.columns.str.replace(".","_")

bike_orderlines_wrangled_df = df

bike_orderlines_wrangled_df

# 6.0 Visualizing a Time Series ----

mkdir('00_data_wrangled')

bike_orderlines_wrangled_df.to_pickle(path = '00_data_wrangled/bike_orderlines_wrangled_df.pkl')

df = pd.read_pickle('00_data_wrangled/bike_orderlines_wrangled_df.pkl')

# 6.1 Total Sales by Month ----

df = pd.DataFrame(df)

df['order_date']

df['order_date'].dt.year

# Quick Plot ----


# Report Plot ----



# 6.2 Sales by Year and Category 2 ----

# ** Step 1 - Manipulate ----


# Step 2 - Visualize ----


# Simple Plot


# Reporting Plot



# 7.0 Writing Files ----


# Pickle ----


# CSV ----


# Excel ----


# WHERE WE'RE GOING
# - Building a forecast system
# - Create a database to host our raw data
# - Develop Modular Functions to:
#   - Collect data
#   - Summarize data and prepare for forecast
#   - Run Automatic Forecasting for One or More Time Series
#   - Store Forecast in Database
#   - Retrieve Forecasts and Report using Templates