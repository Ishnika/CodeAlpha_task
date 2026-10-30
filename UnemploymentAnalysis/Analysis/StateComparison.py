#the 10 states with the highest average unemployment rate over the whole period.
state_avg = df.groupby('Region')[rate].mean().sort_values(ascending=False)

state_avg.head(10).plot(kind='bar', figsize=(10, 5))
plt.title("Top 10 States by Average Unemployment Rate")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("State")
plt.xticks(rotation=45)
plt.show()
