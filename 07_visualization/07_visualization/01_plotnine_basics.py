# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 7 (Plotnine): Plot Anatomy ----

# Imports
import pandas as pd
import numpy as np

from my_pandas_extensions.database import collect_data
from my_pandas_extensions.timeseries import summarize_by_time
from my_pandas_extensions.forecasting import arima_forecast

from plotnine import *
from mizani.formatters import dollar_format


# Data

df = collect_data()

# VISUALIZATION ----

# Step 1: Data Summarization

bike_sales_y_df = df\
    .summarize_by_time(
        date_column  = "order_date",
        value_column = "total_price",
        rule         = "Y",
        kind         = "timestamp"
    )\
        .reset_index()

# Step 2: Plot ----
# - Canvas: Set up column mappings
# - Geometries: Add geoms
# - Format: Add scales, labs, theme

g = (
    # Canvas
    ggplot(
        mapping = aes(x = "order_date", y = "total_price"),
        data    = bike_sales_y_df
    )
    
    #Geometries
    + geom_col(fill = "#2C3E50")
    + geom_smooth(
        method = "lm",
        se     = False,
        color  ="dodgerblue"
        )
    + expand_limits(y = [0, 20e6])
    + scale_y_continuous(
        labels = dollar_format(prefix = "$", big_mark="," , digits = 0))
    + scale_x_datetime(
        date_labels ="%Y",
        date_breaks = "2 years"
    )
    + labs(
        title = "Revenue by Year",
        x = "",
        y = "Revenue"
    )
    +theme_minimal()
)

g

# Saving a plot ----

g.save("07_visualization/bike_sales_y.jpg")

# What is a plotnine plot? ----

type(g)
g.data
g.draw()

m = g.draw()

type(m)