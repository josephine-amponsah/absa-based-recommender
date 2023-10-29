# Destination Recommender (Content-based)

The Destination Recommender Application is a project aimed at providing personalized destination recommendations to users based on their preferences and interests. The goal is to enhance the travel planning experience by leveraging machine learning models and creating a user-friendly web application.

## Skills

- NLP
- Recommender systems
- Clustering
- Web scraping
- Data Cleaning
- API development
- Data modelling

# Table of Contents

1. Code Structure
2. Tools & Packages
3. Data
4. ML Model Training
5. Results
6. API Development
7. Web Application Development
8. Future Development

# 1. Code Structure

# 2. Tools & Packages

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

# 3. Data

## Data Collection

Data of destinations were scraped from the web using APIFY's python client were written to a json file.

## Data Cleaning

- The json data was then transform into three dataframes with: destination bio, destination metrics and destination reviews.
- Missing data points in some dataframes were filled out with manual searches.

## Data Modelling

- A database schema design for a normalized database
- The cleaned dataframes were stored in a MySQL database in designated tables.

# 4. ML Model Training

To achieve the goal of the project, three models are required:

- ABSA model to generate category-aspect sentiments. This would be added to the input data for the recommender algorithms
- Content-based recommender algorithm. To recommend destinations based on user specified preference
- Knowledge-based recommender algorithm. To recommend destinations for the application's zero, based on pre-existing data and rankings.

The ABSA model is explained in the 'ABSA.md' file, while the other two are discussed below.

## Feature Engineering

The data table with description of each data has the prices, review ratings, gps coordinates and list of amenities(json).

- Prices: designated into bins to simplify categorization
- List of amenities: converted to vectors with TfidfVectorizer class from sklearn. Data was tokenized, lemmatized and case normalized before model training.

## Content-based Recommender

- Module designed for the processing of user preferences and output of destination based on cosine similarity
- Outputs are in three forms: closest by similarity, similar destinations outside of selected region and similar destinations outside of budget.

## Knowledge-based Recommender

- Module to be designed for destinations by 3 different rankings: best food, best ambience, budget friendly destinations with good sentiments.
- This feature is mainly based on the results of the ABSA model

# 5. Results

# 6. API Development

A FastAPI application was constructed and linked to the database for data retrieval and modules for inferencing models and algorithms

- Integrated with Web application

# 7. Web Application

- This is the user interface for the target audience of the product. Built with HTML, CSS and Python.
- Mainly runs on FastAPI application

# 8. Future Development

1. Complete web application features
2. Complete Integration of API with web application
3. Add knowledge-based recommender for application's zero state
4. Integrate ABSA model API
5. Add destinations for dates and fun experiences
6. Build collaborative-filtering recommender based on user profiles
