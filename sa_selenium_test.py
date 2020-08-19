from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://dev-1.clicktrans.pl/register-test/courier")

user_data_dict = {
       "user_register_company_name": "Test sp.zoo",
       "user_register_email": "test@test.com",
       "user_register_name": "John Smith",
       "user_register_phone": "12345678",
       "user_register_plainPassword": "12345678",
}

user_agreement_dict = {
       "agreement_regulations": "user_register_settings_agreementRegulations",
       "agreement_personal": "user_register_settings_agreementPersonalData",
       "agreement_marketing": "user_register_settings_agreementMarketing"
}


def enter_data_to_form():
       """
       basic checking of registration form
       """

       for ids, data in user_data_dict.items():
              k = driver.find_element_by_id(ids)
              k.send_keys(data)

       for mark, ids in user_agreement_dict.items():
              k = driver.find_element_by_id(ids)
              k.click()

       code = driver.find_element_by_xpath(
              "//select[@name='user_register[phoneCode]']/option[text()='(+48) Polska']")

       code.click()

       element = driver.find_element_by_id("user_register_submit")
       element.click()

       #driver.close()

enter_data_to_form()


def checking_all_phone_codes():
       """
       because of 'selenium.common.exceptions.InvalidSessionIdException: Message: invalid session id'
       function is not working properly.
       """
       element_phone_code = driver.find_elements(By.XPATH,'//select[@name="user_register[phoneCode]"]/option')

       for i in range(0, len(element_phone_code)):

              for ids, data in user_data_dict.items():
                     k = driver.find_element_by_id(ids)
                     k.send_keys(data)

              for mark, ids in user_agreement_dict.items():
                     k = driver.find_element_by_id(ids)
                     k.click()

              code = driver.find_element_by_xpath("//select[@name='user_register[phoneCode]']/option[text()='{0}']".format(element_phone_code[i].text))
              code.click()

              element = driver.find_element_by_id("user_register_submit")
              element.click()

              driver.close()

#checking_all_phone_codes()