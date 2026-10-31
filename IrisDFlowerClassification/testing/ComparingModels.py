#compare other models 
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=200),
}

for name, m in models.items():
    m.fit(X_train, y_train)
    print(name, "accuracy:", round(accuracy_score(y_test, m.predict(X_test)), 3))
