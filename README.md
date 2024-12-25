![Twitter-Trending-Topics1](https://github.com/user-attachments/assets/72012fe7-27be-43a4-b134-7d3d3b78229a)
# Web Scraping Project

This project implements a web scraping application that fetches Twitter's top 5 trending topics using Selenium and ProxyMesh. The scraped data is stored in a MongoDB database and displayed on a web page.

## Project Structure

```
web-scraping-project
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
   git clone <repository-url>
   cd web-scraping-project
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

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys and database connection strings.

5. **Run the application:**
   ```
   python src/app.py
   ```

## Usage

- Open your web browser and navigate to `http://localhost:5000`.
- Click the button to run the scraping script and view the top 5 trending topics from Twitter.

## Notes

- Ensure that you have the necessary permissions to scrape data from Twitter.
- This project uses ProxyMesh for IP rotation to avoid being blocked by Twitter.

## License

This project is licensed under the MIT License.
