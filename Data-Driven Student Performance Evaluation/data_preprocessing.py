import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.model_selection import train_test_split

def cleaning(Dataframe):
    df = Dataframe.copy()
    # print(df.head(10))
    # print(df.info())

    num_cols = df.select_dtypes(include=['number']).columns
    cat_cols = df.select_dtypes(include=['object', 'string']).columns
    target = "Exam_Score"
    num_cols = num_cols.drop(target)

    # step 1- Filling missing values.
    df[cat_cols] = df[cat_cols].fillna("Unknown")

    # print(df.head())
    # print(df.isnull().sum())

    # step 2- encoding
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    # print(df.head())

    # Step 3- Splitting Data
    feature = df.drop(target, axis = 1)
    X = feature
    y = df[target]

    X_train , X_test , y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)

    # Step 4- Scaling Data
    scaler = StandardScaler()

    cols = X_train.columns

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    X_train = pd.DataFrame(X_train, columns=cols)
    X_test = pd.DataFrame(X_test, columns=cols)

    return X_train, X_test, y_train, y_test, scaler, X_train.columns