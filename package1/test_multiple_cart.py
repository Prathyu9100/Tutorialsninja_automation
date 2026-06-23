import allure

from pages import HomePage
from pages import CartPage
from pages import ProceedPage
from selenium.webdriver.common.by import By
def test_correct_login(setup):
    driver = setup
    driver.implicitly_wait(3)
    home = HomePage.Home_Page(driver)
    cart = CartPage.Cart_Page(driver)
    order = CartPage.Place_order_page(driver)
    proceed = ProceedPage.Proceed_Page(driver)
    #Brocali
    home.increment_item("Brocolli - 1 Kg")
    home.add_to_cart("Brocolli - 1 Kg")
    print("adding Brocoli")
    #Cauliflower - 1 Kg
    home.add_to_cart("Cauliflower - 1 Kg")
    print("adding Cauliflower")
    home.bag_click()
    cart.checkout()
    product_list=order.click_cart_items()
    for p in product_list:
        print("Product in cart:", p.text)

    product_name=[]
    for p in product_list:
        name=p.text.split("-")[0].strip()
        product_name.append(name)
    assert "Cauliflower" in product_name
    assert "Brocolli" in product_name
