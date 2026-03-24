from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)



dt_c = DecisionTreeClassifier(criterion='entropy', max_depth=5,
                               min_samples_split=10, random_state=42)
dt_c.fit(X_train, y_train)

print(f"Training Accuracy: {dt_c.score(X_train, y_train):.4f}")
print(f"Test Accuracy:     {dt_c.score(X_test, y_test):.4f}")

importances = dt_c.feature_importances_
indices = np.argsort(importances)[::-1]
print("\nTop 5 Most Important Features:")
for i in range(5):
    print(f"  {i+1}. {data.feature_names[indices[i]]:<35} {importances[indices[i]]:.4f}")

#Limiting max_depth and min_samples_split stops the tree from memorising noise,
#reducing the training-test gap and improving generalisation.
#Feature importances show which features drive decisions, making the model
#interpretable — clinicians can see exactly what the model relies on.