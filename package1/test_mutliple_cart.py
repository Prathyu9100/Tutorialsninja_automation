import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_correct_login(setup):
    driver = setup
    driver.implicitly_wait(3)
    #Brocali
    driver.find_element(By.XPATH,"//div[h4='Brocolli - 1 Kg']//a[@class='increment']").click()
    driver.find_element(By.XPATH,"//div[h4='Brocolli - 1 Kg']//button[text()='ADD TO CART']").click()
    #Cauliflower - 1 Kg
    driver.find_element(By.XPATH,"//div[h4='Cauliflower - 1 Kg']//div[@class='product-action']//button").click()
    driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
    driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
    product_list=driver.find_elements(By.XPATH,"//td[p[@class='product-name']]")
    product_name=[]
    for p in product_list:
        name=p.text.split("-")[0].strip()
        product_name.append(name)
    assert "Cauliflower" in product_name
    assert "Brocolli" in product_name
    driver.quit()