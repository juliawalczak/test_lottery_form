# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
import kinder_data

class Kinder(unittest.TestCase):
        def setUp(self):
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
                self.driver.get("https://kinderbueno.pl/loteria/")
                self.driver.implicitly_wait(10)
        def tearDown(self):
                self.driver = quit()
        def test_blank_field(self):
                driver = self.driver
                name = driver.find_element_by_xpath('//input[@data-ga-event="loteriaNameInsert"]')
                name.send_keys(kinder_data.name)
                surname = driver.find_element_by_name('surname')
                surname.send_keys(kinder_data.surname)
                telephone = driver.find_element_by_name('PhoneNumber')
                telephone.send_keys(kinder_data.telephone)
                email = driver.find_element_by_xpath('//input[@data-ga-event="loteriaEmailInsert"]')
                email.send_keys(kinder_data.email)
                code = driver.find_element_by_xpath('//input[@data-ga-event="loteriaCaptchaInsert"]')
                code.send_keys(kinder_data.code)
                agreement1 = driver.find_element_by_id('agreement1')
                agreement1.click()
                agreement2 = driver.find_element_by_id('agreement2')
                agreement2.click()
                agreement3 = driver.find_element_by_id('agreement3')
                agreement3.click()
                agreement4 = driver.find_element_by_id('agreement4')
                agreement4.click()
                agreement5 = driver.find_element_by_id('agreement5')
                agreement5.click()
                registration = driver.find_element_by_id('registrationForm')
                registration.click()
                error_notice = driver.find_element_by_id('alert-modal')
                assert error_notice.is_displayed()
                self.assertEqual(error_notice.get_atribute('innerText'),u"Błąd! Kod z wnętrza opakowania: Ta wartość nie powinna być pusta.")

                time.sleep(5)

if __name__ == '__main__':
        unittest.main(verbosity=2)
