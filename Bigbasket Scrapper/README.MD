# **BigBasket Scraper**


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



##To obtain the JSON credentials(creds.json) for the Google Sheets API, you need to follow these steps:

Go to the Google Cloud Console.

Create a new project or select an existing project from the dropdown menu in the top navigation bar.

On the left sidebar, click on the "APIs & Services" and then click on "Library".

Search for "Google Sheets API" and select it from the results.

Click on the "Enable" button to enable the Google Sheets API for your project.

On the left sidebar, click on "Credentials" under "APIs & Services".

Click on the "Create Credentials" button and select "Service Account" from the dropdown menu.

Provide a name for your service account and click on the "Create" button.

On the "Service account permissions" page, you can set the required permissions for your service account. If you only need to access Google Sheets, you can assign the "Editor" role. Click on the "Continue" button.

On the next page, you can skip the "Grant users access to this service account" section by clicking on the "Done" button.

Back on the "Credentials" page, find your newly created service account in the list and click on the pencil icon to edit its settings.

In the "Keys" tab, click on the "Add Key" button and select "Create new key" from the dropdown menu.

Choose the JSON key type and click on the "Create" button. This will download a JSON file containing your service account credentials.

Keep the downloaded JSON file in a secure location as it contains sensitive information.

