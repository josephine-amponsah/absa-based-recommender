from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import modules.data_models
from modules.recommender_algos import main_recommendation
import mysql
from dotenv import load_dotenv
import os
from modules.data_models import UserInput, OutputData
import pandas as pd
import json
import mysql.connector
import uvicorn
from fastapi.staticfiles import StaticFiles
import numpy as np

load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
# DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

try:
    # Create database connection
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
except mysql.connector.Error as err:
    # Handle error
    error_msg = f"Error connecting to database: {err}"
    JSONResponse(content={"error": error_msg}, status_code=500)


cursor = conn.cursor()

with open("modules/options.json", "r") as options_file:
    options_data = json.load(options_file)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def home_page(request: Request):
    return templates.TemplateResponse("base.html", {"options": options_data, "request": request})


@app.post('/recommendation/')
def ranking_rows(budget: str = Form(...),
                 experience: list = Form(...),
                 region: str = Form(...)):
    user_input = UserInput(budget=budget, experience=experience, region=region)

    query = """SELECT hd.* ,hi.*
    FROM hotels_details hd
    INNER JOIN hotels_info hi ON hd.place_id = hi.place_id
    WHERE hd.price_bins = %s 
    AND hi.region = %s"""
    cursor.execute(query, (user_input.budget, user_input.region))
    query_result = cursor.fetchall()
    result_list = [dict(zip([col[0] for col in cursor.description], row))
                   for row in query_result]
    output = main_recommendation(df=result_list, preferences=user_input)
    return {"data": result_list, "result": output}


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


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                reload=True)
