from flask import Flask, render_template, request
import openai

app = Flask (__name__)

openai.api_key = ''

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