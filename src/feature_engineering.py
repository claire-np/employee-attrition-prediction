import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add engineered features for HR Attrition dataset (Kaggle version)
    """
    df = df.copy()

    # 1. Average Hours per Project
    if "average_montly_hours" in df.columns and "number_project" in df.columns:
        df["hours_per_project"] = df["average_montly_hours"] / df["number_project"]

    # 2. Long Tenure Flag
    if "time_spend_company" in df.columns:
        df["long_tenure"] = (df["time_spend_company"] >= 4).astype(int)

    # 3. High evaluation
    if "last_evaluation" in df.columns:
        df["high_eval"] = (df["last_evaluation"] > 0.75).astype(int)

    # 4. Satisfaction level bucket
    if "satisfaction_level" in df.columns:
        df["satisfaction_bucket"] = pd.cut(
            df["satisfaction_level"],
            bins=[0, 0.3, 0.6, 1.0],
            labels=["low", "medium", "high"]
        )

    # One-hot encode categorical features
    df = pd.get_dummies(df, columns=["Department", "salary", "satisfaction_bucket"], drop_first=True)

    return df
