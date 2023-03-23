

import pathlib
import os

import pandas as pd
import numpy as np
import papermill as pm
import string
import pkg_resources

from pandas_flavor import register_dataframe_method
import glob
from tqdm import tqdm
from traitlets.config import Config
from nbconvert.preprocessors import TagRemovePreprocessor
from nbconvert.exporters import HTMLExporter, PDFExporter
from nbconvert.writers import FilesWriter

# Get Template Path
def get_template_path(path ="template/jupyter_report_template.ipynb"):
    return pkg_resources.resource_filename(__name__, path)

# Run Reports
@register_dataframe_method
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
        
        # NB CONVERT ----
        files = glob.glob(f"{directory}/*.ipynb")   
        
        # Convert to HTML
        if convert_to_html:     
            c = Config()
            c.TemplateExporter.exclude_input = True
            c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
            c.TagRemovePreproccesor.remove_all_outputs_tags = ("remove_output",)
            c.TagRemovePreprocessor.remove_input_tags = ("remove_input",)
            c.TagRemovePreprocessor.enabled = True
            fw =FilesWriter(config = c)
        
            print("Executing HTML Reports...")
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
            
            print("Creating PDF Reports...")
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