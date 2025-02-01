# YT-Comment-Scope

YT-Comment-Scope is a YouTube comments analysis dashboard that provides in-depth insights into the sentiments, keywords, and topics derived from YouTube video comments. Built with Python and Streamlit, this project features data preprocessing, visualization, and analysis modules to help you explore trends and patterns in YouTube data.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Modules Overview](#modules-overview)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Sentiment Analysis:**  
  Explore sentiment distributions using multiple analysis techniques (VADER, TextBlob, Transformer).
  - **Sentiment Distribution (VADER):**

  ![Sentiment Distribution VADER](./data/processed/visualizations/sentiment_distribution_vader.png)

- **Sentiment Distribution (TextBlob):**

  ![Sentiment Distribution TextBlob](data/processed/visualizations/sentiment_distribution_textblob.png)

- **Sentiment Distribution (Transformer):**

  ![Sentiment Distribution Transformer](data/processed/visualizations/sentiment_distribution_transformer.png)


- **Keyword Analysis:**  
  Extract and compare keywords using RAKE, YAKE, TF-IDF, and combined methods with visualizations including word clouds and bar charts.

- **Advanced Visualizations:**  
  View interactive and static visualizations such as heatmaps, Venn diagrams, bubble charts, box plots, and network graphs.

- **Interactive Dashboard:**  
  A Streamlit-based web app that offers a user-friendly interface to navigate through different analytical sections.

## Project Structure

The repository is organized as follows:

```plaintext
YT-Comment-Scope/
├── data/
│   ├── raw/
│   │   └── comments.csv                # Raw YouTube comments data
│   ├── processed/
│   │   ├── processed_comments.csv      # Processed version of the raw comments
│   │   ├── comments_with_sentiments.csv# Comments with computed sentiments
│   │   └── visualization/              # Visualization assets (charts, wordclouds, etc.)
│   └── README.md                       # Data folder documentation (optional)
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
├── .gitignore                          # Git ignore file to exclude unnecessary files/folders
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
