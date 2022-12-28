# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# Week 2 (Data Wrangling): Data Wrangling ----

# IMPORTS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# DATA

from my_pandas_extensions.database import collect_data

df = collect_data()
df

# 1.0 SELECTING COLUMNS

# Select by name

df[['order_date','order_id','order_line']]

df['order_date']
df[['order_date']]

# Select by position

df.iloc[:, 0:3]

df.iloc[:, -3:]


# Select by text matching

df.filter(regex = "(^model)|(^cat)", axis = 1)

df.filter(regex = "price$", axis = 1)

df.filter(regex = "(price$)|(date$)", axis = 1)

# Rearranging columns
#Single
l = df.columns.to_list()

l.remove('model')

['model', *l]

df[['model', *l]]

# Multiple Columns
l = df.columns.to_list()
l.remove('model')
l.remove('category_1')
l.remove('category_2')

df[['model', 'category_1', 'category_2', *l]]


# - List Comprehension

l = df.columns.to_list()
l

cols_to_front = ['model', 'category_1', 'category_2']

l2 = [col for col in l if col not in cols_to_front]

df[[*cols_to_front, *l2]]

# Select by data types

df.info()

df1 = df.select_dtypes(include = 'object')

df2 = df.select_dtypes(exclude = 'object')

pd.concat([df1, df2], axis = 1)

# Moving Columns to the Front (Data Frame Seleection)

df1 = df[['model', 'category_1', 'category_2']]

df2 = df.drop(['model', 'category_1', 'category_2'], axis = 1)

pd.concat([df1, df2], axis = 1)

# Dropping Columns (De-selecting)

df.drop(['model', 'category_1', 'category_2'], axis = 1)

# 2.0 ARRANGING ROWS ----

df.sort_values('total_price', ascending = False)

df.sort_values('order_date', ascending = False)

df['price'].sort_values(ascending = False)

# 3.0 FILTERING  ----

# Simpler Filters

df.order_date >= pd.to_datetime('2015-01-01')

df[df.order_date >= pd.to_datetime('2015-01-01')]

df[df.model == "Trigger Carbon 1"]

df[df.model.str.startswith("Trigger")]

df[df.model.str.contains("Carbon")]

# Query

price_threshold_1 = 9000

price_threshold_2 = 1000

df.query("price >= @price_threshold_1 | price <= @price_threshold_2")

df.query(f"price >= {price_threshold_1}")


# Filtering Items in a List

df['category_2'].unique()

df['category_2'].value_counts()

df[df['category_2'].isin(['Triathlon','Over Mountain'])]

df[~df['category_2'].isin(['Triathlon','Over Mountain'])]

# Slicing

df[:5]

df.head(5)

df.tail(5)


# Index Slicing

df.iloc[0:5, [1, 3, 5]]

df.iloc[0:5]

df.iloc[:, [1, 3, 5]]

# Unique / Distinct Values

df[['model', 'category_1', 'category_2', 'frame_material']]\
    .drop_duplicates()

df['model'].unique()

# Top / Bottom

df.nlargest(n = 20, columns = 'total_price')

df['total_price'].nlargest(n = 20)

df.nsmallest(n = 20, columns = 'total_price')

# Sampling Rows

df.sample(n = 10, random_state = 123)

df.sample(frac = 0.10, random_state = 123)

# 4.0 ADDING CALCULATED COLUMNS (MUTATING) ----


# Method 1 - Series Notations

df2 = df.copy()

df2['new_col'] = df2['price'] * df2['quantity']

df2['new_col_2'] = df2['model'].str.lower()

df2
# Method 2 - assign (Great for method chaining)

df.assign(frame_material = lambda x:x['frame_material'].str.lower())

df.assign(frame_material_lower = lambda x: x['frame_material'].str.lower())

df[['model','price']] \
    .drop_duplicates() \
    .assign(price = lambda x: np.log(x['price']))\
    .set_index('model') \
    .plot(kind = 'hist')     
                
# Adding Flags (True/False)



# Binning



# 5.0 GROUPING  ----

# 5.1 Aggregations (No Grouping)


# Common Summaries


# 5.2 Groupby + Agg


# Get the sum and median by groups


# Apply Summary Functions to Specific Columns


# Detecting NA


# 5.3 Groupby + Transform 
# - Note: Groupby + Assign does not work. No assign method for groups.


# 5.4 Groupby + Filter




# 6.0 RENAMING ----

# Single Index


# Targeting specific columns


# - Mult-Index



# 7.0 RESHAPING (MELT & PIVOT_TABLE) ----

# Aggregate Revenue by Bikeshop by Category 1 


# 7.1 Pivot & Melt 

# Pivot (Pivot Wider)


# Melt (Pivoting Longer)



# 7.2 Pivot Table (Pivot + Summarization, Excel Pivot Table)



# 7.3 Stack & Unstack ----

# Unstack - Pivots Wider 1 Level (Pivot)

# Stack - Pivots Longer 1 Level (Melt)


# 8.0 JOINING DATA ----


# Merge (Joining)


# Concatenate (Binding)

# Columns 


# Rows 



# 9.0 SPLITTING (SEPARATING) COLUMNS AND COMBINING (UNITING) COLUMNS

# Separate


# Combine



# 10.0 APPLY 
# - Apply functions across rows 



# 11.0 PIPE 
# - Functional programming helper for "data" functions





