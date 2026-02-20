import pandas as pd
from data_preprocessing import cleaning
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("Data-Driven Student Performance Evaluation/student_ml_practice.csv")
X_train, X_test, y_train, y_test, scaler, encoder = cleaning(df)

model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

# print("Classification Report: ")
# print(classification_report(y_test,y_pred))


new_student = pd.DataFrame({
                "Study_Hours_per_Week": [float(input("Enter Study Hours per Week "))],
                "Attendance_Rate": [float(input("Enter Attendance Rate "))],
                "Past_Exam_Scores" : [float(input("Enter Past Exam Scores "))],
                "Final_Exam_Score":[float(input("Enter Final Exam Score "))],
                "Internet_Access_at_Home": [input("Enter Internet Access at Home ").capitalize()],
                "Extracurricular_Activities" :[input("Enter Extracurricular Activities ").capitalize()]
})
new_student[["Internet_Access_at_Home", "Extracurricular_Activities"]] = encoder.transform(new_student[["Internet_Access_at_Home", "Extracurricular_Activities"]])
scaled_new_student = pd.DataFrame(scaler.transform(new_student), columns=new_student.columns)
prediction = model.predict(scaled_new_student)[0]
if prediction:
    print("Student is likely to Pass")
else:
    print("Student is likely to not Pass")
