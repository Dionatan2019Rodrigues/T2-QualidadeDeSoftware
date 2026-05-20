from selenium.webdriver.common.by import By

class LoginPage:

    URL = "https://access.caltech.edu/auth/login?service=https://access.caltech.edu/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    # ==============================
    # CAMPOS DE LOGIN
    # ==============================
    def username_input(self):
        return self.driver.find_element(By.ID, "username")

    def password_input(self):
        return self.driver.find_element(By.ID, "password")

    def login_button(self):
        return self.driver.find_element(By.NAME, "Sign In")

    # ==============================
    # AÇÕES
    # ==============================
    def type_username(self, text):
        self.username_input().send_keys(text)

    def type_password(self, text):
        self.password_input().send_keys(text)

    def submit_login(self):
        self.login_button().click()