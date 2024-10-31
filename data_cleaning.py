import numpy as np
import pandas as pd
import seaborn as sns
import os

data = {
    'name': ['DEVID','BAN','ANNY','BAN','ANNY','RIAN','JULIA','EMALY'],
    'age':[25,34,28,34,28,27,29,30],
    'salary':[50000,80000,60000,80000,60000,20000,40000,30000]
}

df = pd.DataFrame(data)
print(df)

df=df.drop_duplicates()
print(df)