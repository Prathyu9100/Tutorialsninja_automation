import pytest
from selenium import webdriver

@pytest.fixture()
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

    yield driver

    driver.quit()