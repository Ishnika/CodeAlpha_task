#data cleaning : fixes column name and data type 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Unemployment in India.csv")
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'].str.strip(), dayfirst=True)
rate = df.columns[3]
