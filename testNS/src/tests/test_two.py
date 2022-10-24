import logging


def test_two(pre_requisite):
    logging.info("Test Summary: Verify the app displays all the potential schedules with the default date and time")
    driver = pre_requisite
    xpath_from = "//android.widget.TextView[@bounds='[163,450][907,496]']"
    text_from = "Amsterdam Centraal"
    xpath_to = "//android.widget.TextView[@bounds='[163,567][907,613]']"
    text_to = "Almere Centrum"
    id_search = "nl.ns.android.activity:id/autoCompleteText"

    logging.info("Step1: Open NS App, Travel Planner Activity screen is displayed - Handled in test setup (pre_requisite)")
    logging.info("Step2: Enter any valid Source Location. For e.g.: Amsterdam Central")
    driver.find_element("xpath",xpath_from).click()
    driver.find_element("id",id_search).send_keys("amsterdam")
    driver.find_element("xpath",f"//android.widget.TextView[@content-desc='{text_from}']").click()
    assert driver.find_element("xpath",xpath_from).text == text_from

    logging.info("Step3: Enter any valid destination location. For e.g.: Almere Centrum")
    driver.find_element("xpath",xpath_to).click()
    driver.find_element("id",id_search).send_keys("almere")
    driver.find_element("xpath",f"//android.widget.TextView[@content-desc='{text_to}']").click()
    assert driver.find_element("xpath",xpath_to).text == text_to

    logging.info("Step4: Click on Plan your journey button")
    driver.find_element("xpath","//android.widget.Button[@bounds='[42,858][1038,984]']").click()
    result = driver.find_elements("xpath","//android.view.View")

    logging.info("Expected Result: Searched Results are not empty and potential journey options are displayed from source to destination.")
    assert len(result)>0
