# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 9 (Jupyter Automated Reporting, Part 1): Run Reports, Version 1 ----

# IMPORTS ----

import pathlib
import os

import pandas as pd
import numpy as np

from my_pandas_extensions.database import read_forecast_from_database


# COLLECT DATA ----

df = read_forecast_from_database()


# SELECTING REPORT ID'S ----

ids = df['id'].unique()

ids = pd.Series(ids)

ids_total     = ids[ids.str.startswith('Total')]
ids_cat_1     = ids[ids.str.startswith('Category 1')]
ids_cat_2     = ids[ids.str.startswith('Category 2')]
ids_bikeshops = ids[ids.str.startswith('Bikeshop')]

id_sets = [
    list(ids_total),
    list(ids_cat_1),
    list(ids_cat_2),
    list(ids_bikeshops)
]

id_sets


# REPORT TITLES ----

titles =[
    
    "Sales Forecast: Total Revenue",
    "Sales Forecast: Category 1",
    "Sales Forecast: Category 2",
    "Sales Forecast: Bikeshops"    
]

titles

# 1.0 HANDLING PATHS ----

# 1.1 TEMPLATE INPUT PATH ----

def get_template_path(path ="09_jupyter_papermill/template/jupyter_report_template.ipynb"):
    return pathlib.Path(path)

get_template_path()
# 1.2 REPORT OUTPUT PATH ----





# 2.0 BUILD REPORTING FUNCTION ----
# - Basic Reporting Function: Version 1



