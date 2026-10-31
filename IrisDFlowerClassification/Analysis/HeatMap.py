#heat map shows how strongly each petals measurements are related 
corr = df.drop(columns=['target', 'species']).corr()

sns.heatmap(corr, annot=True, cmap='Blues')
plt.title("Correlation between measurements")
plt.show()
