from sklearn.metrics import accuracy_score, recall_score, classification_report

def evaluate_classification(model, X_test, y_test):
    """
    Prints evaluation metrics for a classifier.
    """
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    rec = recall_score(y_test, preds)

    print("Model Performance:")
    print(f"Accuracy: {acc:.4f}")
    print(f"Recall:   {rec:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, preds))
