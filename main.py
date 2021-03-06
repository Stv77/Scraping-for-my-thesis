from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://____.co.id/list-bisnis')
driver.maximize_window()
time.sleep(10)

container = []

while True:
    try:
        #scroll down and click to a certain xpath
        driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/div[6]/div/button"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[6]/div/button"))))
        time.sleep(10)
    except NoSuchElementException or TimeoutException:
        #get the title and sort it
        name_list = driver.find_elements_by_class_name("list-bisnis-title")
        for names in name_list:
            container.append(names.text)
        new_container = list(set(container))
        for x in new_container:
            print(x)
        break
        
