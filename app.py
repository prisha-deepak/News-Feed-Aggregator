from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://newsapi.org/v2/everything'

app = Flask(__name__)

@app.route('/')
def index():
    query = request.args.get('query', 'technology')
    articles = fetch_news(query)
    return render_template('index.html', articles=articles)

def fetch_news(query):
    params = {
        'q': query,
        'apiKey': API_KEY,
        'pageSize': 10,
        'sortBy': 'publishedAt'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return []

if __name__ == '__main__':
    app.run(debug=True)
