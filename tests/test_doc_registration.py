import re
import random
from faker import Faker
from pages.doc_registration_page import DocRegistrationPage

fake = Faker("en_IN")


def test_add_doctor(logged_in_driver):
    doctor_name = f"Dr. {fake.first_name()} {fake.last_name()}"
    reg_no = f"MCI-{random.randint(10000, 99999)}"
    phone = re.sub(r'\D', '', fake.phone_number())[-10:]

    doc_page = DocRegistrationPage(logged_in_driver)
    doc_page.click_doc()
    doc_page.click_add_doc()

    doc_page.enter_name(doctor_name)
    doc_page.enter_reg_no(reg_no)
    doc_page.enter_phone(phone)

    doc_page.click_schedule()
    doc_page.select_working_days(["Monday", "Wednesday", "Friday"])

    doc_page.click_fee()
    doc_page.enter_new_visit_fee(500)
    doc_page.enter_followup_fee(200)
    doc_page.enter_emergency_fee(1000)

    doc_page.click_save()