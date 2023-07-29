import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

df =  pd.read_csv('aaj_tak_halla_bol.csv')

def scrape_page_with_load_more(url):
    # Configure the Chrome webdriver (you can change this to other browsers)
    driver = webdriver.Chrome() #This will open a Chrome browser window for web automation.

    # Request the initial page using the requests library
    driver.get(url)

    time.sleep(3)  # Give the page some time to load completely
    #Note that using time.sleep() for waiting is not the best practice for real web scraping, but for this simple example, it works.

    try:
        #Setting parameters for load more button
        # Set a maximum number of times you want to click the "Load More" button
        max_load_more_clicks = 12
        load_more_button_xpath = '//*[@id="load_more"]'

        for _ in range(max_load_more_clicks):
            # Find the "Load More" button and click it
            # it locates the "Load More" button using the WebDriverWait and expected_conditions from Selenium, and then clicks it using the execute_script() method.
            load_more_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, load_more_button_xpath))
            )
            # timeout = 10 refers to the maximum amount of time (in seconds) that the WebDriver will wait for a specific condition to be met before raising a TimeoutException
            driver.execute_script("arguments[0].click();", load_more_button)

            # Wait for a few seconds to let the new content load
            time.sleep(3)

        # Once all content is loaded, get the page source using BeautifulSoup
        page_source = driver.page_source  #view page source
        soup = BeautifulSoup(page_source, "html.parser") #parsing page source

        # Now, you can parse the soup to extract the data you need from the page
        urls = soup.select('div.widget-listing-thumb a')
        title = []
        href = []
        for i in urls:
          title.append(i.get('title'))
          href.append(i.get('href'))
        df['title'] = title
        df['href'] = href
        df.to_csv('aaj_tak_halla_bol.csv')

    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://www.aajtak.in/programmes/halla-bol"  # Replace this with the URL of the webpage you want to scrape
    scrape_page_with_load_more(url)
