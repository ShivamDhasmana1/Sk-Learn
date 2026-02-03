from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, confusion_matrix, accuracy_score, precision_score,recall_score

def train_and_evaluate(X_train, X_test, y_train, y_test):
    model = LogisticRegression()
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    print("Accuracy is: ",accuracy_score(y_test,y_pred))
    print("Precision is: ",precision_score(y_test,y_pred))
    print("f1 Score is: ",f1_score(y_test,y_pred))
    print("Recall is: ",recall_score(y_test,y_pred))
    print("confusion matrix is: \n",confusion_matrix(y_test,y_pred))

    return model