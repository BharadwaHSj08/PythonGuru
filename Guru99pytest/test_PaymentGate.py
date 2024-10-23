import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("broswer_invoke")

class TestPayment(BaseClass):

    def test_paymentGateway(self):
        self.driver.implicitly_wait(5)
        # Clicking on Paymentgateway
        gateway = self.driver.find_element(By.LINK_TEXT, "Payment Gateway Project")
        gateway.click()

        # Quantity selection
        item_quantity = "2"

        drop_down = Select(self.driver.find_element(By.XPATH, "//div/select[@name = 'quantity']"))
        drop_down.select_by_visible_text(item_quantity)
        # time.sleep(3)

        # click on Buy now
        self.driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

        # enter card number
        Card_number = "1234567891011121"
        self.driver.find_element(By.ID, "card_nmuber").send_keys(Card_number)

        month_selection = "3"
        month_select = Select(self.driver.find_element(By.ID, "month"))
        month_select.select_by_value(month_selection)

        year_slection = "2023"
        year_select = Select(self.driver.find_element(By.ID, "year"))
        year_select.select_by_value(year_slection)

       # Cvv
        cvv_code = "123"
        self.driver.find_element(By.ID, "cvv_code").send_keys(cvv_code)

        # submit
        self.driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

        if len(Card_number) < 16:
            alert_pop_up = self.driver.switch_to.alert
            alert_pop_up.accept()

        # final page
        payment_message = self.driver.find_element(By.TAG_NAME, "h2").text
        print(payment_message)

        order_id = self.driver.find_element(By.XPATH, "//td[2]/h3").text
        print("Order_ID:", order_id)