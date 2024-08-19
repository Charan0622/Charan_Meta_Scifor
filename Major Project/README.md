# Loan Prediction Application 🏦

Welcome to the Loan Prediction Application! This project leverages machine learning models to predict the likelihood of a loan being approved based on various applicant details.

## Table of Contents 📚
- [Introduction](#introduction-📖)
- [Technologies Used](#technologies-used-🛠️)
- [Project Structure](#project-structure-📁)
- [Setup Instructions](#setup-instructions-⚙️)

## Introduction 📖

This application provides a user-friendly interface for loan prediction. By inputting specific details about the loan applicant, the model predicts whether the loan will be approved.

## Technologies Used 🛠️

- **Python** 🐍
- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Scikit-learn** for machine learning
- **Matplotlib** and **Seaborn** for data visualization
- **Streamlit** for building the web application
- **Pickle** for model serialization

## Project Structure 📁

```
Loan_Prediction/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│
├── models/
│   ├── ML_Model.pkl
│
├── app/
│   ├── app.py
│
├── src/
│   ├── loan_prediction_model.py
│
├── README.md
│
└── requirements.txt
```

- `data/`: Contains the training and testing datasets.
- `models/`: Contains the serialized machine learning model.
- `app/`: Contains the main application code.
- `src/`: Contains the model training and preprocessing code.
- `README.md`: This file.
- `requirements.txt`: Lists the Python dependencies.

## Setup Instructions ⚙️

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/Loan_Prediction.git
   cd Loan_Prediction
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Change directory to the project folder**:

   ```bash
   cd app
   ```

5. **Run the application**:

   ```bash
   streamlit run app.py
   ```

