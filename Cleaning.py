import pandas as pd
import numpy as np

df=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\DiwaliSalesAnalysis\DiwaliSales\Diwali Sales Data.csv', encoding='windows-1252')



#Removing Status, Unanmes columns as they don't carry any value

df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


#checking null values
df.isnull().sum()
df.shape

df.dropna(inplace=True) #Dropping null values from amount as we observed 12 values were dropped.
df.shape

#Converting Amount to Integer with nearest one.
df['Amount']=df['Amount'].astype(int)
df['Amount'].dtype



#Renaming Martial Status values as Not Married and Married.
df['Marital_Status'] = df['Marital_Status'].replace({0: 'Not Married', 1: 'Married'})

print(df[['Age', 'Amount', 'Orders']].describe())

