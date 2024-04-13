from flask import Flask, render_template
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

client = OpenAI()

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/generate/<prompt>")
def generateImage(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    return {"url": response.data[0].url}