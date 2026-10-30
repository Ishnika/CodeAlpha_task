#the average unemployment rate in India, month by month.
monthly = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

monthly.plot(figsize=(10, 5), marker='o')
plt.title("Average Unemployment Rate in India Over Time")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Date")
plt.show()
