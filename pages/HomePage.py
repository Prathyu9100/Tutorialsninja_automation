from selenium.webdriver.common.by import By


class Home_Page:

    def __init__(self, driver):
        self.driver = driver

        # static locators only
        self.search_textbox = (By.CLASS_NAME, "search-keyword")
        self.bag_icon = (By.XPATH,"//a[@class='cart-icon']")
        self.count_items = (By.XPATH, "//div[@class='cart-info']//td[text()='Items']/following-sibling::td[2]/strong")
        self.productsaftersearch=(By.XPATH,"//div[@class='products']")
    # ---------------- ACTION METHODS ----------------
    def bag_click(self):
        self.driver.find_element(*self.bag_icon).click()

    def search(self, search_text):
        self.driver.find_element(*self.search_textbox).send_keys(search_text)

    def add_to_cart(self, product_name):
        self.driver.find_element(
            By.XPATH,
            f"//h4[text()='{product_name}']/parent::div//button[text()='ADD TO CART']").click()

    def increment_item(self, product_name):
        self.driver.find_element(
            By.XPATH,
            f"//h4[text()='{product_name}']/parent::div//a[@class='increment']"
        ).click()

    def decrement_item(self, product_name):
        self.driver.find_element(
            By.XPATH,
            f"//h4[text()='{product_name}']/parent::div//a[@class='decrement']"
        ).click()

    def open_cart(self):
        self.driver.find_element(*self.bag_icon).click()

    def get_item_count(self):
        return self.driver.find_element(*self.count_items).text

    def product_after_search(self):
        return self.driver.find_elements(*self.productsaftersearch)