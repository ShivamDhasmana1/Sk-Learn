from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_and_evaluate(X_train, X_test, y_train, y_test):
    model = LogisticRegression()
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_pred,y_test)
    if accuracy > 0:
        return model
    else:
        return "Model is not accurate"