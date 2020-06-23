from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()

browser.get("https://ssd.jpl.nasa.gov/sbwobs.cgi")

browser.find_element_by_css_selector("a[href*='time']").click()
browser.find_element_by_name('obs_time').send_keys("2021-04-01 01:00")
browser.find_element_by_name('check_time').submit()