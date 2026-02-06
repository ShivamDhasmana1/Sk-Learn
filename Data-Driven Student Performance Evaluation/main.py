import pandas as pd
from data_preprocessing import cleaning
from model_training import train_and_evaluate

df = pd.read_csv("Data-Driven Student Performance Evaluation/student_ml_practice.csv")
X_train, X_test, y_train, y_test = cleaning(df)
model = train_and_evaluate(X_train, X_test, y_train, y_test)
new_student = pd.DataFrame({
    "Study_Hours": [float(input("Enter Hours Studied "))],
    "Attendance": [float(input("Enter Attendance "))],
    "Previous_Score": [float(input("Enter your previous score "))]
})
prediction = model.predict(new_student)

if prediction:
    print("Student is likely to Pass")
else:
    print("Student is likely to not Pass")