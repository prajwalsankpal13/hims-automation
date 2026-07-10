from pages.opd_page import OpdPage

def test_opd(logged_in_driver):
    opd = OpdPage(logged_in_driver)
    opd.click_opd()
    opd.click_new_opd()
    opd.click_search_and_select_patient("Balendra")
    opd.click_search_and_select_doc("Dr. Virendra Power")
    opd.click_date_today()
    opd.click_save()

