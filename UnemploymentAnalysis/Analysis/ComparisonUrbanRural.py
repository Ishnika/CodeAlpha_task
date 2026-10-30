#urban vs rural 
area_avg = df.groupby('Area')[rate].mean()

area_avg.plot(kind='bar', figsize=(6, 5))
plt.title("Average Unemployment Rate: Urban vs Rural")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Area")
plt.xticks(rotation=0)
plt.show()

print(area_avg.round(2))
