from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    """
    Train Random Forest model with fixed params.
    """
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        class_weight='balanced',
        random_state=42
    )
    model.fit(X_train, y_train)
    return model
