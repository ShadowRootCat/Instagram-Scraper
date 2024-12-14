import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CONFIG_FILE = '../config.ini'

def load_credentials():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config['Instagram']['username'], config['Instagram']['password']

def init_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=360,640")
    return webdriver.Chrome(service=Service("chromedriver"), options=options)

def fetch_profile(driver, username):
    driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(3)
    name = driver.find_element(By.XPATH, "//h1").text
    bio = driver.find_element(By.XPATH, "//div[@class='-vDIg']").text
    return name, bio

def main():
    username, password = load_credentials()
    driver = init_browser()
    try:
        target = input("Enter Instagram username: ")
        name, bio = fetch_profile(driver, target)
        print(f"Name: {name}\nBio: {bio}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
