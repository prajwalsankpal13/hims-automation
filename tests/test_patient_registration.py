import re
from faker import Faker

from pages.dashboard_page import DashboardPage
from pages.patient_registration_page import Patient_Registration

fake = Faker("en_IN")


def test_patient_registration(logged_in_driver):
    dashboard = DashboardPage(logged_in_driver)
    dashboard.click_new_registration()

    first_name = fake.first_name()
    last_name = fake.last_name()
    mobile = re.sub(r'\D', '', fake.phone_number())[-10:]

    registration = Patient_Registration(logged_in_driver)
    registration.enter_first_name(first_name)
    registration.enter_last_name(last_name)
    registration.enter_mobile_no(mobile)
    registration.select_gender("Male")
    registration.select_visit_type("OPD — New Visit")  # em dash — confirm this matches exactly
    registration.select_dob_today()
    registration.select_preferred_date_today()
    registration.click_upload_file(r"E:\superman modi.jpg")
    registration.select_department("General Surgery")
    registration.select_doctor("Dr. Reshma — General Medicine")
    registration.check_verify_checkbox()
    registration.click_submit()