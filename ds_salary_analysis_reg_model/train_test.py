import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# Load data (fix index issue)
X_train = pd.read_csv('X_train.csv', index_col=0)
y_train = pd.read_csv('y_train.csv', index_col=0).squeeze()
X_test = pd.read_csv('X_test.csv', index_col=0)

# Strip spaces from column names
X_train.columns = X_train.columns.str.strip()
X_test.columns = X_test.columns.str.strip()

# Print to verify column names
print("Columns in X_train:", X_train.columns)
print("Columns in X_test:", X_test.columns)

# Define feature groups correctly
num_features = []  # No numerical features, as experience_level is categorical
cat_features = ['experience_level', 'employment_type', 'job_title', 'company_location', 'company_size']  # Added experience_level

# Ensure all features exist in X_train
missing_features = set(cat_features) - set(X_train.columns)
if missing_features:
    raise ValueError(f"Missing columns in X_train: {missing_features}")

# Define preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)  # Encode all categorical features
    ]
)

# Create pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Fit the model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Save predictions
y_pred_df = pd.DataFrame(y_pred, columns=['Predicted Salary'])
y_pred_df.to_csv('y_pred.csv', index=False)

print("Predictions saved to y_pred.csv")
