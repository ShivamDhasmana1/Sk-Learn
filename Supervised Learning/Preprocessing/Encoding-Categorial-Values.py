from sklearn.preprocessing import LabelEncoder 
import pandas as pd

df = pd.read_csv("Sample.csv")
df_Label = df.copy()
# Label Encoding
Le = LabelEncoder()
print("\n Label Encoded Data: ")
df_Label["Passed_encoded"] = Le.fit_transform(df_Label["Passed"])
df_Label["Gender_encoded"] = Le.fit_transform(df_Label["Gender"])
df_Label["Name_encoded"] = Le.fit_transform(df_Label["Name"])
print(df_Label[["Name","Name_encoded","Class", "Gender","Gender_encoded","Passed","Passed_encoded"]].head(5))

# One-Hot Encoding

df_new = pd.get_dummies(df , columns=["Class"])
col = ["Class_8","Class_9" , "Class_10" , "Class_11" , "Class_12"]
df_new[col] = df_new[col].replace({True:1,False:0})
print(df_new.head(5))