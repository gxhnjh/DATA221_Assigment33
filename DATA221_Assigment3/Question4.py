import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

#Load data
kidney_data = pd.read_csv("kidney_disease.csv")
kidney_data.columns = kidney_data.columns.str.strip()

label_column = "classification"

#Split into X and y
raw_features = kidney_data.drop(columns=[label_column])
label_vector = kidney_data[label_column]

#Handle missing values
# Fill numeric columns with median
numeric_columns = raw_features.select_dtypes(include=["number"]).columns
raw_features[numeric_columns] = raw_features[numeric_columns].fillna(raw_features[numeric_columns].median())

# Fill the non numeric columns with the mode
categorical_columns = raw_features.select_dtypes(exclude=["number"]).columns
for col in categorical_columns:
    most_common_value = raw_features[col].mode(dropna=True)[0]
    raw_features[col] = raw_features[col].fillna(most_common_value)

#Convert categorical features to numeric
feature_matrix = pd.get_dummies(raw_features, drop_first=True)

#Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    feature_matrix,
    label_vector,
    test_size=0.30,
    random_state=42
)

#Train KNN (k=5)
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

#Our prediction
predicted_labels = knn_model.predict(X_test)

#Confusion matrix and metrics
conf_matrix = confusion_matrix(y_test, predicted_labels)

accuracy = accuracy_score(y_test, predicted_labels)
precision = precision_score(y_test, predicted_labels, pos_label="ckd")
recall = recall_score(y_test, predicted_labels, pos_label="ckd")
f1 = f1_score(y_test, predicted_labels, pos_label="ckd")

print("Confusion Matrix:")
print(conf_matrix)
print()
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

#Written explanations
# True Positive: the model predicts "ckd" and the patient truly has kidney disease.
# True Negative: the model predicts "notckd" and the patient truly does not have kidney disease.
# False Positive: the model predicts "ckd" but the patient is actually healthy.
# False Negative: the model predicts "notckd" but the patient actually has kidney disease.
#Accuracy alone may not be enough because a model can look good if one class is more common than the other.
# If missing a kidney disease case is very serious, recall is most important because it measures how many sick patients the model correctly identifies.

