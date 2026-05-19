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

# ==============================
# TESTE 5: SEÇÃO DE HERO EXISTE
# ==============================
def test_hero_section_exists(driver):
    home = HomePage(driver)
    home.open()

    assert home.hero_section_exists()

# ==============================
# TESTE 6: SEÇÃO DE HERO CONTÉM IMAGENS
# ==============================
def test_hero_has_images(driver):
    home = HomePage(driver)
    home.open()

    assert len(home.hero_images()) > 0

# ==============================
# TESTE 7: SEÇÃO DE EVENTOS DESTACADOS EXISTE
# ==============================
def test_featured_events_section_exists(driver):
    home = HomePage(driver)
    home.open()

    assert home.featured_events_exists()

# ==============================
# TESTE 8: SEÇÃO DE EVENTOS DESTACADOS CONTÉM ITENS
# ==============================
def test_featured_events_has_items(driver):
    home = HomePage(driver)
    home.open()

    assert len(home.featured_events_items()) > 0

# ==============================
# TESTE 9: SEÇÃO DE NOTÍCIAS EXISTE
# ==============================
def test_news_section_exists(driver):
    home = HomePage(driver)
    home.open()

    assert home.news_title_exists()

# ==============================
# TESTE 10: SEÇÃO DE NOTÍCIAS CONTÉM ARTIGOS
# ==============================
def test_news_has_articles(driver):
    home = HomePage(driver)
    home.open()

    assert len(home.news_cards()) > 0

# ==============================
# TESTE 11: SEÇÃO DE LIFE AT CALTECH EXISTE
# ==============================
def test_life_section_exists(driver):
    home = HomePage(driver)
    home.open()

    assert home.life_section_exists()

# ==============================
# TESTE 12: SEÇÃO DE LIFE AT CALTECH CONTÉM IMAGENS
# ==============================
def test_life_section_has_images(driver):
    home = HomePage(driver)
    home.open()

    assert len(home.life_images()) > 0

# ==============================
# TESTE 13: ÍCONES DE MÍDIA SOCIAL EXISTEM
# ==============================
def test_social_icons_exist(driver):
    home = HomePage(driver)
    home.open()

    assert len(home.social_icons()) > 0