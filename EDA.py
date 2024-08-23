import pandas as pd
import pandas_profiling as pp
from pandas_profiling import ProfileReport

df=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\DiwaliSalesAnalysis\DiwaliSales\CleanedData.csv')
rpt=ProfileReport(df, title="Final Data")
rpt.to_file("FinalData.html")