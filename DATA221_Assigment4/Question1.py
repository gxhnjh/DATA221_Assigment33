import numpy as np
from sklearn.datasets import load_breast_cancer

np.random.seed(42)



data = load_breast_cancer()

X = data.data
y = data.target

print(f"Shape of X (feature matrix): {X.shape}")
print(f"Shape of y (target vector):  {y.shape}")

unique, counts = np.unique(y, return_counts=True)
class_names = data.target_names
print("\nClass Distribution:")
for cls, cnt in zip(unique, counts):
    print(f"  Class {cls} ({class_names[cls]}): {cnt} samples")
#Is the dataset balanced or imbalanced?
#The dataset has 212 malignant and 357 benign samples.
# This is a mild imbalance (~37% malignant vs ~63% benign),
#but not much enough to require special resampling.

#Why is class balance important for classification models?
#When classes are heavily imbalanced, a model can achieve
#high accuracy simply by predicting the majority class for
#every sample. This makes accuracy a misleading metric.
#Balanced classes ensure the model learns meaningful
#patterns for both classes. When imbalance exists, metrics
#like precision, recall, F1-score, or AUC-ROC are more
#informative than accuracy alone.