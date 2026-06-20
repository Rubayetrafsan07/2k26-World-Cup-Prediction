import pandas as pd

df = pd.read_csv('data/raw/results.csv')

print(df.head())

print(df.info())

print(df.columns)

print(df.isnull().sum())

print(df.duplicated().sum())

df["date"] = pd.to_datetime(df["date"])   

print(df.info())

df = df.dropna(subset=["home_score","away_score"]) 
print(df.shape)

df["home_score"] = df["home_score"].astype(int)  
df["away_score"] = df["away_score"].astype(int)  

df.to_csv("data/processed/result_clean.csv", index= False)  

