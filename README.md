This is what you can see on UI. To fetch the trending topics click on the link i.e. click here to run the script.
![Twitter-Trending-Topics1](https://github.com/user-attachments/assets/72012fe7-27be-43a4-b134-7d3d3b78229a)

After clicking on the link it will login to your Twitter account automatically and you will get top 5 happening topics of twitter successfully with date, time, IP Address used for that query and json extract from MongoDB
![Twitter-Trending-Topics2](https://github.com/user-attachments/assets/3d1c90ac-3bd6-4cf8-acb5-faf6f38dcd2b)

When you click on "Click here to run the query again" it will fetch the latest happening topics again and you can see date and time is also updated 
![Twitter-Trending-Topics3](https://github.com/user-attachments/assets/b74b96d1-1a11-4609-aa5d-de55cd25faba)


# Twitter Trending Topics

This project fetches Twitter's top 5 trending topics with live date and time using Selenium and ProxyMesh when we click on click here to run the script by the way you will be automatically logged into twitter first because I have done the coding for it also. The scraped data is stored in a MongoDB database and displayed on a web page. You can see there is json data also extracted from the record of MongoDB.And when you click on click here to run the script again the latest top 5 twitter trending topics are fetched again. I have done everything successfully covered all the points of assignment.

## Project Structure

```
Twitter-Trending-Topics
├── src
│   ├── app.py                # Main entry point of the application
│   ├── scraper
│   │   ├── __init__.py       # Package initialization
│   │   └── twitter_scraper.py # Selenium script for scraping Twitter
│   ├── database
│   │   ├── __init__.py       # Package initialization
│   │   └── mongodb.py        # MongoDB connection and data handling
│   ├── web
│   │   ├── __init__.py       # Package initialization
│   │   ├── templates
│   │   │   └── index.html     # HTML template for the web page
│   │   └── static
│   │       └── styles.css     # CSS styles for the web page
│   └── utils
│       └── __init__.py       # Utility functions
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .env                       # Environment variables
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/PrafulShinde8/Twitter-Trending-Topics.git
   cd Twitter-Trending-Topics
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. requirements.txt
   ```
   Flask
   Selenium
   pymongo
   python-dotenv
   requests
   beautifulsoup4
   webdriver-manager
   ```
4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys and database connection strings.
   ```
   MONGO_URI=mongodb://localhost:27017/
   PROXYMESH_URL=http://username:password@us-ca.proxymesh.com:31280
   TWITTER_USERNAME=Your twitter username
   TWITTER_PASSWORD=Your twitter password

5. **Run the application:**
   ```
   python src/app.py
   ```

## Usage

- Open your web browser and navigate to `http://localhost:5000`.
- Click the link named Click here to run the script and view the top 5 trending topics from Twitter.

## Notes

- Ensure that you have the necessary permissions to scrape data from Twitter.
- This project uses ProxyMesh for IP rotation to avoid being blocked by Twitter.

## License

This project is licensed under the MIT License.
