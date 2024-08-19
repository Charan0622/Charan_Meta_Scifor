import streamlit as st
import pickle
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

# Load the model
model = pickle.load(open('Major Project/Loan Prediction/ML_Model.pkl', 'rb'))

def run():
    st.set_page_config(page_title="Loan Prediction", page_icon="🏦", layout="wide")

    # Sidebar for specific inputs
    st.sidebar.title("Loan Application Form 📋")

    # Sidebar fields
    account_no = st.sidebar.text_input('Account Number 📑', placeholder='Enter your account number')
    fn = st.sidebar.text_input('Full Name 👤', placeholder='Enter your full name')

    # Gender
    gen_display = ('Female 👩', 'Male 👨')
    gen_options = list(range(len(gen_display)))
    gen = st.sidebar.selectbox("Gender 🌟", gen_options, format_func=lambda x: gen_display[x])

    # Marital Status
    mar_display = ('No 💔', 'Yes 💍')
    mar_options = list(range(len(mar_display)))
    mar = st.sidebar.selectbox("Marital Status 💑", mar_options, format_func=lambda x: mar_display[x])

    # Number of Dependents
    dep_display = ('No 👶', 'One 👶', 'Two 👶👶', 'More than Two 👨‍👩‍👧‍👦')
    dep_options = list(range(len(dep_display)))
    dep = st.sidebar.selectbox("Dependents 👨‍👩‍👧", dep_options, format_func=lambda x: dep_display[x])

    # Main panel for remaining inputs and results
    st.title("Loan Prediction Form 🏦")

    # Remaining inputs
    edu_display = ('Not Graduate 🎓', 'Graduate 🎓')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education 🎓", edu_options, format_func=lambda x: edu_display[x])

    emp_display = ('Job 💼', 'Business 🏢')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status 💼", emp_options, format_func=lambda x: emp_display[x])

    prop_display = ('Rural 🌾', 'Semi-Urban 🌇', 'Urban 🏙️')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area 🏡", prop_options, format_func=lambda x: prop_display[x])

    cred_display = ('Between 300 to 500 📉', 'Above 500 📈')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score 💳", cred_options, format_func=lambda x: cred_display[x])

    mon_income = st.number_input("Applicant's Monthly Income 💵", value=0)
    co_mon_income = st.number_input("Co-Applicant's Monthly Income 💴", value=0)
    loan_amt = st.number_input("Loan Amount 💰", value=0)

    dur_display = ['2 Months ⏳', '6 Months 🕑', '8 Months 🕑', '1 Year 🗓️', '16 Months 🗓️']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration ⏱️", dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit 📝"):
        duration = [60, 180, 240, 360, 480][dur]
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))

        if ans == 0:
            st.error(
                f"Hello {fn}! 👋\n"
                f"Account Number: {account_no} 🔢\n"
                f"According to our calculations, you will not get the loan from the bank. 🚫"
            )
        else:
            st.success(
                f"Hello {fn}! 🎉\n"
                f"Account Number: {account_no} 🔢\n"
                f"Congratulations!! You will get the loan from the bank. ✅"
            )

run()

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
