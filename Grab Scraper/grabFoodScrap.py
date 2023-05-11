import gzip
import time
from seleniumwire import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from selenium.webdriver.common.by import By

class Driver:
    def __init__(self):
        # Create ChromeOptions object
        chrome_options = Options()

        # Set capability to ignore SSL errors
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptInsecureCerts'] = True

        # Add capability to ChromeOptions object
        chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-features=NetworkService")
        chrome_options.add_argument("--enable-features=NetworkServiceInProcess")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--disable-popup-blocking")

        # Create Chrome driver with ChromeOptions and capabilities
        self.browser = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities)

    def __del__(self):
        self.browser.quit()

    def get(self, url):
        try:
            self.browser.get(url)
            return True
        except:
            print("Error: Could not get URL")
            return False

class Scrapper:
    def __init__(self , driver: Driver):
        self.driver = driver.browser

    def scroll_page(self, SCROLL_PAUSE_TIME):
        # Get the height of the entire page
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to the bottom of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Scroll up by 300 pixels
            self.driver.execute_script("window.scrollBy(0, -300);")

            # Wait to load the page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate the new height of the page and check if we've reached the bottom
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def scrape_data(self):
        list_r = []   
        for request in self.driver.requests:
            if request.path == '/foodweb/v2/search':
                body = request.response.body
                if request.response.headers.get('Content-Encoding') == 'gzip':
                    body = gzip.decompress(body).decode('utf-8')
                body_json = json.loads(body)
                search_merchants = body_json['searchResult']['searchMerchants']
                for restaurant in search_merchants:
                    data = {}
                    data['id'] = restaurant['id']
                    data['name'] = restaurant['address']['name']
                    data['latitude'] = restaurant['latlng']['latitude']
                    data['longitude'] = restaurant['latlng']['longitude']
                    list_r.append(data)
        print(len(list_r))
        with open('latlng_data.json', 'w', encoding='utf-8') as f:
            json.dump(list_r, f, ensure_ascii=False, indent=4)  


if __name__ == '__main__':
    driver = Driver()
    driver.get('https://food.grab.com/ph/en/restaurants')
    scrapper = Scrapper(driver)
    scrapper.scroll_page(10)
    scrapper.scrape_data()


