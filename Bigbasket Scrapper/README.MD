**BigBasket Scraper**
This is a Python script that scrapes the BigBasket website and saves the details of the products in a Google Sheet. The script uses the following libraries:

time
gspread
oauth2client
selenium
BeautifulSoup
Installation
To use this script, you need to install the required libraries. You can install them using the following command:


pip install time gspread oauth2client selenium beautifulsoup4
You also need to download the Chrome WebDriver and save it in the same directory as the script.

Usage
To use this script, you need to create a Google Sheets API credential and save it in a JSON file called creds.json. Follow these instructions to create the credentials.

You also need to create a list of categories and subcategories to scrape. Each category should be a dictionary with the following keys:

super_category: the name of the super category (e.g. "food-grains-oil-masala")
category: the name of the category (e.g. "atta-flours-sooji")
sub_categories: a list of subcategories (e.g. ["atta-whole-wheat", "besan-bengal-gram-flour", "maida-other-flours", "sooji-rava"])
Create an instance of the BigBasketScraper class and call the scrape method with the list of categories as the argument


