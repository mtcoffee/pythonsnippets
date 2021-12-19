#A Simple Python/Selenium script to search Google and print the links from the results

#variables
searchterm = 'NY Pizza'

#selenium setup
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#chrome setup
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.google.com')

search = driver.find_element(By.NAME, "q")
search.send_keys(searchterm)
search.send_keys(Keys.RETURN) # hit return after you enter search text

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class = "g"]')))
results = driver.find_elements(By.XPATH,'//div[@class = "g"]')  # Heading elements

for result in results:
    link = result.find_element(By.CSS_SELECTOR,'.yuRUbf>a').get_attribute("href")  #
    print(link)

# close browser after our manipulations
driver.close()
