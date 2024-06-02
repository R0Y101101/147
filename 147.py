from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import _time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

#NASA Exoplanets URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"  # URL of the NASA Exoplanet Catalog


#Webdriver
browser = webdriver.Chrome() #Initializing Chrome WebDriver
browser.get(START_URL) # Opening the specified URL in the browser

time.sleep(2) #Adding a delay to allow the page to load completel


planets_data =[]

#Define Exoplanets Data Scapping Method
def scrape():
    for i in range(0,10):
        print(f'Scrapping page{i+1}')
        

        #Beautiful Soup Object
soup = BeautifulSoup(browser.page_source, 'html.partial')


planetinfo.append(planet.find('h3', class='heading-22'))    # Finding and storing the planet names

information_to_extract = ["light-years from earth", "planet mass", "stellar magnitude", "discovery date"]

for infoname in information_to_extract():
