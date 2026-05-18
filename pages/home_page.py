from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:

    URL = "https://www.caltech.edu"
    def __init__(self, driver):
        self.driver = driver

    # ==============================
    # AÇÕES BÁSICAS
    # ==============================
    def open(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    # ==============================
    # MENU PRINCIPAL
    # ==============================
    def menu_exists(self):
        return self.driver.find_element(By.TAG_NAME, "header").is_displayed()
    
    def get_menu_items(self):
        # Pega itens do menu principal
        return self.driver.find_elements(By.CSS_SELECTOR, "header nav a")

    # ==============================
    # DROPDOWN (HOVER)
    # ==============================
    def hover_on_menu(self, index=0):
        # Hover no item do menu (pode variar dependendo do site)
        menu_items = self.get_menu_items()
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_items[index]).perform()

    def dropdown_visible(self):
        # Ajuste o seletor conforme o site real
        dropdowns = self.driver.find_elements(By.CSS_SELECTOR, "header nav ul")
        return any(d.is_displayed() for d in dropdowns)

    # ==============================
    # LOGO
    # ==============================
    def click_logo(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        wait = WebDriverWait(self.driver, 10)
        # pega o link que contém uma imagem dentro do header (logo real)
        logo = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//header//a[.//img]")
            )
        )
        # scroll até o elemento
        self.driver.execute_script("arguments[0].scrollIntoView();", logo)
        # clique seguro via JS
        self.driver.execute_script("arguments[0].click();", logo)