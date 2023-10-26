# Destination Recommender (Content-based)

The Destination Recommender Application is a project aimed at providing personalized destination recommendations to users based on their preferences and interests. The goal is to enhance the travel planning experience by leveraging machine learning models and creating a user-friendly web application.

## Skills

- NLP
- Recommender systems
- ABSA
- Document clustering
- Web scraping
- Data Cleaning
- API development
- Data modelling/ storage

# Table of Contents

1. Code Structure
2. Tools & Packages
3. Data
4. ML Model Training
5. Results
6. API Development
7. Web Application Development
8. Future Development

# Code Structure

# Tools & Packages

## Frameworks

- Scikit-learn
- Pandas
- Numpy
- Gensim
- FastAPI
- MySQL Python connector
- Bootstrap

## Languages

- Python
- SQL
- HTML/CSS

# Data

Data of destinations were scraped from the web using APIFY's python client. The json data was then transform into three dataframes with: destination bio, destination metrics and destination reviews.
Missing data points in some dataframes were filled out with manual searches. The final dataframes were stored in a MySQL database in different tables.

# ML Model Training

## Feature Engineering

## Knowledge-based Recommender

## Content-based Recommender

# Results

# API Development

# Web Application

# Future Development

1. Complete web application features
2. Complete Integration of API with web application
3. Add knowledge-based recommender for application's zero state
4. Integrate ABSA model API
5. Add destinations for dates and fun experiences
6. Build collaborative-filtering recommender based on user profiles
