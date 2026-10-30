df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'].str.strip(), dayfirst=True)
df.isnull().sum()
