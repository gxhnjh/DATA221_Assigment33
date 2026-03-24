import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models



np.random.seed(42)
tf.random.set_seed(42)



(X_train_f, y_train_f), (X_test_f, y_test_f) = tf.keras.datasets.fashion_mnist.load_data()

# Normalize and reshape
X_train_f = X_train_f.astype('float32') / 255.0
X_test_f = X_test_f.astype('float32') / 255.0
X_train_f = X_train_f.reshape(-1, 28, 28, 1)
X_test_f = X_test_f.reshape(-1, 28, 28, 1)

cnn = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
cnn.fit(X_train_f, y_train_f, epochs=15, batch_size=64, verbose=1)

print(f"Test Accuracy: {cnn.evaluate(X_test_f, y_test_f, verbose=0)[1]:.4f}")

#CNNs are preferred over fully connected networks for images because they use
#shared convolutional filters that detect spatial patterns regardless of position,
#using far fewer parameters than a fully connected network.
#The Conv2D layer learns low-level features like edges and textures in early layers,
#which combine into higher-level shapes that distinguish clothing categories.