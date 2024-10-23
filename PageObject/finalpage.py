from selenium.webdriver.common.by import By

class FinalPage:

    def __init__(self,driver):
        self.driver = driver

    message_text = (By.TAG_NAME,"h2")
    #payment_message = self.driver.find_element(By.TAG_NAME, "h2").text

    #order_id = self.driver.find_element(By.XPATH, "//td[2]/h3").text
    order_number = (By.XPATH,"//td[2]/h3")

    def getMessagetext(self):
        return self.driver.find_element(*FinalPage.message_text)

    def getOrderId(self):
        return self.driver.find_element(*FinalPage.order_number)

