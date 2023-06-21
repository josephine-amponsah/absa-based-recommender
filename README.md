# Aspect-Based Destination Recommender

The Destination Recommender Application is a project aimed at providing personalized destination recommendations to users based on their preferences and interests. The goal is to enhance the travel planning experience by leveraging machine learning models and creating a user-friendly web application.

# Table of Contents

1. Introduction
2. Data Collection and Manipulation
3. Machine Learning Models
4. API Development
5. Web Application Development
6. Usage
7. Future Development
8. Conclusion

# Introduction

This serves as documentation for this data science project that involves data collection and manipulation, machine learning models, API development, and web application development. This document is aimed at providing a comprehensive guide on the various components involved, their functionalities, and how they interact with each other.

## Skills

- NLP
- Recommender systems
- ABSA
- Document clustering
- Web scraping
- Data Cleaning
- API development
- Data modelling/ storage

## Frameworks

- NLTK
- PyABSA
- Scikit-learn
- Pandas
- Numpy
- Gensim
- FastAPI
- MySQL Python connector

## Languages

- Python
- SQL
- HTML/CSS

# Data Collection & Manipulation

Data of destinations were scraped from the web using APIFY's python client. The json data was then transform into three dataframes with: destination bio, destination metrics and destination reviews.
Missing data points in some dataframes were filled out with manual searches. The final dataframes were stored in a MySQL database in different tables.

# Machine Learning Models

## Aspect-Based Sentiment Analysis (ABSA) model

An ABSA model was built on the reviews data. This was used to generate sentiments of customers on various experiences or aspects of experiences during their stay. This was built using the ATEPC model PyABSA library to generate aspects and sentiments.

## Aspect clustering with Word2Vec

The resulting aspects were many and needed to be categorized under specific labels for proper aggregation of sentiments. A Word2Vec model was trained on the reviews data, and the vectors of selected labels and the generated aspects were passed to cosine similarity function. the aspect were then replaced with labels they were closest to.

## Knowledge-based Recommender

To generate rankings based of specified labels, a knowledge based recommender algorithm was built. Depending on the selected the label, the output of the recommender ranks the column of interest and returns the highest rated based on the column's values.

## Content-based Recommender

# API Development

# Web Application

# Usage

# Future Development

1. Build ETL pipeline to update database
2. Build feature for users to save destination choices
3. Add destinations for dates and fun experiences
4. Build collaborative-filtering recommender based on user profiles
