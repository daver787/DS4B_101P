# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# SQL DATABASES (Module 2): Working with SQLAlchemy ----

# IMPORTS ----
import pandas as pd
import sqlalchemy as sql
# FUNCTION DEFINITION ----
def my_function(a =1):
    b = 1
    return a + b
my_function(a = 3)

def collect_data(conn_string = "sqlite:///00_database/bike_orders_database.sqlite"):
    
    # Body
    
    # 1.0 Connect to Database
    
    engine = sql.create_engine(conn_string)

    conn = engine.connect()
    
    table_names = ['bikes','bikeshops','orderlines']
    
    data_dict = {}
    for table in table_names:
        data_dict[table] = pd.read_sql(f"SELECT * FROM {table}", con = conn) \
            .drop("index", axis = 1)    
    
    conn.close()
    
    #2.0 Combining & Cleaning Data
    
    joined_df = pd.DataFrame(data_dict["orderlines"]) \
        .merge(
            right    = data_dict["bikes"],
            how      = "left",
            left_on  = "product.id",
            right_on = "bike.id"
        ) \
        .merge(
            right    = data_dict["bikeshops"],
            how      = "left",
            left_on  = "customer.id",
            right_on = "bikeshop.id"
        )    
    
    
    return joined_df

collect_data()