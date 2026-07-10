import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpdPage:

    OPD = (By.XPATH, "//span[contains(text(),'OPD – Outpatient')]")
    CLICK_NEW_OPD = (By.XPATH, "//a[@href='/dashboard/opd/appointments/new']")
    PATIENT_SEARCH = (By.XPATH, "//input[@placeholder='Search by name, UHID, or phone…']")
    DOC_SEARCH = (By.XPATH, "//input[@placeholder='Search by name or specialization…']")
    DATE = (By.XPATH, "//span[@class='flex-1 text-cu-text']")
    SAVE = (By.XPATH, "//button[normalize-space()='Confirm Booking']")
    TODAY_BTN = (By.XPATH, "//button[normalize-space()='Today']")

    def __init__(self, driver):
        self.driver = driver

    def click_opd(self):
        self.driver.find_element(*self.OPD).click()
        time.sleep(1)

    def click_new_opd(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLICK_NEW_OPD)
        ).click()

    def click_search_and_select_patient(self, patient_name):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PATIENT_SEARCH)
        )
        search_box.send_keys(patient_name)
        time.sleep(1.5)
        result = self.driver.find_element(
            By.XPATH,
            f"//div[@class='flex cursor-pointer items-center gap-3 border-b border-cu-border px-3 py-2.5 hover:bg-cu-bg'][contains(.,'{patient_name}')]"
        )
        result.click()

    def click_search_and_select_doc(self, doc_name):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DOC_SEARCH)
        )
        search_box.send_keys(doc_name)
        time.sleep(1.5)
        result = self.driver.find_element(
            By.XPATH,
            f"//div[@class='space-y-4 rounded-lg border border-cu-border bg-white p-4']//div//div[@class='flex cursor-pointer items-center gap-3 border-b border-cu-border px-3 py-2.5 hover:bg-cu-bg'][contains(.,'{doc_name}')]"
        )
        result.click()

    def click_date_today(self):
        self.driver.find_element(*self.DATE).click()
        self.driver.find_element(*self.TODAY_BTN).click()

    def click_save(self):
        save_button = self.driver.find_element(*self.SAVE)
        self.driver.execute_script("arguments[0].click();", save_button)