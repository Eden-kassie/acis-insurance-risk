import pandas as pd

def load_insurance_data(file_path):
    """
    Load raw insurance dataset safely with error handling.
    """
    try:
        return pd.read_csv(file_path, sep="|", header=0, low_memory=False, encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ File not found: {file_path}")
    except Exception as e:
        raise RuntimeError(f"⚠️ Error loading data: {e}")
