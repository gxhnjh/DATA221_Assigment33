import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import tensorflow as tf
from tensorflow.keras import layers, models

np.random.seed(42)
tf.random.set_seed(42)

# Rebuild Fashion MNIST data and CNN
(X_train_f, y_train_f), (X_test_f, y_test_f) = tf.keras.datasets.fashion_mnist.load_data()
X_train_f = X_train_f.astype('float32') / 255.0
X_test_f  = X_test_f.astype('float32')  / 255.0
X_train_f = X_train_f.reshape(-1, 28, 28, 1)
X_test_f  = X_test_f.reshape(-1, 28, 28, 1)

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




fashion_labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                  'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

y_pred_f = np.argmax(cnn.predict(X_test_f, verbose=0), axis=1)

# Confusion matrix
fig, ax = plt.subplots(figsize=(10, 8))
ConfusionMatrixDisplay(confusion_matrix(y_test_f, y_pred_f),
                       display_labels=fashion_labels).plot(ax=ax, xticks_rotation=45)
ax.set_title("Q7 — CNN Confusion Matrix")
plt.tight_layout()
plt.savefig("q7_confusion_matrix.png", dpi=150)
plt.show()

# Visualise 3 misclassified images
misclassified = np.where(y_pred_f != y_test_f)[0]
fig, axes = plt.subplots(1, 3, figsize=(9, 3))
for ax, idx in zip(axes, misclassified[:3]):
    ax.imshow(X_test_f[idx].reshape(28, 28), cmap='gray')
    ax.set_title(f"True: {fashion_labels[y_test_f[idx]]}\nPred: {fashion_labels[y_pred_f[idx]]}", fontsize=9)
    ax.axis('off')
plt.tight_layout()
plt.savefig("q7_misclassified.png", dpi=150)
plt.show()

#Pattern observed: the model most often confuses visually similar upper-body garments
#such as Shirt, T-shirt/top, and Pullover, which share similar silhouettes at 28x28 resolution.
#One method to improve performance: data augmentation (random flips, rotations)
#to expose the model to more varied views of each garment during training.