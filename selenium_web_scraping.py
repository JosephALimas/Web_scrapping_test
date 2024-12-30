# selenium nos permite interactuar con páginas web para conseguir
# la información que necesitamos

from selenium import webdriver

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By

import csv
import time

USER = "standard_user"
PASSWORD = "secret_sauce"

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #options = webdriver.ChromeOptions("--headless") #hace que no se abra ninguna ventana, todo de forma minimizada
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/")

    #LOGIN
    user_input = driver.find_element(By.ID, "user-name")
    user_input.send_keys(USER)
    pass_input = driver.find_element(By.ID, "password")
    pass_input.send_keys(PASSWORD)
    button = driver.find_element(By.ID, "login-button")
    button.click()

    
    time.sleep(60)
    
    driver.quit()

if __name__ == "__main__":
    main()