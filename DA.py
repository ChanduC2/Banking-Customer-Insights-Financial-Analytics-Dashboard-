import pymysql
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Connect to server
cnx = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Chandu@123")

query = "select * from banking_cases.customer"
df = pd.read_sql(query,cnx)
cnx.close()
print(df)
df.head()
df.tail()
df.info()
df.describe
df=pd.read_csv(r"D:\DA Project\Banking.csv")
df.head()
df.describe()

#Numerical data into Categorical data using Bins
bins = [0,100000,300000,float('inf')]
labels = ['Low','Medium','High']
df['Income Band'] = pd.cut(df['Estimated Income'], bins=bins,labels=labels,right=False)
df['Income Band'].value_counts()
df['Income Band'].value_counts().plot(kind = 'bar')
plt.show()


bins = [0,100000,300000,float('inf')]
labels = ['Low',"Medium","High"]
df['Acount Band'] = pd.cut(df['Foreign Currency Account'],bins = bins,labels=labels,right = False)
df['Acount Band'].value_counts()
df['Acount Band'].value_counts().plot(kind = 'bar')
plt.show()

#Examine the distribution of unique categories in categorical columns
#univariate analysis - It means analyzing one variable at a time
categorical_col = df[["Nationality","Occupation","Fee Structure","Loyalty Classification","Amount of Credit Cards","Properties Owned","Risk Weighting","BRId","GenderId","IAId","Income Band"]]
for col in categorical_col:
    print(f"count values '{col}' :")
    display(df[col].value_counts().plot(kind='bar'))
    plt.show()
    
#Bivariate Analysis - It is the examination of two variables to understand the relationship, pattern, or comparisionn between them.
target_col = "Nationality"
categorical_col = df[["Nationality","Occupation","Fee Structure","Loyalty Classification","Amount of Credit Cards","Properties Owned","Risk Weighting","BRId","GenderId","IAId","Income Band"]]
for col in categorical_col:
    print(f"count values '{col} vs {target_col}' :")
    sns.countplot(data=df, x=col, hue=target_col, order=df[col].value_counts().index)
    plt.show()

#Histogram
for col in categorical_col:
    if col == "Occupation":
        continue
    plt.figure(figsize=(8,4))
    sns.histplot(df[col])
    plt.title("Histo gram of Occupation count")
    plt.xlabel(col)
    plt.ylabel("count")
    plt.show()  

numerical_cols = df[["Age","Location ID","Estimated Income","Superannuation Savings","Amount of Credit Cards","Amount of Credit Cards","Bank Loans","Bank Deposits","Checking Accounts","Saving Accounts","Foreign Currency Account","Business Lending"]]  
for col in numerical_cols:
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.show()

numerical_cols = df[["Age","Location ID","Estimated Income","Superannuation Savings","Amount of Credit Cards","Amount of Credit Cards","Bank Loans","Bank Deposits","Checking Accounts","Saving Accounts","Foreign Currency Account","Business Lending"]] 
plt.figure(figsize=(15,8))
for i,col in enumerate(numerical_cols):
    plt.subplot(4,3,i+1)
    sns.histplot(df[col],kde=True)
    plt.title(col)
    plt.show()


    








    

    
    