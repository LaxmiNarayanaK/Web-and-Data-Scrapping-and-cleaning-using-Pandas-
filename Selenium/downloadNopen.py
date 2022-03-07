from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import csv
import pandas as pd
options=webdriver.ChromeOptions()

prefs = {'download.default_directory' : 'E:\Zigram\Selenium','safebrowsing.enabled': "false"}
# prefs = {
#     "download.default_directory":"E:\Zigram\Django-Projects\telusko\Data",
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "plugins.always_open_pdf_externally": True}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(service=Service(r"E:\Zigram\Selenium\chromedriver.exe"),options=options)

# driver.get("https://mbasic.facebook.com")
# driver.find_element(By.ID,"m_login_email").send_keys("laxminarayana33317@gmail.com")
# driver.find_element(By.NAME,"pass").send_keys("I'll always forget my FB Password")
# driver.find_element(By.NAME,"login").click()
# driver.find_element(By.LINK_TEXT,"Try Another Way").click()
# driver.find_element(By.XPATH,"//*[@id='contact_point_selector_form']/section/section[5]/table/tbody/tr/td[1]/label/div").click()
# driver.find_element(By.NAME,"reset_action").click()


driver.get("https://www.stats.govt.nz/large-datasets/csv-files-for-download/")
time.sleep(5)
# driver.find_element_by_id('accept-cookie-notification').click()


driver.find_element(By.XPATH,"//*[@id='main']/section/div/div/div/article/div/div[2]/article/ul/li[2]/div/div/h3/a").click()
# time.sleep(3)
# driver.get('chrome://downloads')

# fileName = "D:\\Zigram\\Selenium\\"+driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content #file-link').text")

# df=pd.read_csv(fileName)
# print(df.head(100))

    

