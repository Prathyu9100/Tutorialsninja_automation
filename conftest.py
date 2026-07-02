import pytest
from selenium import webdriver
import allure
from utilities.config import URL

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def setup(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    elif browser=="edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome=yield
    report=outcome.get_result()
    if report.when=="call" and report.outcome=="failed":
        driver=item.funcargs["setup"]
        allure.attach(
            driver.get_screenshot_as_png())