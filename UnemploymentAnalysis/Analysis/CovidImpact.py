#covid impact by state
before_state = df[df['Date'] < '2020-03-25'].groupby('Region')[rate].mean()
after_state = df[df['Date'] >= '2020-03-25'].groupby('Region')[rate].mean()

change = (after_state - before_state).sort_values(ascending=False)

change.head(10).plot(kind='bar', figsize=(10, 5))
plt.title("Top 10 States by Increase in Unemployment After Lockdown")
plt.ylabel("Increase (percentage points)")
plt.xlabel("State")
plt.xticks(rotation=45)
plt.show()
