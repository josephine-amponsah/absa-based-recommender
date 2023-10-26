# Aspect Sentiment Generator

This sub-project is aimed at building a model that generates sentiments of reviews under subjects/categories related to a service. In this case, the service of interest is one provided by hotels or resorts in Ghana to tourists /customers.

## Skills

- Text Data Processing
- Word Embedding
- NLP
- Aspect-Based Sentiment Analysis
- Document clustering

# Table of Contents

1. Code Structure
2. Tools & Packages
3. Data
4. ML Model Training & Evaluation
5. Results
6. Future Development

# Code Structure

# Tools & Packages

## Frameworks

- NLTK
- PyABSA
- Pandas
- Gensim
- FastAPI

## Languages

- Python

# Data

## Data collection

Data of destinations were scraped from the web using APIFY's python client. The json data was then transform into three dataframes with: destination bio, destination metrics and destination reviews.

## Data cleaning

## Data modeling

# ML Model Training & Evaluation

## Feature engineering

## ABSA model training

An ABSA model was built on the reviews data. This was used to generate sentiments of customers on various experiences or aspects of experiences during their stay. This was built using the ATEPC model PyABSA library to generate aspects and sentiments.

## Aspect clustering with Word2Vec

The resulting aspects were many and needed to be categorized under specific labels for proper aggregation of sentiments. A Word2Vec model was trained on the reviews data, and the vectors of selected labels and the generated aspects were passed to cosine similarity function. the aspect were then replaced with labels they were closest to.

# Results

# Future Development

1. Replace model with ABSAIntruction (Category-Aspect Sentiment Generator)
2. Build API for model deployment to applications
3. Build API documentation
