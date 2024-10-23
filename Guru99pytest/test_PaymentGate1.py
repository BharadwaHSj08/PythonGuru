import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.carddetails import Carddetails
from PageObject.finalpage import FinalPage
#from Guru99pytest.Baseclass import BaseClass
from PageObject.paymentclick import PaymentClick
from PageObject.selectitems import selectItems
from Utilities.BaseClass import BaseClass


class TestPayment(BaseClass):

    def test_paymentGateway(self):
        self.driver.implicitly_wait(5)

        # Clicking on Paymentgateway
        gateway = PaymentClick(self.driver)
        gateway.PaymentGatewayClick().click()

        # Quantity selection
        item_quantity = "2"
        items_count = selectItems(self.driver)
        drop_down = Select(items_count.itemsCount())
        drop_down.select_by_visible_text(item_quantity)

        # click on Buy now
        buying = items_count.clickonBuy()
        buying.click()

        # enter card number
        number_on_card = "1234567891011121"
        card_details = Carddetails(self.driver)
        card_details.Cardnumber().send_keys(number_on_card)

        month_selection = "3"
        month_select = Select(card_details.select_Month())
        month_select.select_by_value(month_selection)

        year_selection = "2023"
        year_select = Select(card_details.select_year())
        year_select.select_by_value(year_selection)

       # Cvv
        cvv_code = "123"
        card_details.CVV().send_keys(cvv_code)

        # submit
        card_details.Submit_Click().click()

        if len(number_on_card) < 16:
            alert_pop_up = self.driver.switch_to.alert
            alert_pop_up.accept()

        # final page
        #payment_message = self.driver.find_element(By.TAG_NAME, "h2").text
        payment_message = FinalPage(self.driver)
        payment_message.getMessagetext().text
        print(payment_message)

        #order_id = self.driver.find_element(By.XPATH, "//td[2]/h3").text
        order_id = payment_message.getOrderId().text
        print("Order_ID:", order_id)