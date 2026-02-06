import pandas as pd
from sklearn.preprocessing import MinMaxScaler , OrdinalEncoder
from sklearn.model_selection import train_test_split 

# Step1 - Reading the CSV and making a dataset
df = pd.read_csv("Preprocessing\Sample.csv")
print(df)
# Step 2 - Finding the number of missing values in each column.
print(df.isnull().sum())
# Step 3 - Filling the missing values.
df.fillna({
    "City": "Unknown",
    "Study_Hours": df["Study_Hours"].median(),
    "Attendance": df["Attendance"].mean(),
    "Previous_Score" : df["Previous_Score"].mean()
}, inplace=True)

print(df)
print(df.isnull().sum())

# Step 4 - Encoding the Data.
df2 = df.copy()

df2["Passed"] = OrdinalEncoder().fit_transform(df2[["Passed"]])
print(df2)

num_cols = ["Study_Hours", "Attendance", "Previous_Score"]


# Step 6 - Train Test Split
X = df2[["Study_Hours","Attendance","Previous_Score"]]
y = df2["Passed"]   

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 7 - Scaling ONLY numeric columns
scaler = MinMaxScaler()

X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols]  = scaler.transform(X_test[num_cols])
