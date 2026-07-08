from selenium import webdriver
from pages.dashboard_page import DashboardPage


def test_navigate_to_new_patient_form(logged_in_driver):
    dashboard = DashboardPage(logged_in_driver)
    dashboard.click_new_registration()
    assert dashboard.is_new_patient_page_loaded()