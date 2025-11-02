import pandas as pd

data_list=[1,2,3,4,5,6]
series=pd.Series(data_list)

print(series)
print(series.index)
print(series.dtype)
print("Print 1-4 ",series[1:4])
print("Print upto :4 ",series[:4])
print("Print from 3 to end ",series[3:])

li=pd.Series([10,20,30,40,50,60])
print(series+li)

#DataFrame
import numpy as np
data_array=np.array([["Raman",20,"Latur"],
                    ["Raj",28,"Pune"],
                     ["Ashish",30,"Noida"]])

