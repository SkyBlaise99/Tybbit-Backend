import os
import psycopg2

from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS

RED = 1
BLUE = 2

GET_RED_SCORES_IN_ORDER = "SELECT name, score FROM usersRed ORDER BY score;"
GET_BLUE_SCORES_IN_ORDER = "SELECT name, score FROM usersBlue ORDER BY score;"

INSERT_RED_SCORE = "INSERT INTO usersRed (name, score) VALUES (%s, %s) RETURNING id;"
INSERT_BLUE_SCORE = "INSERT INTO usersBlue (name, score) VALUES (%s, %s) RETURNING id;"

load_dotenv()

app = Flask(__name__)
CORS(app, support_credentials=True)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


@app.get("/get/red")
def get_red_scores_in_order():
    return get_scores_in_order(RED)


@app.get("/get/blue")
def get_blue_scores_in_order():
    return get_scores_in_order(BLUE)


def get_scores_in_order(color):
    with connection:
        with connection.cursor() as cursor:
            if color is RED:
                command = GET_RED_SCORES_IN_ORDER
            elif color is BLUE:
                command = GET_BLUE_SCORES_IN_ORDER

            cursor.execute(command)
            results = cursor.fetchall()

    scores = []
    for result in results:
        scores.append(reformat_score(result))

    return scores


def reformat_score(raw):
    res = {}

    res["name"] = raw[0]
    res["score"] = raw[1]

    return res


@app.post("/add/red")
def add_red_score():
    return add_score(RED)


@app.post("/add/blue")
def add_blue_score():
    return add_score(BLUE)


def add_score(color):
    name = request.args.get("name")
    score = request.args.get("score")

    with connection:
        with connection.cursor() as cursor:
            if color is RED:
                command = INSERT_RED_SCORE
            elif color is BLUE:
                command = INSERT_BLUE_SCORE

            cursor.execute(command, (name, score))
            id = cursor.fetchone()[0]

    return "User " + str(id) + " added", 201
