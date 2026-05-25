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
        return self.driver.find_element(By.TAG_NAME, "header").is_displayed() or self.driver.find_element(By.CSS_SELECTOR, ".slide-menu__opener").is_displayed()
    
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

    # ==============================
    # HERO / BANNER
    # ==============================
    def hero_section_exists(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, "section")) > 0

    def hero_images(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "section img")

    # ==============================
    # FEATURED EVENTS
    # ==============================
    def featured_events_exists(self):
        return len(self.driver.find_elements(By.XPATH, "//h2[contains(text(),'Featured Events')]")) > 0

    def featured_events_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "section li")

    # ==============================
    # NEWS
    # ==============================
    def news_title_exists(self):
        return len(self.driver.find_elements(By.XPATH, "//h2[contains(text(),'News')]")) > 0

    def news_cards(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".article-teaser")

    # ==============================
    # LIFE AT CALTECH
    # ==============================
    def life_section_exists(self):
        return len(self.driver.find_elements(By.XPATH, "//h2[contains(text(),'Life at Caltech')]")) > 0

    def life_images(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "section img")

    # ==============================
    # SOCIAL / CONNECT
    # ==============================
    def social_icons(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "a svg")

    # ==============================
    # FOOTER
    # ==============================
    def footer_exists(self):
        return self.driver.find_element(By.TAG_NAME, "footer").is_displayed()

    def footer_links(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "footer a")

    # ==============================
    # LINKS GERAIS
    # ==============================
    def all_links(self):
        return self.driver.find_elements(By.TAG_NAME, "a")