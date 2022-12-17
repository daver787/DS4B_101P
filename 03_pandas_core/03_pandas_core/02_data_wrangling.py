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

# Select by data types
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

# Dropping Columns (De-selecting)



# 2.0 ARRANGING ROWS ----




# 3.0 FILTERING  ----

# Simpler Filters


# Query


# Filtering Items in a List


# Slicing


# Index Slicing


# Unique / Distinct Values


# Top / Bottom


# Sampling Rows



# 4.0 ADDING CALCULATED COLUMNS (MUTATING) ----


# Method 1 - Series Notations


# Method 2 - assign (Great for method chaining)



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





