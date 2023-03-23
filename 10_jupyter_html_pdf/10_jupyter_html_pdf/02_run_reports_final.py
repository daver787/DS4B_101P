# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Module 10 (Jupyter Automated Reporting, Part 2): Run Reports, Version 2 ----

# IMPORTS ----

import pathlib
import os
import string

import pandas as pd
import numpy as np

import papermill as pm
import pkg_resources

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

def run_reports(data,
                id_sets         = None,
                report_titles   = None,
                directory       = "reports/",
                convert_to_html = False,
                convert_to_pdf  = False):
    
    # Make the directory if not created
    
    dir_path = pathlib.Path(directory)
    directory_exists = os.path.isdir(dir_path)
    if not directory_exists:
        print(f'Making Directory at {str(dir_path.absolute())}')
        os.mkdir(dir_path)
    
    #Make PaperMill Jupyter Notebooks
    print("Executing PaperMill Jupyter Reports...")
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
    
    files = glob.glob(f"{directory}/*.ipynb")   
    
    if convert_to_html:         
        c = Config()
        c.TemplateExporter.exclude_input = True
        c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
        c.TagRemovePreproccesor.remove_all_outputs_tags = ("remove_output",)
        c.TagRemovePreprocessor.remove_input_tags = ("remove_input",)
        c.TagRemovePreprocessor.enabled = True
        fw =FilesWriter(config = c)
        
        for file in tqdm(files):
            file_path = pathlib.Path(file)
            file_name = file_path.stem
            file_dir  = file_path.parents[0]

            (body, resources) = HTMLExporter(config = c).from_filename(file_path)
            file_dir_html = str(file_dir) + "_html"
            c.FilesWriter.build_directory = str(file_dir_html)
            fw =FilesWriter(config = c)
            fw.write(body, resources, notebook_name = file_name)
    
    if convert_to_pdf:
        c = Config()
        c.TemplateExporter.exclude_input = True
        c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
        c.TagRemovePreproccesor.remove_all_outputs_tags = ("remove_output",)
        c.TagRemovePreprocessor.remove_input_tags = ("remove_input",)
        c.TagRemovePreprocessor.enabled = True
        fw =FilesWriter(config = c)
        for file in tqdm(files):
            file_path = pathlib.Path(file)
            file_name = file_path.stem
            file_dir  = file_path.parents[0]
            (body, resources) = PDFExporter(config = c).from_filename(file_path)
            file_dir_pdf = str(file_dir) + "_pdf"
            c.FilesWriter.build_directory = str(file_dir_pdf)
            fw = FilesWriter(config = c)
            fw.write(body, resources, notebook_name = file_name) 
    print("Reporting complete.")                           
    pass

# Test reporting.py version 2

from my_pandas_extensions.reporting import run_reports

run_reports(
    data            = df,
    id_sets         = id_sets,
    report_titles   = titles,
    directory       = "10_jupyter_html_pdf/sales_reports/",
    convert_to_html = True,
    convert_to_pdf  = True
    )

