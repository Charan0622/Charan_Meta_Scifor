import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Change directory to where the data files are located
os.chdir('C:/Users/gchar/Scifor_Major_Project')

# Load training and testing data
train = pd.read_csv('C:/Users/gchar/Scifor_Major_Project/train.csv')
test = pd.read_csv('C:/Users/gchar/Scifor_Major_Project/test.csv')

# Map target variable
train.Loan_Status = train.Loan_Status.map({'Y': 1, 'N': 0})

# Check for missing values in training data
print(train.isnull().sum())

# Combine training and testing data for preprocessing
Loan_status = train.Loan_Status
train.drop('Loan_Status', axis=1, inplace=True)
Loan_ID = test.Loan_ID
data = pd.concat([train, test], ignore_index=True)


# Preprocess data
data.Gender = data.Gender.map({'Male': 1, 'Female': 0})
data.Married = data.Married.map({'Yes': 1, 'No': 0})
data.Dependents = data.Dependents.map({'0': 0, '1': 1, '2': 2, '3+': 3})
data.Education = data.Education.map({'Graduate': 1, 'Not Graduate': 0})
data.Self_Employed = data.Self_Employed.map({'Yes': 1, 'No': 0})
data.Property_Area = data.Property_Area.map({'Urban': 2, 'Semiurban': 1, 'Rural': 0})

# Fill missing values
data.Credit_History.fillna(np.random.randint(0, 2), inplace=True)
data.Married.fillna(np.random.randint(0, 2), inplace=True)
data.LoanAmount.fillna(data.LoanAmount.median(), inplace=True)
data.Loan_Amount_Term.fillna(data.Loan_Amount_Term.mean(), inplace=True)
data.Gender.fillna(np.random.randint(0, 2), inplace=True)
data.Dependents.fillna(data.Dependents.median(), inplace=True)
data.Self_Employed.fillna(np.random.randint(0, 2), inplace=True)

# Drop Loan_ID column
data.drop('Loan_ID', axis=1, inplace=True)

# Split data into features and target variable
train_X = data.iloc[:614, ]
train_y = Loan_status
train_X, test_X, train_y, test_y = train_test_split(train_X, train_y, random_state=0)

# Define models
models = [
    ("Logistic Regression", LogisticRegression()),
    ("Decision Tree", DecisionTreeClassifier()),
    ("Linear Discriminant Analysis", LinearDiscriminantAnalysis()),
    ("Random Forest", RandomForestClassifier()),
    ("Support Vector Classifier", SVC()),
    ("K-Nearest Neighbors", KNeighborsClassifier()),
    ("Naive Bayes", GaussianNB())
]

# Evaluate models
scoring = 'accuracy'
result = []
names = []
for name, model in models:
    kfold = KFold(n_splits=10, random_state=0, shuffle=True)
    cv_result = cross_val_score(model, train_X, train_y, cv=kfold, scoring=scoring)
    result.append(cv_result)
    names.append(name)
    print(f"{name}: {cv_result.mean():.6f}")
