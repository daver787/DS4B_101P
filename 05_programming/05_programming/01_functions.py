# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 5 (Programming): Functions ----

# Imports

import pandas as pd
import numpy as np
from my_pandas_extensions.database import collect_data


df = collect_data()

# 1.0 EXAMINING FUNCTIONS ----

# Pandas Series Function
# ?pd.Series.max
# ?np.max

?pd.Series.max

df.total_price.max()

pd.Series.max("a")

my_max = pd.Series.max

my_max(df.total_price)

type(my_max)

type(pd.Series.max)

# Pandas Data Frame Function
# ?pd.DataFrame.aggregate

pd.DataFrame.aggregate(
    self = df,
    func = np.sum
)

df.aggregate(func = np.sum)

pd.DataFrame.aggregate(
    self = df[['total_price']],
    func = np.quantile,
    q    = 0.5
)

# 2.0 OUTLIER DETECTION FUNCTION ----
# - Works with a Pandas Series

x = df['total_price']


def detect_outliers(x):
    
    return x

detect_outliers(x)

# 3.0 EXTENDING A CLASS ----

