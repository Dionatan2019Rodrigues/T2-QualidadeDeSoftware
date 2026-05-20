from selenium.webdriver.common.by import By

class DirectoryPage:

    URL = "https://directory.caltech.edu/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    # ==============================
    # BUSCA
    # ==============================
    def search_input(self):
        return self.driver.find_element(By.NAME, "query")

    def search_button(self):
        return self.driver.find_element(By.XPATH, "//input[@type='submit' or @value='Search']")

    def type_search(self, text):
        field = self.search_input()
        field.clear()
        field.send_keys(text)

    def click_search(self):
        self.search_button().click()