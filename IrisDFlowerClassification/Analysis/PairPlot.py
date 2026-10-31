#this chart distinguishes the three flowers based on size setosa is seprated completely 
sns.pairplot(df.drop(columns='target'), hue='species')
plt.show()
