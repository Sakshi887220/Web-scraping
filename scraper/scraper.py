from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

def scrape():
    
    for i in range(0, 428):
        
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
