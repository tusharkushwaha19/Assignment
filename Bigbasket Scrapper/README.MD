# BigBasket Scraper

This script is used to scrape product data from the BigBasket website. It utilizes Selenium and Beautiful Soup libraries to automate the process of navigating through the website and extracting the required information. The scraped data is then stored in a Google Sheet.

## Prerequisites

- Python 3.x
- Selenium library (`pip install selenium`)
- Beautiful Soup library (`pip install beautifulsoup4`)
- gspread library (`pip install gspread`)
- oauth2client library (`pip install oauth2client`)
- Chrome web driver compatible with your Chrome browser version
- Google Sheets API credentials (JSON file)

## Setup

1. Clone this repository or download the `bigbasket_scraper.py` script.
2. Install the required dependencies by running the following command:

   ```
   pip install selenium beautifulsoup4 gspread oauth2client
   ```

3. Download the Chrome web driver that matches your Chrome browser version from the [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) page. Make sure to place the web driver executable in a directory listed in your system's `PATH` environment variable.

4. Obtain the Google Sheets API credentials by following the steps below:
   - Go to the [Google Cloud Console](https://console.developers.google.com/).
   - Create a new project (or select an existing project).
   - Enable the Google Sheets API for the project.
   - Create service account credentials and download the JSON file.
   - Rename the downloaded JSON file to `creds.json` and place it in the same directory as the script.

5. In the `__init__` method of the `BigBasketScraper` class, modify the `self.sheet_name` variable to set the name for the Google Sheet that will be created to store the scraped data.

6. In the `__init__` method of the `BigBasketScraper` class, update the `self.header_row` list to match the desired column headers for the Google Sheet. Make sure the order of the headers matches the order of the data being appended in the `row` list later in the script.

7. In the `scrape` method of the `BigBasketScraper` class, update the `categories` list to include the desired categories, subcategories, and super categories that you want to scrape. Each category should be represented as a dictionary with the following structure:

   ```
   {
       "super_category": "Super Category Name",
       "category": "Category Name",
       "sub_categories": ["Subcategory 1", "Subcategory 2", ...]
   }
   ```

   Add or remove dictionaries as needed to scrape data from different categories.

## Usage

1. Run the script using the following command:

   ```
   python bigbasket_scraper.py
   ```

2. The script will launch a Chrome browser window and navigate to the BigBasket website.
3. It will scrape the specified categories and subcategories, visiting each product page and extracting relevant information.
4. The scraped data will be stored in a Google Sheet with the specified name, and the column headers will be set accordingly.
5. You can view the Google Sheet by opening the URL printed in the console after the scraping is complete.

## Notes

- The script utilizes Selenium to automate browser actions and Beautiful Soup to extract data from the HTML content.
- Make sure to adjust the `time.sleep` durations according to the website's loading speed and network conditions to ensure proper scraping.
- The `driver.quit()` method is called to close the browser window after scraping is complete.
- The Google Sheet is created using the gspread library, and the Google Sheets API credentials are used for authentication. Make sure to provide the correct path to the `creds

.json` file.
- The `self.sheet.share()` method is used to generate a shareable link for the Google Sheet. You can remove or modify this line if you don't need to share the sheet.
- Review the BigBasket website's terms of service to ensure compliance with scraping activities.



# **To obtain the JSON credentials(creds.json) for the Google Sheets API, you need to follow these steps:**

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

Keep the downloaded JSON file in a folder where you save this script
