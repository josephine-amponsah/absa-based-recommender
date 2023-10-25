import sklearn
import pandas as pd
import mysql
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
import joblib
from modules.data_models import HotelData, UserInput, OutputData, RankingData

with open('models/tfidf-vectorizer.pkl', 'rb') as f:
    vectorizer = joblib.load(f)

# generate tf-idf vectors of experiences


def user_vector(preferences: UserInput):
    user_pref = vectorizer.transform(preferences.experience)
    matrix = user_pref.toarray()
    matrix_as_list = matrix.tolist()
    return matrix_as_list


def get_vectors(options):
    vector = vectorizer.transform(options)
    matrix = vector.toarray()
    matrix_as_list = matrix.tolist()  #
    return matrix_as_list

# get cosine similarity between user preference matrix and experience matrix


def get_similarity(df: HotelData, preferences):
    data = pd.DataFrame(df)
# Parse the 'experience' column as JSON
    data['experience'] = data['experience'].apply(json.loads)
    cos_sim_means = []
    for record in data['experience']:
        cos_sim = cosine_similarity(get_vectors(
            record['amenities']), user_vector(preferences))
        # Calculate the mean of the cosine similarity values
        mean_cos_sim = np.mean(cos_sim)
        cos_sim_means.append(mean_cos_sim)  # Append the mean to the list

    data['cos_sim'] = cos_sim_means
    return data

# calculate weighted score of cosine_similarity, ratings and count of ratings


def get_weighted_score(df):
    df['weighted_score'] = (0.6 * df["cos_sim"]) + \
        (0.25 * df["total_score"]) + (0.15 * df["reviews_count"])
    return df

# ranking and returning out in descending order


def output_ranking(df: OutputData):
    sorted_df = df.sort_values(by='weighted_score', ascending=False)
    return sorted_df


def main_recommendation(df, preferences):
    sim_df = get_similarity(df, preferences)
    # weighted_df = get_weighted_score(sim_df)
    # sorted_df = output_ranking(weighted_df)
    return sim_df


def higher_price():
    return


def other_regions():
    return
