import sklearn
import pandas as pd
import mysql
from sklearn.metrics.pairwise import cosine_similarity
import json

vectorizer = json.load('models/tfidf-vectorizer')

# generate tf-idf vectors of experiences


def user_vector(preferences):
    user_pref = vectorizer.transform(preferences)
    return user_pref


def get_vectors(list):
    vector = vectorizer.transform(list)
    return vector

# get cosine similarity between user preference matrix and experience matrix


def get_similarity(df, col, preferences):
    df['cos_sim'] = [cosine_similarity(
        get_vectors(exp['amenities']), user_vector(preferences)) for exp in df[col]]
    return df

# calculate weighted score of cosine_similarity, ratings and count of ratings


def get_weighted_score(df, col1, col2, col3):
    df['weighted_score'] = (0.4*df[col1]) + (0.4*df[col2]) + (0.2*df[col3])
    return df

# ranking and returning out in descending order


def output_ranking(df):
    sorted_df = df.sort_values(by='weighted_score', ascending=False)
    return sorted_df


def main_recommendation():
    return


def higher_price():
    return


def other_regions():
    return
