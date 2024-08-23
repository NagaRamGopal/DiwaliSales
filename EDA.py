import pandas as pd
import pandas_profiling as pp
from pandas_profiling import ProfileReport

import matplotlib.pyplot as plt
import seaborn as sb

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
#This gives the average amount spent by male and female. Here we can even though pp of females>males, male's avg>female's avg.

age_spent_amount=df.groupby('Age Group')['Amount'].sum()
age_spent_amount.plot(kind='bar')
plt.xlabel('Age Group')
plt.ylabel('Amount')
plt.show()
#Throught this we can see 26-35 spends more than other age groups.


sb.countplot(df, x='Age Group', hue='Gender')
#This gives the Age Group spending amount divided by gender.

tv=sb.countplot(df, x='Age Group', hue='Gender')
for bars in tv.containers:
  tv.bar_label(bars)
#This gives the same but also includes values

#This conlcudes most of the buyers are females from 26-35 age.


state_amount=df.groupby('State')['Amount'].sum()
print(state_amount)
#We can see the amount spent for diwali from each state.


#We can see numbers of orders was placed from each state
state_orders=df.groupby('State')['Orders'].sum().sort_values(ascending=False)
state_orders.plot(kind='bar')
plt.xlabel('State')
plt.ylabel('Orders')
plt.show()


marital_analysis=df.groupby('Marital_Status')['Amount'].sum()
marital_analysis.plot(kind='bar',xlabel='Marital_Status', ylabel='Amount')
#Here we can see that persons who are not married are spending more.

occupation_analysis=df.groupby('Occupation')['Amount'].sum().sort_values(ascending=False)
print(occupation_analysis)
occupation_analysis.plot(kind='bar', xlabel='Occupation', ylabel='Amount')
#Here we can see that It sector people are spending more and Agriculture sector people are least spending.

plt.figure(figsize=(20, 6))
oa=sb.countplot(df,x='Occupation')
for bars in oa.containers:
  oa.bar_label(bars)