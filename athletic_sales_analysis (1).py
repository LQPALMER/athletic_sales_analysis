#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries and Dependencies
import pandas as pd


# ### 1. Combine and Clean the Data
# #### Import CSVs

# In[2]:


# Read the CSV files into DataFrames.
import pandas as pd

url = "https://raw.githubusercontent.com/LQPALMER/athletic_sales_analysis/main/Resources/athletic_sales_2020.csv"
url2 = "https://raw.githubusercontent.com/LQPALMER/athletic_sales_analysis/main/Resources/athletic_sales_2021.csv"
athletics_2020 = pd.read_csv(url)
athletics_2021 = pd.read_csv (url2)


# In[3]:


# Display the 2020 sales DataFrame
athletics_2020.head()


# In[4]:


# Display the 2021 sales DataFrame
athletics_2020.head()


# #### Check the data types of each DataFrame

# In[5]:


# Check the 2020 sales data types.
athletics_2020.dtypes


# In[6]:


# Check the 2021 sales data types.
athletics_2021.dtypes


# #### Combine the sales data by rows.

# In[7]:


# Combine the 2020 and 2021 sales DataFrames on the rows and reset the index.
_2020_2021_combined = pd.concat([athletics_2020,  athletics_2021], axis="rows", join='inner').reset_index(drop=True)


# In[8]:


# Check if any values are null.
_2020_2021_combined.dropna(inplace=True)


# In[9]:


# Check the data type of each column
print(_2020_2021_combined.dtypes)


# In[10]:


# Convert the "invoice_date" to a datetime datatype
_2020_2021_combined["invoice_date"] = pd.to_datetime(_2020_2021_combined["invoice_date"], format="mixed")


# In[11]:


# Confirm that the "invoice_date" data type has been changed.
print(_2020_2021_combined.dtypes)


# ### 2. Determine which Region Sold the Most Products

# #### Using `groupby`

# In[12]:


# Show the number of products sold for region, state, and city.
# Rename the sum to "Total_Products_Sold".
_2020_2021_groupby = _2020_2021_combined.groupby(['region', 'state', 'city'])['units_sold'].agg(Total_Products_Sold=("sum"))

_2020_2021_groupby = _2020_2021_groupby.rename(columns={'units_sold': 'Total_Products_Sold'})

# Show the top 5 results.
_2020_2021_groupby.sort_values(by=(["Total_Products_Sold"]), ascending=False)
_2020_2021_groupby.head()



# #### Using `pivot_table`

# In[13]:


# Show the number products sold for region, state, and city.
pivot_table_products_sold = pd.pivot_table(_2020_2021_combined,
                                           index=['region', 'state', 'city'], 
                                           values= 'units_sold', 
                                           aggfunc='sum')


# Rename the "units_sold" column to "Total_Products_Sold"
pivot_table_products_sold = pivot_table_products_sold.rename(columns={'units_sold': 'Total_Products_Sold'})




# Show the top 5 results.
pivot_table_products_sold = pivot_table_products_sold.sort_values(by='Total_Products_Sold', ascending=False)
pivot_table_products_sold.head()
                                   


# In[14]:


_2020_2021_combined.head()


# ### 3. Determine which Region had the Most Sales

# #### Using `groupby`

# In[15]:


# Show the total sales for the products sold for each region, state, and city.
# Rename the "total_sales" column to "Total Sales"
total_sales_grouped = _2020_2021_combined.groupby(['region', 'state', 'city'])['total_sales'].sum().reset_index()
total_sales_grouped.rename(columns={'total_sales': 'Total Sales'}, inplace=True)


# Show the top 5 results.
total_sales_grouped = total_sales_grouped.sort_values(by='Total Sales', ascending=False)
total_sales_grouped.head()


# #### Using `pivot_table`

# In[16]:


# Show the total sales for the products sold for each region, state, and city.
total_sales_grouped2 = pd.pivot_table(_2020_2021_combined,
                                     index=['region', 'state', 'city'], 
                                     values='units_sold', 
                                     aggfunc='sum')



                                                            
# Show the top 5 results.
total_sales_grouped2.sort_values(by=(['units_sold']), ascending=False)
total_sales_grouped2.head()


# ### 4. Determine which Retailer had the Most Sales

# #### Using `groupby`

# In[17]:


# Show the total sales for the products sold for each retailer, region, state, and city.
# Rename the "total_sales" column to "Total Sales"

total_sales_grouped2 = _2020_2021_combined.groupby(['retailer', 'region', 'state', 'city'])['total_sales'].sum().reset_index()
total_sales_grouped2.rename(columns={'total_sales': 'Total Sales'}, inplace=True)

# Show the top 5 results.
total_sales_grouped2.sort_values(by=(['Total Sales']), ascending=False)
total_sales_grouped2.head()


# In[18]:


_2020_2021_combined.head()


# #### Using `pivot_table`

# In[19]:


# Show the total sales for the products sold for each retailer, region, state, and city.
total_sales_grouped2 = pd.pivot_table(_2020_2021_combined,
                                     index=['region', 'state', 'city'], 
                                     values='total_sales', 
                                     aggfunc='sum')

# Optional: Rename the "total_sales" column to "Total Sales"
total_sales_grouped2.rename(columns={'total_sales': 'Total Sales'}, inplace=True)

# Show the top 5 results.
total_sales_grouped2.sort_values(by=(['Total Sales']), ascending=False)
total_sales_grouped2.head()


# ### 5. Determine which Retailer Sold the Most Women's Athletic Footwear

# #### Using `groupby`

# In[20]:


print(_2020_2021_combined.columns)


# In[21]:


# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
women_athletic_footwear_sales =  _2020_2021_combined[ _2020_2021_combined["product"].str.contains("Women's Athletic Footwear")]
womens_athletic_footwear_totals = women_athletic_footwear_sales.groupby(['retailer', 'region', 'state', 'city'])['units_sold'].sum().reset_index()
# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
womens_athletic_footwear_totals.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'}, inplace=True)

# Show the top 5 results.
womens_athletic_footwear_totals.head()


# #### Using `pivot_table`

# In[22]:


# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
pivot_table2 = _2020_2021_combined.pivot_table(index=['retailer','region', 'state', 'city'], values='total_sales', aggfunc='sum').reset_index()
# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
pivot_table2.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'}, inplace=True)

# Show the top 5 results.
pivot_table2.head()


# ### 6. Determine the Day with the Most Women's Athletic Footwear Sales

# In[23]:


# Create a pivot table where the 'invoice_date' column is the index, and the "total_sales" as the values.
pivot_table3 = _2020_2021_combined.pivot_table(index='invoice_date', values='total_sales')

# Optional: Rename the "total_sales" column to "Total Sales"
pivot_table3.rename(columns={'total_sales': 'Total Sales'}, inplace=True)

# Show the table.
pivot_table3


# In[24]:


# Resample the pivot table into daily bins, and get the total sales for each day.
daily_total_sales = pivot_table3.resample('D').sum()

# Sort the resampled pivot table in descending order by "Total Sales".
daily_total_sales = daily_total_sales.sort_index(ascending=False)


# ### 7.  Determine the Week with the Most Women's Athletic Footwear Sales

# In[25]:


# Resample the pivot table into weekly bins, and get the total sales for each week.
weekly_total_sales = pivot_table3.resample('W').sum()

# Sort the resampled pivot table in descending order on "Total Sales".
weekly_total_sales = weekly_total_sales.sort_index(ascending=False)

