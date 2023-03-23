

import pandas as pd
import pathlib
import os
from datetime import datetime

from my_pandas_extensions.database import read_forecast_from_database
from my_pandas_extensions.reporting import run_reports


def main():
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


    # REPORT TITLES ----

    titles = [
        "Sales Forecast: Total Revenue",
        "Sales Forecast: Category 1",
        "Sales Forecast: Category 2",
        "Sales Forecast: Bikeshops"
    ]

    # RUN REPORTS
    
    time_text = datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%p")
    dir_path = pathlib.Path.home()/'OneDrive'/'Desktop'/'sales_reports'
    
    # os.path.isdir(dir_path)
   # os.path.isdir(pathlib.Path.home()/'Desktop')
    
    print("Generating Reports...")
    
    run_reports(
        data            = df,
        id_sets         = id_sets,
        report_titles   = titles,
        directory       = dir_path,
        convert_to_html = True,
        convert_to_pdf  = True
    )

if __name__=="__main__":
    main()