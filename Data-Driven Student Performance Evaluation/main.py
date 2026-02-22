import pandas as pd
from Data_preprocessing import cleaning
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv(r"Data-Driven Student Performance Evaluation\StudentPerformanceFactors.csv")

X_train, X_test, y_train, y_test, scaler, cat_encoder = cleaning(df)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# print("MAE:", mean_absolute_error(y_test, y_pred))
# print("MSE:", mean_squared_error(y_test, y_pred))
# print("R2 Score:", r2_score(y_test, y_pred))

students = pd.DataFrame({
    'Hours_Studied': [10, 20, 30],
    'Attendance': [60, 80, 95],
    'Parental_Involvement': ['Low', 'Medium', 'High'],
    'Access_to_Resources': ['Low', 'Medium', 'High'],
    'Extracurricular_Activities': ['No', 'Yes', 'Yes'],
    'Sleep_Hours': [5, 6, 8],
    'Previous_Scores': [50, 65, 85],
    'Motivation_Level': ['Low', 'Medium', 'High'],
    'Internet_Access': ['No', 'Yes', 'Yes'],
    'Tutoring_Sessions': [0, 1, 3],
    'Family_Income': ['Low', 'Medium', 'High'],
    'Teacher_Quality': ['Low', 'Medium', 'High'],
    'School_Type': ['Public', 'Public', 'Private'],
    'Peer_Influence': ['Negative', 'Neutral', 'Positive'],
    'Physical_Activity': [2, 4, 6],
    'Learning_Disabilities': ['No', 'No', 'No'],
    'Parental_Education_Level': ['High School', 'College', 'Postgraduate'],
    'Distance_from_Home': ['Far', 'Moderate', 'Near'],
    'Gender': ['Male', 'Female', 'Male']
})
cat_cols = df.select_dtypes(include=['object', 'string']).columns
num_cols = df.select_dtypes(include=['number']).columns
students[cat_cols] = cat_encoder.transform(students[cat_cols])
students_scaled = scaler.transform(students)

new_student_prediction = model.predict(students)
print(f"Predicted Performance Score: {new_student_prediction[0]:.2f}")