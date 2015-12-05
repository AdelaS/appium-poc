import os
from appium import webdriver
from pytest import fixture


@fixture
def apk_file_path():
    return os.path.join(
        os.path.dirname(__file__),
        '../assets/binary_code_translator.apk'
    )


@fixture
def driver_options(apk_file_path):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': 'Nexus 5 API 23 x86',
        'app': apk_file_path
    }

    return desired_caps


@fixture
def app_driver(request, driver_options):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', driver_options)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
