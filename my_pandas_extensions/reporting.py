

import pathlib
import os

import pandas as pd
import numpy as np
import papermill as pm
import string
import pkg_resources

from pandas_flavor import register_dataframe_method
from my_pandas_extensions.database import read_forecast_from_database

# Get Template Path
def get_template_path(path ="template/jupyter_report_template.ipynb"):
    return pkg_resources.resource_filename(__name__, path)

# Run Reports
@register_dataframe_method
def run_reports(data,
                id_sets       = None,
                report_titles = None,
                directory     = "reports/"):
    
    # Make the directory if not created
    
    dir_path = pathlib.Path(directory)
    directory_exists = os.path.isdir(dir_path)
    if not directory_exists:
        print(f'Making Directory at {str(dir_path.absolute())}')
        os.mkdir(dir_path)
    
    #Make PaperMill Jupyter Notebooks
    for i, id_set in enumerate(id_sets):
        
        # Input Filename
        input_path    = get_template_path()
        
        # Output Path
        report_title = report_titles[i]
        
        file_name = report_title\
        .translate(
        str.maketrans('','',string.punctuation)
        )\
        .lower()\
        .replace(" ","_")
        
        output_path = pathlib.Path(f'{directory}/{file_name}.ipynb')  

        #Parameters
        params = {
            'ids'  : id_set,
            'title': report_title,
            'data' : data.to_json()
        }

        pm.execute_notebook(
        input_path  = input_path,
        output_path = output_path,
        parameters  = params,
        report_mode = True
        )
    pass