# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 9 (Jupyter Automated Reporting): Papermill Automation ----

# IMPORTS ----

import pandas as pd
import numpy as np

import papermill as pm
import pathlib
import os

from my_pandas_extensions.database import read_forecast_from_database

# COLLECT DATA ----

df = read_forecast_from_database()

# 1.0 SELECTING REPORT ID'S ----
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

# 2.0 SETUP DIRECTORY ----

# Make the report directory if doesn't already exist

directory = "09_jupyter_papermill/reports/"

dir_path = pathlib.Path(directory)

str(dir_path.absolute())

dir_path.name

os.mkdir(dir_path)

os.path.isdir(dir_path)

os.path.isdir("test")

directory_exists = os.path.isdir(dir_path)

if not directory_exists:
    print(f'Making Directory at {str(dir_path.absolute())}')
    os.mkdir(dir_path)

# 3.0 MAKE JUPYTER TEMPLATE ----
# - Convert Analysis to a Papermill Template
# - Parameterize key variables:
#   - ids
#   - title
#   - data: Note that data will be passed as json

# 4.0 PAPERMILL ----

# Iterating without a loop




# Iterating with for-loop and enumerate()




