import pandas as pd
import logging

def load_csv(filepath):
    """Load CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(filepath)
        logging.info(f"Loaded data from {filepath}")
        return df
    except FileNotFoundError:
        logging.error(f"File {filepath} not found.")
        return pd.DataFrame()
    except Exception as e:
        logging.error(f"Error loading {filepath}: {e}")
        return pd.DataFrame()