from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from datetime import datetime


class IPDPage:

    IPD = (By.XPATH, "//span[contains(text(),'IPD – Inpatient')]")
    ADMIT_PAT = (By.XPATH, "//a[normalize-space()='Admit Patient']")
    PATIENT = (By.XPATH, "//input[@placeholder='Search by name, UHID, or phone…']")
    ADMISSION_TYPE = (By.XPATH, "//label[contains(text(),'Admission Type')]/following::select[1]")
    ADMISSION_DATETIME = (By.XPATH, "//input[@type='datetime-local']")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def click_IPD(self):
        self.driver.find_element(*self.IPD).click()

    def click_admit(self):
        self.driver.find_element(*self.ADMIT_PAT).click()

    def search_and_select_patient(self, patient_name):
        self.driver.find_element(*self.PATIENT).send_keys(patient_name)
        time.sleep(1.5)
        result = self.driver.find_element(
            By.XPATH,
            f"//div[@class='cursor-pointer border-b border-cu-border px-3 py-2.5 hover:bg-cu-bg'][contains(.,'{patient_name}')]"
        )
        result.click()

    def select_ward(self, ward_name):
        self.driver.find_element(
            By.XPATH,
            f"//button[.//*[contains(text(),'{ward_name}')]]"
        ).click()
        time.sleep(1)

    def select_random_available_bed(self):
        available_beds = self.driver.find_elements(
            By.XPATH,
            "//button[.//span[normalize-space()='Available']]"
        )
        if not available_beds:
            raise Exception("No available beds found in this ward")
        random.choice(available_beds).click()

    def select_admission_type(self, admission_type):
        Select(self.driver.find_element(*self.ADMISSION_TYPE)).select_by_visible_text(admission_type)

    def select_payment_type(self, payment_value):
        radio = self.driver.find_element(By.XPATH, f"//input[@value='{payment_value}']")
        if not radio.is_selected():
            radio.click()

    def select_admission_datetime_now(self):
        date_field = self.driver.find_element(*self.ADMISSION_DATETIME)
        now = datetime.now().strftime("%m%d%Y%H%M")
        date_field.send_keys(now)

    def submit_admission(self):
        submit_btn = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].click();", submit_btn)
        time.sleep(3)