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


def detect_outliers(x, iqr_mutiplier = 1.5, how = "both"):
    
    # IQR LOGIC
    
    q75 = np.quantile(x, 0.75)
    q25 = np.quantile(x, 0.25)
    iqr = q75 - q25
    
    lower_limit = q25 - iqr_mutiplier * iqr
    upper_limit = q75 + iqr_mutiplier * iqr
    
    outliers_upper = x >= upper_limit
    outliers_lower  = x <= lower_limit
    
    if how == "both":
        outliers = outliers_upper | outliers_lower
    elif how == "lower":
        outliers = outliers_lower
    else:
        outliers = outliers_upper        
    
    return outliers

detect_outliers(df['total_price'], iqr_mutiplier= 0.9, how = "lower")

df[detect_outliers(df['total_price'], iqr_mutiplier= 0.3, how = "lower")]

# 3.0 EXTENDING A CLASS ----

