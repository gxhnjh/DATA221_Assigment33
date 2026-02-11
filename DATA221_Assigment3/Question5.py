import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# ---------------- Load + prepare data (same as Q4) ----------------
kidney_data = pd.read_csv("kidney_disease.csv")
kidney_data.columns = kidney_data.columns.str.strip()

label_column = "classification"

raw_features = kidney_data.drop(columns=[label_column])
label_vector = kidney_data[label_column]

# Fill missing values
numeric_columns = raw_features.select_dtypes(include=["number"]).columns
raw_features[numeric_columns] = raw_features[numeric_columns].fillna(raw_features[numeric_columns].median())

categorical_columns = raw_features.select_dtypes(exclude=["number"]).columns
for col in categorical_columns:
    most_common_value = raw_features[col].mode(dropna=True)[0]
    raw_features[col] = raw_features[col].fillna(most_common_value)

# One-hot encode categorical features so KNN can use them
feature_matrix = pd.get_dummies(raw_features, drop_first=True)

# Train/test split (same as Q3/Q4)
X_train, X_test, y_train, y_test = train_test_split(
    feature_matrix,
    label_vector,
    test_size=0.30,
    random_state=42
)

# ---------------- Train multiple KNN models with different k ----------------
k_values = [1, 3, 5, 7, 9]
accuracy_results = []

for k in k_values:
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train, y_train)
    predicted_labels = knn_model.predict(X_test)

    test_accuracy = accuracy_score(y_test, predicted_labels)
    accuracy_results.append({"k": k, "accuracy": test_accuracy})

# Create a small table showing k and accuracy
results_table = pd.DataFrame(accuracy_results)
print("KNN Test Accuracy Results:")
print(results_table.to_string(index=False))

# Identify which k gives the highest test accuracy
best_row = results_table.loc[results_table["accuracy"].idxmax()]
best_k = int(best_row["k"])
best_accuracy = float(best_row["accuracy"])

print("\nBest k:", best_k)
print("Highest test accuracy:", best_accuracy)

# ---- Written explanations (3–5 sentences total) ----
# Changing k changes how smooth vs sensitive the decision boundary is: small k reacts strongly to nearby points, larger k averages more neighbors.
# Very small k (like 1) may overfit because the model can “memorize” noise and outliers in the training data.
# Very large k may underfit because predictions become too averaged and the model may miss real patterns in the data.
# We choose k based on test performance because we want the best generalization to unseen data, not just the training set.
