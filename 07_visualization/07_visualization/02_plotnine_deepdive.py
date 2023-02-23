# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 7 (Plotnine): Plotnine Deep-Dive ----

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from my_pandas_extensions.database import collect_data
from my_pandas_extensions.timeseries import summarize_by_time

import plotnine
from plotnine import *

# Matplotlib stylings


# Data

df = collect_data()

# 1.0 Scatter Plots ----
# - Great for Continuous vs Continuous

# Goal: Explain relationship between order line value
#  and quantity of bikes sold

#Step 1: Data Manipulation
quantity_total_price_by_order_df = df[['order_id', 'quantity', 'total_price']]\
    .groupby('order_id')\
    .sum()\
    .reset_index()        

# Step 2: Data Visualization
(
    ggplot(
        mapping = aes(x = 'quantity', y = 'total_price'),
        data    = quantity_total_price_by_order_df
    )
    + geom_point(alpha = 0.5)
    + geom_smooth(method = 'lm')   
)

# 2.0 Line Plot ----
# - Great for time series

# Goal: Describe revenue by Month, expose cyclic nature

# Step 1: Data Manipulation

bike_sales_m_df = df\
    .summarize_by_time(
        date_column  = "order_date",
        value_column = "total_price",
        rule         = "M",
        kind         = "timestamp"
    )\
    .reset_index()    

# Step 2: Plot
(
    ggplot(
        mapping = aes('order_date', 'total_price'),
        data    = bike_sales_m_df 
    )
    + geom_line()
    + geom_smooth(method = "lm", se = False)
    + geom_smooth(
        method = "lowess",
        se     = False,
        span   = 0.2,
        color  = "dodgerblue"
        ) 
)



# 3.0 Bar / Column Plots ----
# - Great for categories

# Goal: Sales by Descriptive Category

# Step 1: Data Manipulation


# Aside: Categorical Data (pd.Categorical)
# - Used frequently in plotting to designate order of categorical data



# Step 2: Plot



# 4.0 Histogram / Density Plots ----
# - Great for inspecting the distribution of a variable

# Goal: Unit price of bicycles

# Histogram ----

# Step 1: Data Manipulation


# Step 2: Visualize


# Density ----




# 5.0 Box Plot / Violin Plot ----
# - Great for comparing distributions

# Goal: Unit price of model, segmenting by category 2

# Step 1: Data Manipulation



# Step 2: Visualize

# Box Plot



# Violin Plot & Jitter Plot



# 6.0 Adding Text & Label Geometries----

# Goal: Exposing sales over time, highlighting outlier

# Data Manipulation



# Adding text to bar chart
# Filtering labels to highlight a point



# 7.0 Facets, Scales, Themes, and Labs ----
# - Facets: Used for visualizing groups with subplots
# - Scales: Used for transforming x/y axis and colors/fills
# - Theme: Used to adjust attributes of the plot
# - Labs: Used to adjust title, x/y axis labels

# Goal: Monthly Sales by Categories

# Step 1: Format Data


# Step 2: Visualize








