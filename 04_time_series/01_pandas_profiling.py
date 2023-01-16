# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 4 (Time Series): Profiling Data ----


# IMPORTS

import pandas as pd
from pandas_profiling import ProfileReport, profile_report
from my_pandas_extensions.database import collect_data

df = collect_data()
df

# PANDAS PROFILING

# Get a Profile

profile = ProfileReport(df = df)

# Sampling - Big Datasets


# Pandas Helper
# ?pd.DataFrame.profile_report


# Saving Output


# VSCode Extension - Browser Preview



