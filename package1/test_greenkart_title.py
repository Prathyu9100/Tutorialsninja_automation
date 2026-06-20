from selenium import webdriver
from selenium.webdriver.common.by import By
def test_correct_login(setup):
    driver = setup
    driver.implicitly_wait(3)
    assert "GreenKart" in driver.title
    print(driver.title)
#to search particular element whether serch is showing correct or not
def test_search(setup):
    driver=setup
    driver.implicitly_wait(3)
    driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("cucumber")
    products=driver.find_elements(By.XPATH,"//div[@class='products']")
    assert len(products)==1
#check cart count
def test_cart_count(setup):
    driver = setup
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH,"//div[h4='Brocolli - 1 Kg']//button[text()='ADD TO CART']").click()
    cart_count=driver.find_element(By.XPATH,"(//div[@class='cart-info']//strong)[1]").text
    assert cart_count=="2"

