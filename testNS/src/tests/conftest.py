import os

import pytest
from appium import webdriver


@pytest.fixture(scope='module')
def pre_requisite():
    """
    Desired Capabilities
    """
    app_path = os.path.abspath("./src/resource/ns.apk")

    desired_cap = {
        "platformName":"Android",
        "deviceName":"emulator-5554",
        "app":app_path,
        "appPackage": "nl.ns.android.activity",
        "appActivity": "nl.ns.android.travelplanner.ui.planner.TravelPlannerActivity",
        "noReset": True,
    }

    # Create the driver instance
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(20)

    yield driver
