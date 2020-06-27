from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

print("DTG format = YYYY-MM-DD HH:MM")
dateTime = input("Enter the DTG group to search for: ")

driver.get("https://ssd.jpl.nasa.gov/sbwobs.cgi")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='time']"))).click()
timeElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='obs_time']")))
timeElement.click()
timeElement.clear()
timeElement.send_keys(dateTime)
driver.find_element_by_css_selector("input[name='check_time']").click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='loc']"))).click()
locElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='l_str']")))
locElement.click()
locElement.clear()
locElement.send_keys("Las Palmas")
driver.find_element_by_css_selector("input[name='s_lookup']").click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='constraint']"))).click()
magElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='mag_limit']")))
zenithElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='max_zd']")))
zenithElement.click()
zenithElement.clear()
magElement.click()
magElement.clear()
magElement.send_keys("20")
driver.find_element_by_xpath("//select/option[@value='0']").click() # set to 0 for unlimited
driver.find_element_by_css_selector("input[name='check_constraints']").click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))).click()

time.sleep(60)
WebDriverWait(driver, 600).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

observableFile = open(f"Observable at {dateTime}.txt", 'w+')
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))
    observableFile.write(elem.get_attribute("href"))
    observableFile.write("\n")

print("Finished!")
observableFile.close()

