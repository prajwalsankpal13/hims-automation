# HIMS Automation

Selenium + Pytest automation for the Careup.ai HIMS platform (Tenant Admin role),
using the Page Object Model (POM).

## Project Structure

HIMS Automation/
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── patient_registration_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_dashboard.py
│   └── test_patient_registration.py
├── requirements.txt
└── README.md

## Setup

1. Create and activate a virtual environment:
   python -m venv .venv
   .venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Make sure Chrome is installed and matches your ChromeDriver version.

## Running Tests

Run all tests:
   pytest tests/ -v

Run a specific module:
   pytest tests/test_login.py -v
   pytest tests/test_dashboard.py -v
   pytest tests/test_patient_registration.py -v

## How It's Structured

- pages/ — one class per page of the app, holding locators and actions for that page only.
- tests/ — one file per module/flow, importing whichever page objects it needs.
- conftest.py — shared logged_in_driver fixture: launches Chrome, logs in, and confirms
  the dashboard loaded, so tests can start right past login.

## Adding a New Module

1. Add a new page class in pages/ with that page's locators + actions.
2. Add a new test_<module>.py in tests/, using logged_in_driver to skip past login.
3. Commit and push once that module's tests pass.