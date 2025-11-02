import numpy as np
import pandas as pd


'''
Basic usage and convention
pandas has two Datastructure

series:-it is 1D,Homogeneous,
dataframe:-2D,Heterogeneous,

'''
data=[1,2,3,4,5]
print(type(data))
series=pd.Series(data)
print(series)
print("Data type of series: ",type(series))

d=["Raman","Ashish"]
sd=pd.Series(d)
print(sd)

# Creting a Dataframe
dataf={
    'name':["Raman","Ashish","RaajDeep"],
    'age':[20,30,40],
    'City':['Latur',"Pune","Chennai"]
}
print(dataf)
print(type(dataf))

df=pd.DataFrame(dataf)
print('Head:-',df.head(2))
print("Tail:-",df.tail(2))
print("Information",df.info())
print("desc ",df.describe())  #It describe the only the Mathematics count it olny finde age column
print("Replace",df.replace(0,'Ramana'))

# Select the name coulmn
print("---Name--- \n",df['name'])
print("---Name,City--- \n",df[['name','City']])

# Filtering Rows
print(df[df['age']>20]) # it will return the age havinf greater than the Filterring

