# src/analysis/sentiment_analysis.py

import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline
from dotenv import load_dotenv
import logging
from src.utils.logger import setup_logger
from src.utils.data_loader import load_csv

# Setup logger
logger = setup_logger('sentiment_analysis_logger', 'logs/sentiment_analysis.log')

# Load environment variables
load_dotenv()

DATA_DIR = os.getenv('DATA_DIR', './data/processed')
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, 'processed_comments.csv')
SENTIMENT_DATA_PATH = os.path.join(DATA_DIR, 'comments_with_sentiment.csv')

# Initialize sentiment analyzers
vader_analyzer = SentimentIntensityAnalyzer()
textblob_analyzer = TextBlob
transformer_sentiment_pipeline = pipeline("sentiment-analysis")

def get_vader_sentiment(text):
    """Compute sentiment using VADER."""
    scores = vader_analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        return 'Positive'
    elif compound <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def get_textblob_sentiment(text):
    """Compute sentiment using TextBlob."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def get_transformer_sentiment(text):
    """Compute sentiment using a transformer-based model."""
    try:
        result = transformer_sentiment_pipeline(text[:512])[0]  # Truncate if necessary
        label = result['label']
        score = result['score']
        return label, score
    except Exception as e:
        logger.error(f"Transformer sentiment analysis failed for text: {text[:50]}... Error: {e}")
        return 'Neutral', 0.0

def perform_sentiment_analysis(df):
    """Add sentiment analysis results to the DataFrame."""
    # VADER Sentiment
    logger.info("Starting VADER sentiment analysis.")
    df['sentiment_vader'] = df['cleaned_comment'].apply(get_vader_sentiment)
    
    # TextBlob Sentiment
    logger.info("Starting TextBlob sentiment analysis.")
    df['sentiment_textblob'] = df['cleaned_comment'].apply(get_textblob_sentiment)
    
    # Transformer-based Sentiment
    logger.info("Starting Transformer-based sentiment analysis.")
    transformer_results = df['cleaned_comment'].apply(get_transformer_sentiment)
    df[['sentiment_transformer', 'transformer_score']] = pd.DataFrame(transformer_results.tolist(), index=df.index)
    
    logger.info("Completed sentiment analysis.")
    return df

def save_sentiment_data(df, filepath):
    """Save DataFrame with sentiment analysis to CSV."""
    try:
        df.to_csv(filepath, index=False)
        logger.info(f"Sentiment analysis results saved to {filepath}")
    except Exception as e:
        logger.error(f"Error saving sentiment data: {e}")

def main():
    """Main function to perform sentiment analysis."""
    # Load processed data
    df = load_csv(PROCESSED_DATA_PATH)
    
    if df.empty:
        logger.warning("No data available for sentiment analysis.")
        return
    
    # Perform sentiment analysis
    df = perform_sentiment_analysis(df)
    
    # Save results
    save_sentiment_data(df, SENTIMENT_DATA_PATH)

if __name__ == "__main__":
    main()
