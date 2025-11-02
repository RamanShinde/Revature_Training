
import pandas as pd

data=pd.DataFrame({'A':[1,2,3],
                   'B':[4,5,6],
                   'c':[7,8,9]})

data.to_csv('data.csv')

df=pd.read_csv('data.csv')
print(df)

import sqlite3
# Create an in-memory SQLite database and insert the sample Data