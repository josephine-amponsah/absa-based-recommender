from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import modules.data_models
import modules.recommender_algos
import mysql
from dotenv import load_dotenv
import os
from modules.data_models import UserInput, OutputData
import pandas as pd

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
# DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
try:
    # Create database connection
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
except mysql.connector.Error as err:
    # Handle error
    error_msg = f"Error connecting to database: {err}"
    JSONResponse(content={"error": error_msg}, status_code=500)


cursor = conn.cursor()

app = FastAPI()


@app.get('/')
def home_page():
    return


@app.get('/recommendation')
def ranking_rows(user_pref: UserInput):
    query = "SELECT * FROM hotels_details WHERE price_bins = %s "
    cursor.execute(query, (user_pref['price_range'],))
    query_result = cursor.fetchall()
    df = pd.DataFrame(query_result, columns=[
                      col[0] for col in cursor.description])

    return


@app.post('/destination')
def details():
    return


@app.post('/dest')
def recommend():
    return


@app.post("/process/")
async def process(user_input: str = Form(...)):
    # Process user input and perform actions

    # Redirect to other endpoints with user input as query parameters
    redirect_url1 = f"/endpoint1?input={user_input}"
    redirect_url2 = f"/endpoint2?input={user_input}"
    redirect_url3 = f"/endpoint3?input={user_input}"

    return {
        "message": "User input processed successfully",
        "redirect_urls": [redirect_url1, redirect_url2, redirect_url3]
    }


@app.get("/endpoint1")
async def endpoint1(input: str = None):
    return {"endpoint": "Endpoint 1", "input": input}


@app.get("/endpoint2")
async def endpoint2(input: str = None):
    return {"endpoint": "Endpoint 2", "input": input}


@app.get("/endpoint3")
async def endpoint3(input: str = None):
    return {"endpoint": "Endpoint 3", "input": input}
