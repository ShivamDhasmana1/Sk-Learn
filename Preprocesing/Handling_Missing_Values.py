import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Raj", "Sneha", None],
    "Age": [22, 30, None, 28, 26],
    "City": ["Delhi", "Mumbai", "Delhi", None, "Chennai"]
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)
print("\nMissing Values: \n",df.isnull().sum())
print('\n Dropping missing values: ')
droped = df.dropna()
print(droped)

print("\nFilling missing values in age with mean values:")
df["Age"] = df['Age'].fillna(df['Age'].mean())
df['Name'] = df['Name'].fillna(df['Name'].mode()[0])
print(df)