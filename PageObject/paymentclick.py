from selenium.webdriver.common.by import By


class PaymentClick:

    def __init__(self,driver):
        self.driver = driver

    click_on_payment=(By.LINK_TEXT,"Payment Gateway Project")
    #By.LINK_TEXT, "Payment Gateway Project"

    def PaymentGatewayClick(self):
        return self.driver.find_element(*PaymentClick.click_on_payment)