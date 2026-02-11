import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
kidney_data = pd.read_csv("kidney_disease.csv")

# Clean column names (remove hidden spaces)
kidney_data.columns = kidney_data.columns.str.strip()

# Print column names ONCE (you can delete this line after confirming)
print("Columns:", list(kidney_data.columns))

# The label column in this dataset is called 'classification'
label_column = "classification"

# Create feature matrix X (all columns except label)
feature_matrix = kidney_data.drop(columns=[label_column])

# Create label vector y
label_vector = kidney_data[label_column]

# Split into training (70%) and testing (30%)
X_train, X_test, y_train, y_test = train_test_split(
    feature_matrix,
    label_vector,
    test_size=0.30,
    random_state=42
)

# Confirm shapes
print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)
print("Training labels:", y_train.shape)
print("Testing labels:", y_test.shape)

# ---- Written explanations (as comments) ----
# We should not train and test a model on the same data because the model could memorize
# the data instead of learning general patterns, which results in overfitting.
# The testing set is used to evaluate the model on unseen data and estimate
# how well it will perform in real-world situations.
