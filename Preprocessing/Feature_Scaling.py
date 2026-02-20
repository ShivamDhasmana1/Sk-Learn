from sklearn.preprocessing import StandardScaler , MinMaxScaler
import pandas as pd
from sklearn.model_selection import train_test_split 

# Syntax of standardScaler and MinMaxScaler.

# scaler = StandardScaler() , MinMaxScaler()

# X_scaled = scaler.fit_transform()

# X_scaled = scaler.fit_transform()


df = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks":        [35, 40, 45, 55, 60, 65, 70, 78, 85, 92]
})

# Standard Scaler

Standard_Scaler = StandardScaler()
scaled = Standard_Scaler.fit_transform(df)
print("\n Standard Scaler \n")
print(pd.DataFrame(scaled , columns=["Hours_Studies" , "Marks"]))

# Formula for standard scaler
# Z = [(X-u)/SD]

# MinMax Scaler

Minmax = MinMaxScaler()
scale = Minmax.fit_transform(df)
print("\n MinMaxScaler\n")
print(pd.DataFrame(scale,columns=["Hours_Studies" , "Marks"] ))

# Formula for MinMaxScaler
# Z = [(X - X-min)/(X-max - X-min)]

# train_test_split 

X = df[["Hours_Studied"]]
y = df[["Marks"]]

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2, random_state=42)

print("\nX_Train\n")
print(X_train)
print("\ny_Train\n")
print(y_train)
print("\nX_test\n")
print(X_test)
print("\ny_test\n")
print(y_test)