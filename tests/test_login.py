import time
import datetime


from selenium.webdriver.common.by import By

from Tutorialsninja_automation.tests.conftest import setup


def test_login_valid(setup):
    driver=setup
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    time.sleep(2) # implicit wait
    driver.find_element(By.LINK_TEXT,"Register").click()
    time.sleep(2)
    driver.find_element(By.NAME,"firstname").send_keys("John")
    driver.find_element(By.NAME,"lastname").send_keys("Smith")
    driver.find_element(By.NAME,"email").send_keys(time_current())
    driver.find_element(By.ID,"input-telephone").send_keys("12345")
    driver.find_element(By.ID,"input-password").send_keys("12345@abc")
    driver.find_element(By.ID,"input-confirm").send_keys("12345@abc")
    driver.find_element(By.NAME,"agree").click()
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    time.sleep(2)
    expected_output=driver.find_element(By.XPATH,"//div[@id='content']/h1").text
    print(expected_output)
    assert expected_output == "Your Account Has Been Created!"
    driver.quit()
def test_login_invalid(setup):
    driver=setup
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.NAME, "firstname").send_keys("John")
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(2)
    expected_Failure=driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text
    assert expected_Failure == "Warning: You must agree to the Privacy Policy!"
    time.sleep(3)
    driver.quit()
def time_current():
    return f"test{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}@gmail.com"




