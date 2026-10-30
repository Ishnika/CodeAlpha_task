#seasonal pattern 
df['Month'] = df['Date'].dt.month_name()

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

month_avg = df.groupby('Month')[rate].mean().reindex(month_order)

month_avg.plot(kind='bar', figsize=(10, 5))
plt.title("Average Unemployment Rate by Month")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.show()
