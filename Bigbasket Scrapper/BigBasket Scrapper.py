import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

class BigBasketScraper:
    def __init__(self):
        # Authenticate the Google Sheets API credentials
        scope = ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "creds.json", scope)
        self.client = gspread.authorize(creds)

        # Create a new Google Sheet and set the headers
        self.sheet_name = "BigBasket Products"
        self.sheet = self.client.create(self.sheet_name).sheet1
        self.header_row = ["City", "Super Category (P0)", "Category (P1)", "Sub Category (P2)",
                      "SKU ID", "Image", "Brand", "SKU Name", "SKU Size", "MRP", "SP", "Link", "Active?", "Out of Stock?"]
        self.sheet.append_row(self.header_row)

        # Initialize the webdriver and navigate to the website
        self.main_url = "https://www.bigbasket.com/"
        self.driver = webdriver.Chrome()
        self.driver.get(self.main_url)
        self.driver.implicitly_wait(10)
        
    def scrape(self, categories):
        # Loop through each category and subcategory
        for category in categories:
            super_category = category["super_category"]
            category_name = category["category"]
            sub_categories = category["sub_categories"]

            for sub_category in sub_categories:
                # Navigate to the subcategory page
                url = f"{self.main_url}/pc/{super_category.replace(' ', '-')}/{category_name.replace(' ', '-')}/{sub_category.replace(' ', '-')}/"
                self.driver.get(url)

                # Wait for the page to load and extract the HTML content
                time.sleep(2)
                html = self.driver.page_source
                soup = BeautifulSoup(html, "html.parser")

                # Find the products and loop through each product
                products_html = soup.find_all('div', {'class': 'col-sm-12 col-xs-5 prod-view ng-scope'})

                for product_html in products_html[:10]:
                    a_tag = product_html.find('a')
                    href = a_tag.get('href')
                    product_link = self.main_url+href
                    self.driver.get(product_link)

                    city = "Bhopal"
                    image = self.driver.find_element(By.XPATH,'//img[@alt = "Product image"]').get_attribute('src')


                    brand = self.driver.find_element(By.XPATH,"//a[@class = 'sc-jzgbtB fOnvuQ']").text
                    
                    sku_name = self.driver.find_element(By.XPATH,"//div[@class = 'sc-gJWqzi iKWfqc']").text
                    

                    sku_size = ""
                    try:
                        sku_size = self.driver.find_element(By.XPATH,"//label[@class='sc-kGXeez eLMZfa']")
                        sku_size =  sku_size.text.strip()
                        sku_size = "".join(sku_size.split()[:2])
                    except:
                        pass

                    mrp = self.driver.find_element(By.XPATH,"//div[@class = 'sc-bRBYWo iEAlBH']").text
                    

                    sp = ""
                    try:
                        sp = self.driver.find_element(By.XPATH,"//.../div[@class = 'sc-bwzfXH gLgjeg']").text
                        
                    except:
                        pass
                    
                    try:                # Check if the product is active and if it is out of stock
                        active = True
                        out_of_stock = False
                        status_element = self.driver.find_element(By.XPATH,"(//*[@class='fade sc-bbmXgH cEBnvi'])[1]")
                        if "Active" not in status_element.text:
                            active = False
                        if "Out of Stock" in status_element.text:
                            out_of_stock = True
                    except:
                        pass

                    # Append the product details to the Google Sheet
                    row = [city, super_category, category_name, sub_category, href.split("/")[-2], image, brand, sku_name, sku_size, mrp, sp, product_link, active, out_of_stock]
                    self.sheet.append_row(row)
                    print(f"Appended {sku_name} to {self.sheet_name}")
                    

    # Quit the webdriver after scraping is complete
        self.driver.quit()
        self.sheet = self.client.open(self.sheet_name)
        self.sheet.share('', perm_type='anyone', role='reader', with_link=True) 
        print(self.sheet.url)

if __name__ == '__main__':
    # categories = 
    # [
    #     {
    #         "super_category": "food-grains-oil-masala",
    #         "category": "atta-flours-sooji",
    #         "sub_categories": ["atta-whole-wheat", "besan-bengal-gram-flour", "maida-other-flours", "sooji-rava"]
    #     },
    #     {
    #         "super_category": "fruits-vegetables",
    #         "category": "fruits",
    #         "sub_categories": ["fresh-fruits", "exotic-fruits", "organic-fruits", "fruit-baskets"]
    #     }
    # ]
    categories =   [
    {
        "super_category": "Eggs-Meat-Fish",
        "category": "Marinades",
        "sub_categories": [
            "Marinated-Meat"
        ]
    },
    {
        "super_category": "Bakery-Cakes-Dairy",
        "category": "Ice-Creams-Desserts",
        "sub_categories": [
            "Ice-Creams"
        ]
    },
    {
        "super_category": "Beverages",
        "category": "Coffee",
        "sub_categories": [
            "Ground-Coffee",
            "Instant-Coffee",
        ]
    },
    {
        "super_category": "Beverages",
        "category": "Water",
        "sub_categories": [
            "Packaged-Water",
            "Spring-Water",
        ]
    },
    {
        "super_category": "Bakery-Cakes-Dairy",
        "category": "Non-Dairy",
        "sub_categories": [
            "Dairy-Free-Vegan"
        ]
    },
    {
            "super_category": "food-grains-oil-masala",
            "category": "atta-flours-sooji",
            "sub_categories": ["atta-whole-wheat", "besan-bengal-gram-flour", "maida-other-flours", "sooji-rava"]
        },
]

    scraper = BigBasketScraper()
    scraper.scrape(categories)
