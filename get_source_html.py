from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/local/bin/chromedriver',
                          chrome_options=chrome_options)

driver.get(
    "https://doph.maps.arcgis.com/apps/opsdashboard/index.html#/f8fb4ccc3d2d42c7ab0590dbb3fc26b8")
print(driver.title)


# Wait 30 seconds for page to load and extract the element after it loads
timeout = 30
try:
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.ID, "ember8")))
except TimeoutException:
    print('Timed out waiting for page to load')
    driver.quit()

Html_file = open("source_html_2.html", "w")
Html_file.write(driver.page_source)
Html_file.close()
driver.close()
