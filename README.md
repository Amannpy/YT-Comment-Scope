# YT-Comment-Scope

YT-Comment-Scope is a YouTube comments analysis dashboard that provides in-depth insights into the sentiments, keywords, and topics derived from YouTube video comments. Built with Python and Streamlit, this project features data preprocessing, visualization, and analysis modules to help you explore trends and patterns in YouTube data.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Modules Overview](#modules-overview)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Sentiment Analysis:**  
  Explore sentiment distributions using multiple analysis techniques (VADER, TextBlob, Transformer).  
  - **Sentiment Distribution (VADER):**  
    ![Sentiment Distribution VADER](data/visualizations/sentiment_distribution_vader.png)
  - **Sentiment Distribution (TextBlob):**  
    ![Sentiment Distribution TextBlob](data/visualizations/sentiment_distribution_textblob.png)
  - **Sentiment Distribution (Transformer):**  
    ![Sentiment Distribution Transformer](data/visualizations/sentiment_distribution_transformer.png)

- **Keyword Analysis:**  
  Extract and compare keywords using RAKE, YAKE, TF-IDF, and combined methods with visualizations including word clouds and bar charts.  
  - **Bar Comparative Top Keywords:**  
    ![Bar Comparative Top Keywords](data/visualizations/bar_comparative_top_keywords.png)
  - **Bar Top Keywords (RAKE):**  
    ![Bar Top Keywords RAKE](data/visualizations/bar_top_keywords_rake_keywords.png)
  - **Bar Top Keywords (TF-IDF):**  
    ![Bar Top Keywords TF-IDF](data/visualizations/bar_top_keywords_tfidf_keywords.png)
  - **Bar Top Keywords (YAKE):**  
    ![Bar Top Keywords YAKE](data/visualizations/bar_top_keywords_yake_keywords.png)
  - **Heatmap Keyword Frequency:**  
    ![Heatmap Keyword Frequency](data/visualizations/heatmap_keyword_frequency.png)
  - **Venn Diagram for Keyword Extraction Methods:**  
    ![Venn Diagram Keyword Methods](data/visualizations/venn_keyword_methods.png)

- **Topic Analysis:**  
  Visualize the top words for each topic discovered in the comment data.
  - **Topic 1 Top Words:**  
    ![Topic 1 Top Words](data/visualizations/topic_1_top_words.png)
  - **Topic 2 Top Words:**  
    ![Topic 2 Top Words](data/visualizations/topic_2_top_words.png)
  - **Topic 3 Top Words:**  
    ![Topic 3 Top Words](data/visualizations/topic_3_top_words.png)
  - **Topic 4 Top Words:**  
    ![Topic 4 Top Words](data/visualizations/topic_4_top_words.png)
  - **Topic 5 Top Words:**  
    ![Topic 5 Top Words](data/visualizations/topic_5_top_words.png)

- **Word Cloud Visualizations:**  
  See an overall view and sentiment-specific word clouds.
  - **Word Cloud All Comments:**  
    ![Word Cloud All Comments](data/visualizations/wordcloud_all_comments.png)
  - **Word Cloud Combined Methods:**  
    ![Word Cloud Combined Methods](data/visualizations/wordcloud_combined_methods.png)
  - **Word Cloud Keywords (RAKE):**  
    ![Word Cloud Keywords RAKE](data/visualizations/wordcloud_keywords_rake.png)
  - **Word Cloud Keywords (TF-IDF):**  
    ![Word Cloud Keywords TF-IDF](data/visualizations/wordcloud_keywords_tfidf.png)
  - **Word Cloud Keywords (YAKE):**  
    ![Word Cloud Keywords YAKE](data/visualizations/wordcloud_keywords_yake.png)
  - **Word Cloud Negative Comments:**  
    ![Word Cloud Negative Comments](data/visualizations/wordcloud_negative_comments.png)
  - **Word Cloud Neutral Comments:**  
    ![Word Cloud Neutral Comments](data/visualizations/wordcloud_neutral_comments.png)
  - **Word Cloud Positive Comments:**  
    ![Word Cloud Positive Comments](data/visualizations/wordcloud_positive_comments.png)

- **Interactive Dashboard:**  
  A Streamlit-based web app provides a user-friendly interface for navigating all these analyses and visualizations.

## Project Structure

```plaintext
YT-Comment-Scope/
├── data/
│   ├── raw/
│   │   └── comments.csv                # Raw YouTube comments data
│   ├── processed/
│   │   ├── processed_comments.csv      # Processed version of the raw comments
│   │   ├── comments_with_sentiments.csv# Comments with computed sentiments
│   ├── visualizations/                 # Visualization assets (charts, word clouds, etc.)
│   │   ├── bar_comparative_top_keywords.png
│   │   ├── bar_top_keywords_rake_keywords.png
│   │   ├── bar_top_keywords_tfidf_keywords.png
│   │   ├── bar_top_keywords_yake_keywords.png
│   │   ├── heatmap_keyword_frequency.png
│   │   ├── sentiment_distribution_textblob.png
│   │   ├── sentiment_distribution_transformer.png
│   │   ├── sentiment_distribution_vader.png
│   │   ├── topic_1_top_words.png
│   │   ├── topic_2_top_words.png
│   │   ├── topic_3_top_words.png
│   │   ├── topic_4_top_words.png
│   │   ├── topic_5_top_words.png
│   │   ├── venn_keyword_methods.png
│   │   ├── wordcloud_all_comments.png
│   │   ├── wordcloud_combined_methods.png
│   │   ├── wordcloud_keywords_rake.png
│   │   ├── wordcloud_keywords_tfidf.png
│   │   ├── wordcloud_keywords_yake.png
│   │   ├── wordcloud_negative_comments.png
│   │   ├── wordcloud_neutral_comments.png
│   │   └── wordcloud_positive_comments.png
│   └── README.md                       # Optional data documentation
├── log/
│   ├── keywords_extraction.log         # Logs for keyword extraction process
│   ├── sentiment_analysis.log          # Logs for sentiment analysis process
│   └── topic_modelling.log             # Logs for topic modelling process
├── notebooks/
│   └── 01_Data_Exploration.ipynb       # Jupyter Notebook for initial data exploration
├── src/
│   ├── __pycache__/                    # Compiled Python files
│   ├── preprocessing.py                # Data preprocessing scripts
│   ├── scrapper.py                     # Data scraping scripts
│   ├── __init__.py
│   ├── utils/                          # Utility functions and helper modules
│   │   ├── __init__.py
│   │   ├── data_loader.py              # Module to load and manage data
│   │   └── logger.py                   # Custom logging utilities
│   └── analysis/                       # Analysis and visualization modules
│       ├── __init__.py
│       ├── app.py                      # Streamlit dashboard application
│       ├── keywords_extraction.py      # Keyword extraction routines
│       ├── sentiment_analysis.py       # Sentiment analysis routines
│       ├── topic_modelling.py          # Topic modelling routines
│       └── visualization.py            # Functions for creating visualizations
├── venv/                               # Python virtual environment
├── .env                                # Environment variables file
├── .gitignore                          # Git ignore file
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
