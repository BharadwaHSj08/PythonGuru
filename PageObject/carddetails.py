from selenium.webdriver.common.by import By


class Carddetails:

    def __init__(self,driver):
        self.driver = driver


    card_number = (By.ID,"card_nmuber")

    month = (By.ID,"month")

    year = (By.ID,"year")

    cvv = (By.ID,"cvv_code")

    submit = (By.XPATH,"//input[@type = 'submit']")

    def Cardnumber(self):
        return self.driver.find_element(*Carddetails.card_number)

    def select_Month(self):
        return self.driver.find_element(*Carddetails.month)

    def select_year(self):
        return self.driver.find_element(*Carddetails.year)

    def CVV(self):
        return self.driver.find_element(*Carddetails.cvv)

    def Submit_Click(self):
        return self.driver.find_element(*Carddetails.submit)

