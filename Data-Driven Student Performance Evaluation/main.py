import pandas as pd
from Data_preprocessing import cleaning
from sklearn.linear_model import LinearRegression
from Students_data import students
from sklearn.metrics import  mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv(r"Data-Driven Student Performance Evaluation\StudentPerformanceFactors.csv")

X_train, X_test, y_train, y_test, scaler, train_cols = cleaning(df)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# print("MAE:", mean_absolute_error(y_test, y_pred))
# print("MSE:", mean_squared_error(y_test, y_pred))
# print("R2 Score:", r2_score(y_test, y_pred))
students = students()

cat_cols = students.select_dtypes(include=['object', 'string']).columns

num_cols = students.select_dtypes(include=['number']).columns

students = pd.get_dummies(students, columns=cat_cols, drop_first=True)

students = students.reindex(columns=train_cols, fill_value=0)

students_scaled = scaler.transform(students)

new_student_prediction = model.predict(students_scaled)
print(f"Predicted Performance Score: {new_student_prediction}")