from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time
import sys



#Locators
WEBPAGE_BASEURL = "https://useinsider.com/"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

def Scenario1(): # Open Insider Home Page
    driver.get(WEBPAGE_BASEURL)
    # Check if the Insider homepage is opened
    if driver.title == "#1 Leader in Individualized, Cross-Channel CX — Insider":
        print("Insider homepage is opened")
    else:
        print("Insider homepage is not opened")

def Scenario2():
    driver.get(WEBPAGE_BASEURL)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wt-cli-accept-all-btn"))).click()   #pop-up closed. accept all button.
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li.dropdown:nth-child(6) > a:nth-child(1) > span:nth-child(1)"))).click()   
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[6]/div/div[1]/div[3]/div/a").click() #career section

    # Our Locations Section Check Process
    element = driver.find_element(By.XPATH, "//*[contains(text(), 'Our Locations')]")
    text1 = element.text
    def check (text1):
        assert text1 == "Our Locations" , "Our Locations is not on the site."
    print("Our Locations title found.")
    #Teams Section Check Process
    element = driver.find_element(By.XPATH, "//*[contains(text(), 'See all teams')]")
    text2 = element.text
    def check(text2):
        assert text2 == "See all teams","Teams Information is not on this page!"
    print("See all teams button found.")
    #Life at Insider Section Check Process
    element = driver.find_element(By.XPATH, "//*[contains(text(), 'Life at Insider')]")
    text3 = element.text
    def check(text3):
        assert text3 == "Life at Insider","Life at Insider section is not on this page!"
    print(" Life at Insider title found. ")

def Scenario3():
    driver.get(WEBPAGE_BASEURL)
    driver.maximize_window()
    
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wt-cli-accept-all-btn"))).click()   #pop-up closed. accept all button.
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li.dropdown:nth-child(6) > a:nth-child(1) > span:nth-child(1)"))).click()   
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[6]/div/div[1]/div[3]/div/a").click() #career section
    sleep(2)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#career-our-location > div > div > div > div.col-12.col-md-6 > h3"))) #Find Our Locations
    element_to_select = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='career-find-our-calling']/div/div/a"))) #select see all teams button
    action.move_to_element(element_to_select)
    action.perform()
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section/div/div/div[2]/div[12]/div[1]/a"))).click()  #Select Quality Assurance
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#page-head > div > div > div.col-12.col-lg-7.order-2.order-lg-1 > div > div > a"))).click()   #See all QA jobs button
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,"select2-filter-by-location-container"))).click() #filter
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,"select2-filter-by-location-result-v74z-Istanbul, Turkey"))).click() #Location Selection 

Scenario3()