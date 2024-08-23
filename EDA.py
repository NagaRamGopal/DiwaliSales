import pandas as pd
import pandas_profiling as pp
from pandas_profiling import ProfileReport

import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\DiwaliSalesAnalysis\DiwaliSales\CleanedData.csv')

rpt=ProfileReport(df, title="Final Data")
rpt.to_file("FinalData.html")

amt_by_gender=df.groupby('Gender')['Amount'].sum()
print(amt_by_gender)


amt_by_gender.plot(kind='bar', color=('Pink', 'Blue')) 
plt.xlabel('Gender')
plt.ylabel('Amount')
plt.show()
#Through this we can see Female's spend more than male's. So purchasing power of female>male.

avg_amt=df.groupby('Gender')['Amount'].mean()
print(avg_amt.astype(int))
#This gives the average amount spent by male and female.

