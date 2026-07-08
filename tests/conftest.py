# tests/conftest.py
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def logged_in_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://aster.careup.ai/login")

    login = LoginPage(driver)
    login.enter_email("admin@aster.com")
    login.enter_password("Aster@2025")
    login.click_login()

    dashboard = DashboardPage(driver)
    dashboard.is_dashboard_loaded()  # wait until dashboard confirmed

    yield driver
    driver.quit()