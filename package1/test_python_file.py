import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import logger
from pages import HomePage
from pages import CartPage
from pages import ProceedPage
from utilities.logger import LogGenerator
logger=LogGenerator.loggen()

@allure.severity(allure.severity_level.CRITICAL)
def test_correct_login(setup):
    driver = setup
    home = HomePage.Home_Page(driver)
    cart = CartPage.Cart_Page(driver)
    order=CartPage.Place_order_page(driver)
    proceed=ProceedPage.Proceed_Page(driver)

    driver.implicitly_wait(3)
    home.search("potato")
    logger.info("Searching for potato")
    home.increment_item("Potato - 1 Kg")
    home.add_to_cart("Potato - 1 Kg")
    logger.info("Adding potato to cart")
    home.bag_click()
    logger.info("check the items in bag")
    cart.checkout()
    order.click_to_place_order()
    proceed.click_to_check_agree()
    proceed.click_to_proceed_order()
    expected_text=proceed.click_to_confirmatin_text()
    logger.info("order placed")
    assert expected_text == "Thank you, your order has been placed successfully\nYou'll be redirected to Home page shortly!!"

@allure.severity(allure.severity_level.BLOCKER)
def test_empty_login(setup):
    driver = setup
    home = HomePage.Home_Page(driver)
    cart = CartPage.Cart_Page(driver)
    home.open_cart()
    expected_text = cart.empty_cart()
    assert expected_text == "You cart is empty!"



