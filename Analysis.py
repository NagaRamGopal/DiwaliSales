import pandas as pd
import numpy as np
import pandas_profiling as pp
from pandas_profiling import ProfileReport
#Looks like file is corrupted. So we are using encoding.
df=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\DiwaliSalesAnalysis\DiwaliSales\Diwali Sales Data.csv', encoding='windows-1252')

print(df.shape)
print(df.head())
print(df.info())

rpt=ProfileReport(df, title="Diwali Sales")
rpt.to_file("Diwali Sales.html")