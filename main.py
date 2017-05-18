from selenium import webdriver



driver = webdriver.Chrome()

def login(name,pwd):
    driver.find_element_by_id("username").send_keys(name)
    driver.find_element_by_id("password").send_keys(pwd)
    driver.find_element_by_css_selector("button[type*='submit']").click()

driver.get("http://the-internet.herokuapp.com/")

driver.find_element_by_css_selector("a[href*='/login']").click()

login("tomsmith","SuperSecretPassword!")

driver.save_screenshot('test.png')

driver.quit()