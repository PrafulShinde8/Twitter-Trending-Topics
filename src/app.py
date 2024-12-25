import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, jsonify
from scraper.twitter_scraper import TwitterScraper
from database.mongodb import MongoDB

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
scraper = TwitterScraper()
db = MongoDB()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-scraper', methods=['POST'])
def run_scraper():
    record = scraper.save_trending_topics()
    return jsonify(record)

@app.route('/latest-trends', methods=['GET'])
def latest_trends():
    record = db.get_latest_record()
    return jsonify(record)

if __name__ == '__main__':
    app.run(debug=True)
