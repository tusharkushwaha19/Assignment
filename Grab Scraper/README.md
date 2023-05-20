# Grab Food Scraper

This script is used to scrape restaurant data from the Grab Food website. It utilizes Selenium with Chrome web driver to automate the process of scrolling through the page and capturing the required data. The scraped data is then stored in a JSON file.

## Prerequisites

- Python 3.x
- Selenium Wire library (`pip install selenium-wire`)
- Chrome web driver compatible with your Chrome browser version

## Usage

1. Clone this repository or download the `grab_food_scraper.py` script.
2. Install the required dependencies by running the following command:

   ```
   pip install selenium-wire
   ```

3. Download the Chrome web driver that matches your Chrome browser version from the [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) page. Make sure to place the web driver executable in a directory listed in your system's `PATH` environment variable.

4. Run the script using the following command:

   ```
   python grab_food_scraper.py
   ```

5. The script will launch a Chrome browser window and navigate to the Grab Food website (https://food.grab.com/ph/en/restaurants).
6. It will then scroll through the page to load more restaurant data dynamically. The script will wait for 10 seconds between each scroll to allow the page to load properly. You can adjust the value of the `SCROLL_PAUSE_TIME` variable in the script to modify the wait time.
7. Once all the restaurant data is loaded, the script will scrape the required information from the network requests made by the website. It will capture the restaurant ID, name, latitude, and longitude.
8. The scraped data will be stored in a file named `latlng_data.json` in the same directory as the script. Each restaurant will be represented as a JSON object with the following properties:

   - `id`: The ID of the restaurant.
   - `name`: The name of the restaurant.
   - `latitude`: The latitude coordinate of the restaurant.
   - `longitude`: The longitude coordinate of the restaurant.

   ```
   [
       {
           "id": "123456",
           "name": "Restaurant 1",
           "latitude": 12.3456,
           "longitude": 98.7654
       },
       {
           "id": "789012",
           "name": "Restaurant 2",
           "latitude": 34.5678,
           "longitude": 67.8901
       },
       ...
   ]
   ```

9. You can now use the `latlng_data.json` file for further analysis or processing.

## Notes

- It's important to note that web scraping can be against the terms of service of some websites. Make sure to review the website's terms of service before scraping any data.
- The script utilizes Selenium Wire, which is an extension of Selenium that allows capturing network requests made by the browser. This allows us to extract the required data from the website's API calls.
- The script includes a scroll feature to load more data dynamically. Adjust the `SCROLL_PAUSE_TIME` value to control the wait time between each scroll. This value should be set according to the website's loading speed.
- The script is specifically designed for the Grab Food website and may not work for other websites with different structures or APIs.
- The Chrome browser window launched by the script will remain open until the script finishes executing. You can modify the script to close the browser window after scraping if needed.
