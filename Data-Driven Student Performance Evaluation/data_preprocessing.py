import pandas as pd
from sklearn.preprocessing import StandardScaler , OrdinalEncoder
from sklearn.model_selection import train_test_split 

def cleaning(Dataframe):
        df = Dataframe.copy()

        # Step1 - Finding and filling missing values
        num_cols = df.select_dtypes(include="number").columns
        cat_cols = df.select_dtypes(include="object").columns
        df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
        df[cat_cols] = df[cat_cols].fillna("Unknown")

        #step2 - Encoding
        Encoded = OrdinalEncoder()
        target = df.columns[-1]
        cat_cols = cat_cols.drop(target)
        df[target] = Encoded.fit_transform(df[[target]])
        df[cat_cols] = Encoded.fit_transform(df[cat_cols])

        # Step3 - train test and split

        X = df.iloc[ :, :-1]  # All columns except last
        y = df.iloc[ :, -1]   # last column
        num_cols = X.select_dtypes(include="number").columns

        X_train , X_test , y_train , y_test = train_test_split( X, y, test_size=0.2, random_state=42)

        # step4 - scaling
        scaler = StandardScaler()
        X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
        X_test[num_cols]  = scaler.transform(X_test[num_cols])

        return X_train , X_test , y_train, y_test