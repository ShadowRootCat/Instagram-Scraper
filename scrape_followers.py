import configparser
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

CONFIG_FILE = '../config.ini'

def load_credentials():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config['Instagram']['username'], config['Instagram']['password']

def init_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=360,640")
    return webdriver.Chrome(service=Service("chromedriver"), options=options)

def login(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
    time.sleep(5)

def scrape_followers(driver, profile, limit):
    driver.get(f"https://www.instagram.com/{profile}/followers/")
    time.sleep(3)
    followers = set()
    while len(followers) < limit:
        elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/')]")
        for el in elements:
            followers.add(el.text)
            if len(followers) >= limit:
                break
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)
    return followers

def main():
    username, password = load_credentials()
    driver = init_browser()
    try:
        login(driver, username, password)
        profile = input("Enter profile username: ")
        limit = int(input("Max followers to fetch: "))
        followers = scrape_followers(driver, profile, limit)
        with open(f"followers_{profile}.txt", "w") as file:
            file.write("\n".join(followers))
        print(f"Followers saved to followers_{profile}.txt")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
