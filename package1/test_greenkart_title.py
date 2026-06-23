from selenium import webdriver
from selenium.webdriver.common.by import By

from pages import HomePage, CartPage, ProceedPage


def test_correct_login(setup):
    driver = setup
    driver.implicitly_wait(3)
    assert "GreenKart" in driver.title
    print(driver.title)
#to search particular element whether serch is showing correct or not
def test_search(setup):
    driver = setup
    home = HomePage.Home_Page(driver)
    home.search("cucumber")
    products=home.product_after_search()
    assert len(products)==1
#check cart count
def test_cart_count(setup):
    driver = setup
    home = HomePage.Home_Page(driver)
    home.add_to_cart("Brocolli - 1 Kg")
    cart_count=home.get_item_count()
    assert cart_count==1

