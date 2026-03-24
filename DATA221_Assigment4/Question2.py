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

dt = DecisionTreeClassifier(criterion='entropy', random_state=42)
dt.fit(X_train, y_train)

print(f"Training Accuracy: {dt.score(X_train, y_train):.4f}")
print(f"Test Accuracy:     {dt.score(X_test, y_test):.4f}")

#Entropy measures the impurity of a node. The tree picks splits that maximise
#information gain (reduction in entropy). A pure node has entropy 0.
#Training accuracy = 100% but test accuracy is lower — this is overfitting.
#The unconstrained tree memorised the training data including noise.