from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date
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

def get_source():
    # Wait 30 seconds for page to load and extract the element after it loads
    timeout = 60
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='CaseCount_With_Cases_150420_4042_layer']")))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()
        return False

    today = date.today()
    # YYYYMMDD
    today_str = today.strftime("%Y%m%d")
    Html_file = open("source_html_"+today_str+".html", "w")
    Html_file.write(driver.page_source)
    Html_file.close()
    driver.close()
    return True
