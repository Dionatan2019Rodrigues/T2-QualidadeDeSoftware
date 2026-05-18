from pages.home_page import HomePage


# ==============================
# TESTE 1: MENU PRINCIPAL VISÍVEL
# ==============================
def test_menu_visible(driver):
    home = HomePage(driver)
    home.open()

    assert home.menu_exists()

# ==============================
# TESTE 2: ITENS DO MENU EXISTEM
# ==============================
def test_menu_items_present(driver):
    home = HomePage(driver)
    home.open()

    menu_items = home.get_menu_items()

    # valida que existem itens no menu
    assert len(menu_items) > 0

    # opcional: validar texto de alguns itens
    textos = [item.text for item in menu_items]

    assert any("About" in t for t in textos)
    assert any("Research" in t for t in textos)

# ==============================
# TESTE 3: DROPDOWN FUNCIONA (HOVER)
# ==============================
def test_dropdown_opens_on_hover(driver):
    home = HomePage(driver)
    home.open()

    # hover no primeiro item do menu
    home.hover_on_menu(0)

    # valida se dropdown apareceu
    assert home.dropdown_visible()

# ==============================
# TESTE 4: LOGO REDIRECIONA PARA HOME
# ==============================
def test_logo_redirects_home(driver):
    home = HomePage(driver)
    home.open()

    home.click_logo()

    assert "caltech.edu" in driver.current_url