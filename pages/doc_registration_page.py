import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select

class DocRegistrationPage:

    DOC=(By.XPATH,"//span[normalize-space()='Doctors']")
    ADD_DOC=(By.XPATH,"//button[normalize-space()='Add Doctor']")
    NAME=(By.XPATH,"//input[@placeholder='Dr. Firstname Lastname']")
    REG_NO=(By.XPATH,"//input[@placeholder='MCI-12345']")
    PHONE=(By.XPATH,"//input[@placeholder='9876543210']")
    SCHEDULE=(By.XPATH,"//button[normalize-space()='Schedule']")
    FEES=(By.XPATH,"//button[normalize-space()='Fees']")
    SUBMIT=(By.XPATH,"//button[@class='flex items-center gap-2 rounded-lg px-6 py-2 text-sm font-bold text-white transition-colors bg-cu-green hover:bg-cu-green-dark cursor-pointer']")

    def __init__(self,driver):
        self.driver = driver

    def click_doc(self):
       self.driver.find_element(*self.DOC).click()

    def click_add_doc(self):
        self.driver.find_element(*self.ADD_DOC).click()

    def enter_name(self,text):
        self.driver.find_element(*self.NAME).send_keys(text)

    def enter_phone(self,number):
        self.driver.find_element(*self.PHONE).send_keys(number)

    def enter_reg_no(self,number):
        self.driver.find_element(*self.REG_NO).send_keys(number)

    def click_schedule(self):
        self.driver.find_element(*self.SCHEDULE).click()

    def click_day_checkbox(self, day_name):
        checkbox = self.driver.find_element(
            By.XPATH,
            f"//span[contains(text(),'{day_name.lower()}')]/preceding-sibling::input[@type='checkbox']"
        )
        if not checkbox.is_selected():
            checkbox.click()

    def select_working_days(self, day_names):
        for day in day_names:
            self.click_day_checkbox(day)

    def click_fee(self):
        self.driver.find_element(*self.FEES).click()

    def _enter_fee(self, label_text, amount):
        fee_input = self.driver.find_element(
            By.XPATH,
            f"//*[contains(text(),'{label_text}')]/ancestor::div[contains(@class,'rounded-lg')][1]//input[@type='number']"
        )
        fee_input.clear()
        fee_input.send_keys(str(amount))

    def enter_new_visit_fee(self, amount):
        self._enter_fee("New Visit", amount)

    def enter_followup_fee(self, amount):
        self._enter_fee("Follow-up", amount)

    def enter_emergency_fee(self, amount):
        self._enter_fee("Emergency", amount)

    def click_save(self):
        self.driver.find_element(*self.SUBMIT).click()