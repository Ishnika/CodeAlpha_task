#predict a new flower 
sample = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=iris.feature_names)
print(iris.target_names[model.predict(sample)[0]])
