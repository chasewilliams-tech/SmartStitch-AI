from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Fashion AI"

app.run(debug=True)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods = ["POST"])
def api():

    message = request.json.get("message" )

    completion = openai.ChatCompletion.create(
        model = "gpt-4.1-mini",
        messages=[
        {"role": "user", "content": message}
        ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message 
    else :
        return 'Failed to Generate response!'
    if _name_ == '__main__':
        app.run( )

@app.route("/recommend", methods=["POST"])
def recommend_route():

    budget = int(request.form["budget"])
    style = request.form["style"]

    results = recommend(budget, style)

    return results.to_html()

from flask import request

@app.route("/recommend", methods=["POST"])
def recommend_route():

    budget = int(request.form["budget"])
    style = request.form["style"]

    results = recommend(budget, style)

    return results.to_html()

# // Ask AI // * 

def recommend(products, budget):
    return [item for item in products if item["price"] <= budget]

def recommend(budget, style, color, size, material, structure, hardware, season):

    results = products[
        (products["price"] <= budget) &
        (products["style"] == style) &
        (products["size"] == size) &
        (products["season"] == season) &
        (products["size"] == hardware) &
        (products["structure"] == structure) &
        (products["color"] == color)
    ]

    return results

budget = int(input("Budget: "))
style = input("Style: ")

results = recommend(budget, style)

print(results)

def score(item, budget, style, color):

    points = 0

    if item["price"] <= budget:
        points += 5

    if item["style"] == style:
        points += 4

    if item["color"] == color:
        points += 3

    return points

products = products.sort_values(
    by="score",
    ascending=False
)

from flask import request