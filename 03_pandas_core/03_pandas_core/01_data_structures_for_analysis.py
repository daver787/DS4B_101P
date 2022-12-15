# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 3 (Pandas Core): Data Structures ----

# IMPORTS ----

import pandas as pd
import numpy as np
from my_pandas_extensions.database import collect_data

df = collect_data()

df
# 1.0 HOW PYTHON WORKS - OBJECTS

# Objects

type(df)

# Classes have objects

type(df).mro()

type("string").mro()

# Objects have attributes

df.shape
df.columns

# Objects have methods

df.query("model == 'Jekyll Carbon 2'")


# 2.0 KEY DATA STRUCTURES FOR ANALYSIS

# - PANDAS DATA FRAME

df
type(df)

# - PANDAS SERIES

type(df['order_date'])
df["order_date"].dt.year
df.dt

# - NUMPY

type(df["order_date"].values).mro()

df["order_date"].values.dtype

# -Data Types

type(df['price'].values).mro()

df['price'].values.dtype

# 3.0 DATA STRUCTURES - PYTHON

# Dictionaries



# Lists



# Tuples


# Base Data Types




# Casting


