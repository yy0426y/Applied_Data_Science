import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import warnings
warnings.filterwarnings("ignore")  # Ignore some warnings for cleaner output

# 1. Data Preparation
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Convert to DataFrame for easier handling (optional but useful for visualization)
X_df = pd.DataFrame(X, columns=iris.feature_names)
y_df = pd.Series(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features (important for some algorithms like SVM and Logistic Regression)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. Model Selection
# Choose different classification algorithms as candidates
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Support Vector Machine": SVC()
}

# 3. Model Training and Initial Evaluation
results = {}
for model_name, model in models.items():
    # Train the model
    model.fit(X_train, y_train)
    # Make predictions on the training set
    y_train_pred = model.predict(X_train)
    # Calculate performance metrics on the training set
    train_accuracy = accuracy_score(y_train, y_train_pred)
    train_precision = precision_score(y_train, y_train_pred, average='weighted')
    train_recall = recall_score(y_train, y_train_pred, average='weighted')
    train_f1 = f1_score(y_train, y_train_pred, average='weighted')

    # Store the results
    results[model_name] = {
        "train_accuracy": train_accuracy,
        "train_precision": train_precision,
        "train_recall": train_recall,
        "train_f1": train_f1
    }

# 4. Hyperparameter Tuning
tuned_models = {}
param_grid = {
    "Logistic Regression": {
        "C": [0.001, 0.01, 0.1, 1, 10, 100]
    },
    "Decision Tree": {
        "max_depth": [3, 5, 7, 10],
        "min_samples_split": [2, 5, 10]
    },
    "Random Forest": {
        "n_estimators": [50, 100, 200],
        "max_depth": [3, 5, 7, 10]
    },
    "Support Vector Machine": {
        "C": [0.1, 1, 10],
        "kernel": ["linear", "rbf", "poly"]
    }
}

for model_name, model in models.items():
    grid_search = GridSearchCV(model, param_grid[model_name], cv=5)
    grid_search.fit(X_train, y_train)
    tuned_models[model_name] = grid_search.best_estimator_

# 5. Re-evaluate Tuned Models on Validation (using cross-validation on training set)
tuned_results = {}
for model_name, tuned_model in tuned_models.items():
    cv_scores = cross_val_score(tuned_model, X_train, y_train, cv=5)
    tuned_results[model_name] = {
        "cv_mean_accuracy": np.mean(cv_scores),
        "cv_std_accuracy": np.std(cv_scores)
    }

# 6. Final Evaluation on Test Set
test_results = {}
for model_name, tuned_model in tuned_models.items():
    y_test_pred = tuned_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    test_precision = precision_score(y_test, y_test_pred, average='weighted')
    test_recall = recall_score(y_test, y_test_pred, average='weighted')
    test_f1 = f1_score(y_test, y_test_pred, average='weighted')
    test_confusion_matrix = confusion_matrix(y_test, y_test_pred)

    test_results[model_name] = {
        "test_accuracy": test_accuracy,
        "test_precision": test_precision,
        "test_recall": test_recall,
        "test_f1": test_f1,
        "test_confusion_matrix": test_confusion_matrix
    }

# 7. Selecting the Best Model
best_model_name = max(test_results, key=lambda x: test_results[x]["test_accuracy"])
print(f"The best performing model is {best_model_name} with an accuracy of {test_results[best_model_name]['test_accuracy']}")