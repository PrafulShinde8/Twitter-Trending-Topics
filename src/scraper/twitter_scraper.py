# import os
# import re
# import time
# import uuid
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from dotenv import load_dotenv
# from src.database.mongodb import MongoDB

# load_dotenv()

# class TwitterScraper:
#     def __init__(self):
#         self.db = MongoDB()
#         self.proxy_url = os.getenv('PROXYMESH_URL')
#         self.username = os.getenv('TWITTER_USERNAME')
#         self.password = os.getenv('TWITTER_PASSWORD')

#     def get_driver(self):
#         options = Options()
#         options.add_argument('--headless')
#         options.add_argument('--disable-gpu')
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')

#         proxy = Proxy()
#         proxy.proxy_type = ProxyType.MANUAL
#         proxy.httpProxy = self.proxy_url
#         proxy.sslProxy = self.proxy_url
#         options.proxy = proxy

#         # Update the path to the ChromeDriver executable
#         chrome_driver_path = r"C:\WebDrivers\chromedriver-win32\chromedriver.exe"  # Ensure this path is correct
#         service = Service(chrome_driver_path)
#         driver = webdriver.Chrome(service=service, options=options)
#         return driver

#     def login(self, driver):
#         driver.get('https://twitter.com/login')
#         wait = WebDriverWait(driver, 10)
#         username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']")))
#         username_field.send_keys(self.username)
#         username_field.send_keys(Keys.RETURN)

#         try:
#             password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
#         except:
#             username_validation_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']")))
#             username_validation_field.send_keys(self.username)
#             username_validation_field.send_keys(Keys.RETURN)
#             password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))

#         password_field.send_keys(self.password)
#         password_field.send_keys(Keys.RETURN)
#         time.sleep(5)

#     def fetch_trending_topics(self):
#         driver = self.get_driver()
#         self.login(driver)
#         driver.get('https://twitter.com/explore/tabs/trending')
#         wait = WebDriverWait(driver, 10)
#         trends_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Timeline: Explore']")))
#         trends = trends_container.find_elements(By.CSS_SELECTOR, "div[data-testid='trend']")

#         top_trends = []
#         for trend in trends[:5]:
#             intermediate_trend = trend.find_elements(By.CSS_SELECTOR, "div.css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-b88u0q.r-1bymd8e")
        
#             for element in intermediate_trend:
#                 # print("trend", element.text)
#                 top_trends.append(element.text)

#         ip_address = self.get_public_ip()
#         print("IP Address for calling twitter is", ip_address)

#         driver.quit()
#         return top_trends[:5]

#     def get_public_ip(self):
#         driver = self.get_driver()
        
#         driver.get('https://ifconfig.me')
#         wait = WebDriverWait(driver, 10)
#         page_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body"))).text
#         #print("page_text", page_text)

#         # Extract IP address using regular expression
#         match = re.search(r'(\d+\.\d+\.\d+\.\d+)', page_text)
#         ip_address = match.group(1) if match else 'N/A'
#         #print("IP Address", ip_address)

#         driver.quit()
#         return f"IP Address {ip_address}"

#     def save_trending_topics(self):
#         trends = self.fetch_trending_topics()
#         ip_address = self.get_public_ip()
      
#         record = {
#             '_id': str(uuid.uuid4()),
#             'trend1': trends[0],
#             'trend2': trends[1],
#             'trend3': trends[2],
#             'trend4': trends[3],
#             'trend5': trends[4],
#             'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
#             'ip_address': ip_address
#         }
#         self.db.insert_record(record)
#         return record




import os
import re
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from src.database.mongodb import MongoDB

load_dotenv()

class TwitterScraper:
    def __init__(self):
        self.db = MongoDB()
        self.proxy_url = os.getenv('PROXYMESH_URL')
        self.username = os.getenv('TWITTER_USERNAME')
        self.password = os.getenv('TWITTER_PASSWORD')

    def get_driver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.httpProxy = self.proxy_url
        proxy.sslProxy = self.proxy_url
        options.proxy = proxy

        # Update the path to the ChromeDriver executable
        chrome_driver_path = r"C:\WebDrivers\chromedriver-win32\chromedriver.exe"  # Ensure this path is correct
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def login(self, driver):
        driver.get('https://twitter.com/login')
        wait = WebDriverWait(driver, 20)  # Increased timeout to 20 seconds
        try:
            username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']")))
            username_field.send_keys(self.username)
            username_field.send_keys(Keys.RETURN)

            try:
                password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
            except:
                username_validation_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']")))
                username_validation_field.send_keys(self.username)
                username_validation_field.send_keys(Keys.RETURN)
                password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))

            password_field.send_keys(self.password)
            password_field.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Error during login: {e}")
            driver.save_screenshot("login_error.png")  # Save a screenshot for debugging
            raise

    def fetch_trending_topics(self):
        driver = self.get_driver()
        try:
            self.login(driver)
            driver.get('https://twitter.com/explore/tabs/trending')
            wait = WebDriverWait(driver, 20)  # Increased timeout to 20 seconds
            trends_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Timeline: Explore']")))
            trends = trends_container.find_elements(By.CSS_SELECTOR, "div[data-testid='trend']")

            top_trends = []
            for trend in trends[:5]:
                intermediate_trend = trend.find_elements(By.CSS_SELECTOR, "div.css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-b88u0q.r-1bymd8e")
            
                for element in intermediate_trend:
                    top_trends.append(element.text)

            ip_address = self.get_public_ip()
            print("IP Address for calling twitter is", ip_address)

            return top_trends[:5]
        except Exception as e:
            print(f"Error fetching trending topics: {e}")
            driver.save_screenshot("fetch_trending_topics_error.png")  # Save a screenshot for debugging
            raise
        finally:
            driver.quit()

    def get_public_ip(self):
        driver = self.get_driver()
        try:
            driver.get('https://ifconfig.me')
            wait = WebDriverWait(driver, 10)
            page_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body"))).text

            # Extract IP address using regular expression
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)', page_text)
            ip_address = match.group(1) if match else 'N/A'

            return f"IP Address {ip_address}"
        except Exception as e:
            print(f"Error fetching public IP: {e}")
            driver.save_screenshot("get_public_ip_error.png")  # Save a screenshot for debugging
            raise
        finally:
            driver.quit()

    def save_trending_topics(self):
        try:
            trends = self.fetch_trending_topics()
            if len(trends) < 5:
                raise ValueError("Not enough trending topics fetched")

            ip_address = self.get_public_ip()
        
            record = {
                '_id': str(uuid.uuid4()),
                'trend1': trends[0],
                'trend2': trends[1],
                'trend3': trends[2],
                'trend4': trends[3],
                'trend5': trends[4],
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'ip_address': ip_address
            }
            self.db.insert_record(record)
            return record
        except Exception as e:
            print(f"Error saving trending topics: {e}")
            raise