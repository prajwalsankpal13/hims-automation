from selenium import webdriver
from pages.login_page import LoginPage
import time

def test_login_page():
    driver = webdriver.Chrome()
    driver.get("https://aster.careup.ai/login")
    driver.maximize_window()

    login = LoginPage(driver)
    login.enter_email("admin@aster.com")
    login.enter_password("Aster@2025")
    login.click_login()
    assert login.is_dashboard_loaded()


    driver.quit()