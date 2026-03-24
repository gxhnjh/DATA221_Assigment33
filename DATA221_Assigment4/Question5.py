import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import tensorflow as tf
from tensorflow.keras import layers, models

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Rebuild constrained decision tree
dt_c = DecisionTreeClassifier(criterion='entropy', max_depth=5,
                               min_samples_split=10, random_state=42)
dt_c.fit(X_train, y_train)

# Rebuild neural network
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

nn = models.Sequential([
    layers.Input(shape=(X_train_s.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
nn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
nn.fit(X_train_s, y_train, epochs=100, batch_size=16, verbose=0)




y_pred_dt = dt_c.predict(X_test)
y_pred_nn = (nn.predict(X_test_s, verbose=0).flatten() >= 0.5).astype(int)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred_dt),
                       display_labels=data.target_names).plot(ax=axes[0], colorbar=False)
axes[0].set_title("Decision Tree")

ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred_nn),
                       display_labels=data.target_names).plot(ax=axes[1], colorbar=False)
axes[1].set_title("Neural Network")

plt.tight_layout()
plt.savefig("q5_confusion_matrices.png", dpi=150)
plt.show()

#For a medical task, the Neural Network is preferred if it achieves higher accuracy.
#Decision Tree advantage: fully interpretable, easy to explain to clinicians.
#Decision Tree limitation: prone to overfitting without careful tuning.
#Neural Network advantage: captures complex non-linear patterns, often more accurate.
#Neural Network limitation: black-box — hard to explain individual predictions.