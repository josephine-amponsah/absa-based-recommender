from fastapi import FastAPI
import modules.data_models
import modules.recommender_algos
import mysql


app = FastAPI()


@app.get('/')
def home_page():
    return


@app.get('/ranking')
def ranking_rows():
    return


@app.post('/user_search')
def recommend():
    return


@app.post('/destination')
def details():
    return
