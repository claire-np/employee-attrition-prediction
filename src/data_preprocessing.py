import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic data cleaning:
    - Remove duplicates
    - Standardize column names
    - Handle missing values (simple strategy)
    """
    df = df.copy()

    # Standardize column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Drop duplicates
    df = df.drop_duplicates()

    # Simple missing value handling
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df
