import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.model_selection import train_test_split


def cleaning(dataframe):
        df = dataframe.copy()
        
        # Remove irrelevant columns
        df = df.drop(["Student_ID", "Gender", "Parental_Education_Level"], axis=1)
        
        # Encode categorical variables
        target_encoder = OrdinalEncoder()
        feature_encoder = OrdinalEncoder()
        
        target = "Passed"
        df[[target]] = target_encoder.fit_transform(df[[target]])
        
        categorical_cols = [
                "Internet_Access_at_Home",
                "Extracurricular_Activities"
        ]
        df[categorical_cols] = feature_encoder.fit_transform(df[categorical_cols])
        
        # Split features and target
        features = [
                "Study_Hours_per_Week",
                "Attendance_Rate",
                "Past_Exam_Scores",
                "Final_Exam_Score",
                "Internet_Access_at_Home",
                "Extracurricular_Activities"
        ]
        X = df[features]
        y = df[target]
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale features
        scaler = StandardScaler()
        X_train[features] = scaler.fit_transform(X_train[features])
        X_test[features] = scaler.transform(X_test[features])
        
        return X_train, X_test, y_train, y_test, scaler, feature_encoder