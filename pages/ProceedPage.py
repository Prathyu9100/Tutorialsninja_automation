from selenium.webdriver.common.by import By


class Proceed_Page:
    def __init__(self,driver):
        self.driver=driver
        self.check_agree=(By.CLASS_NAME, "chkAgree")
        self.proceed=(By.XPATH, "//button[text()='Proceed']")
        self.confirmatin_text=(By.XPATH,"//span[text()='Thank you, your order has been placed successfully ']")

        # ---------------- ACTION METHODS ----------------

    def click_to_check_agree(self):
        self.driver.find_element(*self.check_agree).click()
    def click_to_proceed_order(self):
        self.driver.find_element(*self.proceed).click()
    def click_to_confirmatin_text(self):
        return self.driver.find_element(*self.confirmatin_text).text






