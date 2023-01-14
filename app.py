import os
import psycopg2

from dotenv import load_dotenv
from flask import Flask, request, jsonify

GET_SCORES_IN_ORDER = "SELECT name, score FROM users ORDER BY score;"
INSERT_SCORE = "INSERT INTO users (name, score) VALUES (%s, %s) RETURNING id;"

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


@app.get("/get")
def get_scores_in_order():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_SCORES_IN_ORDER)
            results = cursor.fetchall()

            scores = []
            for result in results:
                scores.append(reformat_score(result))

            return add_header(scores)


def reformat_score(raw):
    res = {}

    res["name"] = raw[0]
    res["score"] = raw[1]

    return res


def add_header(result):
    resp = jsonify(result)
    resp.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return resp


@app.post("/add")
def add_score():
    data = request.get_json()
    name = data["name"]
    score = data["score"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_SCORE, (name, score))
            id = cursor.fetchone()[0]

            return "User " + str(id) + " added", 201
