from pages.ipd_page import IPDPage


def test_ipd_admission(logged_in_driver):
    ipd = IPDPage(logged_in_driver)
    ipd.click_IPD()
    ipd.click_admit()
    ipd.search_and_select_patient("prajwal")
    ipd.select_ward("Male General Ward")
    ipd.select_random_available_bed()
    ipd.select_admission_type("Emergency")  # confirm real option text
    ipd.select_admission_datetime_now()
    ipd.select_payment_type("self")
    ipd.submit_admission()