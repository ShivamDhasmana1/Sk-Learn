import pandas as pd
from data_preprocessing import cleaning
from model_training import train_and_evaluate

df = pd.read_csv("Data-Driven Student Performance Evaluation/student_ml_practice.csv")
X_train, X_test, y_train, y_test = cleaning(df)
prediction = train_and_evaluate(X_train, X_test, y_train, y_test)
