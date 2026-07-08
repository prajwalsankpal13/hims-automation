import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select


class Patient_Registration:

    F_NAME = (By.XPATH, "//input[@placeholder='First name']")
    L_NAME = (By.XPATH, "//input[@placeholder='Last name']")
    DOB = (By.XPATH, "//label[contains(text(),'Date of Birth')]/following::button[1]")
    MOB_NO = (By.XPATH, "//div[@class='rounded-xl border border-cu-border bg-white p-5 shadow-sm border-cu-border']//div[@class='flex flex-col gap-3']//div//div//input[@placeholder='9876543210']")
    GENDER = (By.XPATH, "//label[contains(text(),'Gender')]/following::select[1]")
    UPLOAD = (By.XPATH, "//input[@type='file']")
    VISIT_TYPE = (By.XPATH, "//label[contains(text(),'Visit Type')]/following::select[1]")
    PRE_DATE = (By.XPATH, "//label[contains(text(),'Preferred Date')]/following::button[1]")
    CHECKBOX = (By.XPATH, "(//input[@type='checkbox'])[1]")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

    TODAY_BUTTON = (By.XPATH, "//button[normalize-space()='Today']")

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.F_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.L_NAME).send_keys(last_name)

    def enter_mobile_no(self, mobile_no):
        self.driver.find_element(*self.MOB_NO).send_keys(mobile_no)

    def select_gender(self, gender):
        Select(self.driver.find_element(*self.GENDER)).select_by_visible_text(gender)

    def select_visit_type(self, visit_type):
        Select(self.driver.find_element(*self.VISIT_TYPE)).select_by_visible_text(visit_type)

    def select_dob_today(self):
        self.driver.find_element(*self.DOB).click()
        self.driver.find_element(*self.TODAY_BUTTON).click()

    def select_preferred_date_today(self):
        self.driver.find_element(*self.PRE_DATE).click()
        self.driver.find_element(*self.TODAY_BUTTON).click()

    def click_upload_file(self, file_path):
        upload_element = self.driver.find_element(*self.UPLOAD)
        upload_element.send_keys(file_path)

    def check_verify_checkbox(self):
        checkbox = self.driver.find_element(*self.CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT).click()
        time.sleep(3)