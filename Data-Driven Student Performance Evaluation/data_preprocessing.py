import pandas as pd
from sklearn.preprocessing import StandardScaler , OrdinalEncoder
from sklearn.model_selection import train_test_split 

def cleaning(Dataframe):
        df = Dataframe.copy()

        # Step1 - Finding and filling missing values
        num_cols = ["Study_Hours","Attendance","Previous_Score"]
        df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

        #step2 - Encoding
        Encoded = OrdinalEncoder()
        target = "Passed"
        df[[target]] = Encoded.fit_transform(df[[target]])

        # Step3 - train test and split
        X = df[num_cols]
        y = df[target]

        X_train , X_test , y_train , y_test = train_test_split( X, y, test_size=0.2, random_state=42)

        # step4 - scaling
        scaler = StandardScaler()
        X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
        X_test[num_cols]  = scaler.transform(X_test[num_cols])

        return X_train , X_test , y_train, y_test