from selenium.webdriver.common.by import By

class HomePage:

    URL = "https://www.caltech.edu"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def menu_exists(self):
        return self.driver.find_element(By.TAG_NAME, "header").is_displayed()