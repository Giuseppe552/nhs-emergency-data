import pandas as pd

def load_and_clean(filepath):
    df = pd.read_excel(filepath, skiprows=13)

    df.dropna(axis=1, how='all', inplace=True)
    df.dropna(axis=0, how='all', inplace=True)

    # Show raw column names (before renaming)
    print("ORIGINAL COLUMNS:", df.columns.tolist())

    # Normalize column names
    df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]

    # Show processed column names
    print("CLEANED COLUMNS:", df.columns.tolist())

    return df
