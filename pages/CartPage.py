from selenium.webdriver.common.by import By


class Cart_Page:
    def __init__(self,driver):
        self.driver=driver
        self.checkout_button=(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']")
        self.empty_cart_text=(By.XPATH,"(//div[@class='empty-cart']//h2)[1]")

        # ---------------- ACTION METHODS ----------------

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
    def empty_cart(self):
        return self.driver.find_element(*self.empty_cart_text).text



class Place_order_page:
    def __init__(self,driver):
        self.driver=driver
        self.cart_items = (By.XPATH, "//div[@class='products']//p[@class='product-name']")
        self.place_order=(By.XPATH,"//button[text()='Place Order']")

        # ---------------- ACTION METHODS ----------------

    def click_cart_items(self):
        return self.driver.find_elements(*self.cart_items)
    def click_to_place_order(self):
        self.driver.find_element(*self.place_order).click()

