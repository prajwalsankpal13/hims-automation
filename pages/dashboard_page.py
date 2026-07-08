from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class DashboardPage:
    NEW_REGISTRATION = (By.XPATH,"//a[@href='/dashboard/patients/new']")

    def __init__(self,driver):
        self.driver = driver

    def is_dashboard_loaded(self):
        WebDriverWait(self.driver, 10).until(ec.url_contains("dashboard"))
        return "dashboard" in self.driver.current_url

    def click_new_registration(self):
        WebDriverWait(self.driver,10).until(
         ec.element_to_be_clickable(self.NEW_REGISTRATION)
        ).click()
        WebDriverWait(self.driver,10).until(ec.url_contains("patients/new"))

    def is_new_patient_page_loaded(self):
        return "patients/new" in self.driver.current_url