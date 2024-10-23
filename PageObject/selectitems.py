from selenium.webdriver.common.by import By


class selectItems:

    def __init__(self,driver):
        self.driver = driver


    number_of_items = (By.XPATH,"//div/select[@name = 'quantity']")
    #self.driver.find_element(By.XPATH, "//div/select[@name = 'quantity']")

    buying = (By.XPATH, "//input[@type = 'submit']")

    def itemsCount(self):
        return self.driver.find_element(*selectItems.number_of_items)

    def clickonBuy(self):
        return self.driver.find_element(*selectItems.buying)