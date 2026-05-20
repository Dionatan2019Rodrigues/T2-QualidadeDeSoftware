from pages.home_page import HomePage
from selenium.webdriver.common.by import By

# ==============================
# TESTE 1: MENU PRINCIPAL
# Verifica se o menu existe e se possui itens visíveis com textos esperados
# ==============================
def test_menu(driver):
    home = HomePage(driver)
    home.open()

    # Verifica se o header (menu) está visível
    assert home.menu_exists()

    # Verifica se existem itens no menu
    menu_items = home.get_menu_items()
    assert len(menu_items) > 0

    # Valida se alguns textos esperados aparecem no menu
    textos = [item.text for item in menu_items]
    assert any("About" in t for t in textos)
    assert any("Research" in t for t in textos)


# ==============================
# TESTE 2: DROPDOWN
# Verifica se o dropdown do menu aparece ao passar o mouse (hover)
# ==============================
def test_dropdown(driver):
    home = HomePage(driver)
    home.open()

    # Simula hover no primeiro item do menu
    home.hover_on_menu(0)

    # Verifica se algum dropdown ficou visível
    assert home.dropdown_visible()


# ==============================
# TESTE 3: LOGO
# Verifica se o clique no logo redireciona para a homepage
# ==============================
def test_logo(driver):
    home = HomePage(driver)
    home.open()

    # Clica no logo
    home.click_logo()

    # Verifica se a URL contém o domínio principal
    assert "caltech.edu" in driver.current_url


# ==============================
# TESTE 4: HERO
# Verifica se a seção principal (hero) existe e possui imagens
# ==============================
def test_hero_section(driver):
    home = HomePage(driver)
    home.open()

    # Verifica existência da seção hero
    assert home.hero_section_exists()

    # Verifica se há imagens dentro da seção
    assert len(home.hero_images()) > 0


# ==============================
# TESTE 5: FEATURED EVENTS
# Verifica se a seção de eventos destacados existe e contém itens
# ==============================
def test_featured_events(driver):
    home = HomePage(driver)
    home.open()

    # Verifica existência da seção
    assert home.featured_events_exists()

    # Verifica se há eventos listados
    assert len(home.featured_events_items()) > 0


# ==============================
# TESTE 6: NEWS
# Verifica se a seção de notícias existe e contém cards/artigos
# ==============================
def test_news(driver):
    home = HomePage(driver)
    home.open()

    # Verifica título da seção de notícias
    assert home.news_title_exists()

    # Verifica se há notícias listadas
    assert len(home.news_cards()) > 0


# ==============================
# TESTE 7: LIFE AT CALTECH
# Verifica se a seção "Life at Caltech" existe e possui imagens
# ==============================
def test_life_section(driver):
    home = HomePage(driver)
    home.open()

    # Verifica existência da seção
    assert home.life_section_exists()

    # Verifica se há imagens nessa seção
    assert len(home.life_images()) > 0


# ==============================
# TESTE 8: SOCIAL ICONS
# Verifica se os ícones de redes sociais estão presentes
# ==============================
def test_social_icons(driver):
    home = HomePage(driver)
    home.open()

    # Verifica se existem ícones sociais
    assert len(home.social_icons()) > 0


# ==============================
# TESTE 9: FOOTER
# Verifica se o rodapé existe e contém links
# ==============================
def test_footer(driver):
    home = HomePage(driver)
    home.open()

    # Verifica existência do rodapé
    assert home.footer_exists()

    # Verifica se há links no rodapé
    assert len(home.footer_links()) > 0


# ==============================
# TESTE 10: LINKS GERAIS
# Verifica se a página possui links (<a>)
# ==============================
def test_page_links(driver):
    home = HomePage(driver)
    home.open()

    # Verifica se existem links na página
    assert len(home.all_links()) > 0


# ==============================
# TESTE 11: IMAGENS
# Verifica se a página possui imagens (<img>)
# ==============================
def test_page_images(driver):
    home = HomePage(driver)
    home.open()

    images = driver.find_elements(By.TAG_NAME, "img")
    assert len(images) > 0


# ==============================
# TESTE 12: SECTIONS
# Verifica se a página possui seções (<section>)
# ==============================
def test_page_sections(driver):
    home = HomePage(driver)
    home.open()

    sections = driver.find_elements(By.TAG_NAME, "section")
    assert len(sections) > 0


# ==============================
# TESTE 13: BOTÕES
# Verifica se a página possui botões (<button>)
# ==============================
def test_page_buttons(driver):
    home = HomePage(driver)
    home.open()

    buttons = driver.find_elements(By.TAG_NAME, "button")
    assert len(buttons) > 0


# ==============================
# TESTE 14: TÍTULO
# Verifica se o título da página não está vazio
# ==============================
def test_page_title(driver):
    home = HomePage(driver)
    home.open()

    assert home.get_title() != ""