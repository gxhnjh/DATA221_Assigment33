import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras import layers, models

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)




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

print(f"Training Accuracy: {nn.evaluate(X_train_s, y_train, verbose=0)[1]:.4f}")
print(f"Test Accuracy:     {nn.evaluate(X_test_s,  y_test,  verbose=0)[1]:.4f}")

#Feature scaling is necessary because gradient-based optimisation is sensitive
#to feature magnitudes. Unscaled features cause uneven gradient updates and
#slow or unstable training. Standardisation ensures equal contribution from all features.
#An epoch is one complete pass through the entire training dataset.