# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 10 (Jupyter Automated Reporting, Part 2): Run Reports, Version 2 ----

# IMPORTS ----

import pathlib
import os
import string

import pandas as pd
import numpy as np

import papermill as pm

from my_pandas_extensions.database import read_forecast_from_database

# >>> ADD IMPORTS <<<
import glob
from tqdm import tqdm
from traitlets.config import Config
from nbconvert.preprocessors import TagRemovePreprocessor
from nbconvert.exporters import HTMLExporter, PDFExporter
from nbconvert.writers import FilesWriter

# COLLECT DATA ----

df = read_forecast_from_database()

# SELECTING REPORT ID'S ----
ids = df['id'].unique()
ids = pd.Series(ids)

ids_total = ids[ids.str.startswith('Total')]
ids_cat_1 = ids[ids.str.startswith('Category 1')]
ids_cat_2 = ids[ids.str.startswith('Category 2')]
ids_bikeshops = ids[ids.str.startswith('Bikeshop')]

id_sets = [
    list(ids_total),
    list(ids_cat_1),
    list(ids_cat_2),
    list(ids_bikeshops)
]

id_sets


# REPORT TITLES ----

titles = [
    "Sales Forecast: Total Revenue",
    "Sales Forecast: Category 1",
    "Sales Forecast: Category 2",
    "Sales Forecast: Bikeshops"
]

titles


# TEMPLATE INPUT PATH ----

def get_template_path(path='09_jupyter_papermill/template/jupyter_report_template.ipynb'):
    return path

get_template_path()


# 1.0 MODIFY REPORTING FUNCTION ----
# - Upgraded Reporting Function: Version 2
# - Add HTML and PDF reporting



# Test reporting.py version 2
run_reports(
    data            = df,
    id_sets         = id_sets,
    report_titles   = titles,
    directory       = "10_jupyter_html_pdf/sales_reports/",
    convert_to_html = True,
    convert_to_pdf  = True
    )

