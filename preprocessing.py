# preprocessing.py

import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
from dotenv import load_dotenv
import emoji  # Import the emoji library

# Load environment variables from .env
load_dotenv()

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Initialize spaCy English model
try:
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
except OSError:
    # If the model is not present, download it
    from spacy.cli import download
    download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

# Define file paths
DATA_DIR = os.getenv('DATA_DIR', 'data')
COMMENT_COLUMN = os.getenv('COMMENT_COLUMN', 'comment')  # Set default to lowercase
RAW_DATA_PATH = os.path.join(DATA_DIR, 'comments.csv')
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, 'processed_comments.csv')

def load_data(filepath):
    """
    Load comments data from a CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        df.columns = df.columns.str.strip().str.lower()  # Normalize column names to lowercase
        print(f"Loaded {df.shape[0]} comments from {filepath}")
        print("Columns in the CSV file:", df.columns.tolist())  # Debugging line
        return df
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"File {filepath} is empty.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return pd.DataFrame()

def handle_missing_values(df, column='comment'):
    """
    Drop rows with missing values in the specified column.
    """
    initial_count = df.shape[0]
    df = df.dropna(subset=[column])
    final_count = df.shape[0]
    print(f"Dropped {initial_count - final_count} rows with missing '{column}'")
    return df

def demojize_text(text):
    """
    Convert emojis in the text to their descriptive text.
    Example: "I love this! 😊" -> "I love this! :smiling_face_with_smiling_eyes:"
    """
    return emoji.demojize(text, delimiters=(" ", " "))

def clean_text(text):
    """
    Clean the input text by removing URLs, HTML tags, non-alphabetic characters,
    converting to lowercase, and stripping extra spaces.
    """
    # Remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove non-alphabetic characters except colons and underscores (to keep demojized emojis)
    text = re.sub(r'[^a-zA-Z\s:_]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize_text(text):
    """
    Tokenize the input text into words.
    """
    return word_tokenize(text)

def remove_stopwords(tokens):
    """
    Remove English stop words from the list of tokens.
    """
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

def lemmatize_tokens(tokens):
    """
    Lemmatize the list of tokens using spaCy.
    """
    doc = nlp(' '.join(tokens))
    lemmatized = [token.lemma_ for token in doc]
    return lemmatized

def preprocess_comments(df):
    """
    Perform preprocessing on the comments DataFrame.
    """
    # Handle missing values
    df = handle_missing_values(df, column=COMMENT_COLUMN)
    
    # Convert emojis to text
    df['demojized_comment'] = df[COMMENT_COLUMN].apply(demojize_text)
    
    # Clean text
    df['cleaned_comment'] = df['demojized_comment'].apply(clean_text)
    
    # Tokenization
    df['tokens'] = df['cleaned_comment'].apply(tokenize_text)
    
    # Remove stop words
    df['filtered_tokens'] = df['tokens'].apply(remove_stopwords)
    
    # Lemmatization
    df['lemmatized_tokens'] = df['filtered_tokens'].apply(lemmatize_tokens)
    
    return df

def save_processed_data(df, filepath):
    """
    Save the processed DataFrame to a CSV file.
    """
    # Select relevant columns to save
    processed_df = df[['serial number', 'comment', 'demojized_comment', 'cleaned_comment', 'lemmatized_tokens']]
    
    # Save to CSV
    processed_df.to_csv(filepath, index=False)
    print(f"Processed data saved to {filepath}")

def main():
    """
    Main function to execute preprocessing steps.
    """
    # Ensure the data directory exists
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"Created data directory at {DATA_DIR}")
    
    # Load raw data
    df = load_data(RAW_DATA_PATH)
    
    if df.empty:
        print("No data to process.")
        return
    
    # Preprocess comments
    df = preprocess_comments(df)
    
    # Save processed data
    save_processed_data(df, PROCESSED_DATA_PATH)

if __name__ == "__main__":
    main()
