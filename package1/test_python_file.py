import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
@allure.severity(allure.severity_level.CRITICAL)
def test_correct_login(setup):
    driver = setup

    driver.implicitly_wait(3)  # Wait up to 10 seconds
    driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("potato")

    driver.find_element(By.CLASS_NAME,"increment").click()
    driver.find_element(By.XPATH,"//button[text()='ADD TO CART']").click()
    driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()
    driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
    driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
    driver.find_element(By.CLASS_NAME,"chkAgree").click()
    driver.find_element(By.XPATH,"//button[text()='Proceed']").click()
    expected_text=driver.find_element(By.XPATH,"//span[text()='Thank you, your order has been placed successfully ']").text
    print(expected_text)
    assert expected_text == "Thank you, your order has been placed successfully\nYou'll be redirected to Home page shortly!!"
    print(expected_text)
@allure.severity(allure.severity_level.BLOCKER)
def test_empty_login(setup):
    driver = setup
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()
    expected_text=driver.find_element(By.XPATH,"(//div[@class='empty-cart']//h2)[1]").text
    assert expected_text=="You cart is not empty!"



