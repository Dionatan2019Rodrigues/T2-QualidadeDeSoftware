from pages.home_page import HomePage

def test_homepage_loads(driver):
    home = HomePage(driver)
    home.open()

    assert "Caltech" in home.get_title()


def test_menu_visible(driver):
    home = HomePage(driver)
    home.open()

    assert home.menu_exists()