import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage:

    EMAIL= (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SIGN_IN = (By.XPATH,"//button[normalize-space()='Sign In']")

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_field=WebDriverWait(self.driver,10).until(
            ec.visibility_of_element_located(self.EMAIL,)
        )
        email_field.send_keys(email)
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.SIGN_IN).click()

    def is_dashboard_loaded(self):
        WebDriverWait(self.driver, 10).until(ec.url_contains("dashboard"))
        return "dashboard" in self.driver.current_url