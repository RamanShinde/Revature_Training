

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

# Extract
customers=pd.read_csv("../data resources/customers.csv")
prodiuct=pd.read_csv("../data resources/product.csv")
orders=pd.read_csv("../data resources/orders.csv")

print('Customer: \n',customers.head())
print('product: \n',prodiuct.head())
print('orders: \n',orders.head())

# clean customer names and citie
customers['name']=customers['name'].str.title()
customers['city']=customers['city'].str.title()
customers['join_date']=pd.to_datetime(customers['join_date'])

#  Ensure The date to valid or not
orders['orders_date']=pd.to_datetime(orders['order_date'])

# Add deriver column
orders['avg_price_per_time']=orders['total_amount']/orders['quantity']

# join orders with product to incluse category
orders=orders.merge(prodiuct[['product_id','category']],on='product_id',how='left')
print("<----After Cleaning---->")
print('Customer: \n',customers.head())
print('product: \n',prodiuct.head())
print('orders After merge: \n',orders.head())

# Push to the bigquery
from google.cloud import bigquery

client=bigquery.Client(project="authentic-scout-477503-d8")
customer_table="authentic-scout-477503-d8.ecommerce_data.customers"
product_table="authentic-scout-477503-d8.ecommerce_data.prodiuct"
orders_table="authentic-scout-477503-d8.ecommerce_data.orders"

# Load Data Frame into bigquery
client.load_table_from_dataframe(customers,customer_table).result()
client.load_table_from_dataframe(prodiuct,product_table).result()
client.load_table_from_dataframe(orders,orders_table).result()

print("Data loaded successfully into bigquery")
