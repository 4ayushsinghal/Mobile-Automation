import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def _check_footer_menu_options(driver):
    xpath_prefix = "//android.widget.TextView"
    elements_xpath = [
        f"{xpath_prefix}[@text='Plannen']",
        f"{xpath_prefix}[@text='Vertrektijden']",
        f"{xpath_prefix}[@text='In de buurt']",
        f"{xpath_prefix}[@text='Mijn reizen']",
        f"{xpath_prefix}[@text='Meer']",
        ]
    for ele in elements_xpath:
        assert WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.XPATH, ele))
            ), "Footer menu options not available"


def test_three(pre_requisite):
    logging.info("Test Summary: Verify the app lists all the footer menu options while switching to different Activity screens")
    driver = pre_requisite
    xpath_from = "//android.widget.TextView[@bounds='[163,450][907,496]']"
    text_from = "Amsterdam Centraal"
    xpath_to = "//android.widget.TextView[@bounds='[163,567][907,613]']"
    text_to = "Almere Centrum"
    id_search = "nl.ns.android.activity:id/autoCompleteText"

    logging.info("Step1: Open NS App, Travel Planner Activity screen is displayed-"
    "Handled in test setup (pre_requisite)")

    logging.info("Step2: Footer menu options are displayed.")
    _check_footer_menu_options(driver)

    logging.info("Step3: Enter any valid Source Location. For e.g.: Amsterdam Central")
    driver.find_element(MobileBy.XPATH,xpath_from).click()
    driver.find_element(MobileBy.ID,id_search).send_keys("amsterdam")
    driver.find_element(MobileBy.XPATH,f"//android.widget.TextView[@content-desc='{text_from}']").click()
    assert driver.find_element(MobileBy.XPATH,xpath_from).text == text_from

    logging.info("Step4: Enter any valid destination location. For e.g.: Almere Centrum")
    driver.find_element(MobileBy.XPATH,xpath_to).click()
    driver.find_element(MobileBy.ID,id_search).send_keys("almere")
    driver.find_element(MobileBy.XPATH,f"//android.widget.TextView[@content-desc='{text_to}']").click()
    assert driver.find_element(MobileBy.XPATH,xpath_to).text == text_to

    logging.info("Step5: Click on Plan your journey button")
    driver.find_element(MobileBy.XPATH,"//android.widget.Button[@bounds='[42,858][1038,984]']").click()
    result = driver.find_elements(MobileBy.XPATH,"//android.view.View")

    logging.info("The footer menu bar is displayed consistently with options:"
    "planner, departures,nearby me, my trips, and more on both pages.")
    _check_footer_menu_options(driver)
