import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


ch_capabilities = {
    'LT:Options': {
        "user": "<username>",
        "accessKey": "<accesskey>",
        "build": "NoSuchElementException Test on Chrome",
        "name": "NoSuchElementException Test on Chrome",
        "platformName": "Windows 10"
    },
    "browserName": "Chrome",
    "browserVersion": "102.0",
}


def test_lambdatest_nosuchelement():
    # LambdaTest Profile username
    user_name = "<username>"
    # LambdaTest Profile access_key
    app_key = "<accesskey>"
    # Remote Url to connect to our instance of LambdaTest
    remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    # creating an instance of Firefox based on the remote url and the desired capabilities
    ch_driver = webdriver.Remote(
        command_executor=remote_url, desired_capabilities = ch_capabilities)
    ch_driver.get('https://www.lambdatest.com/selenium-playground/')
    # This will maximize the window interface of the driver class in this case it's FIREFOX
    ch_driver.maximize_window()
    # Will find an element by its NAME property in the page and click it
    ch_driver.find_element(By.CLASS_NAME, "p-10").click()
    ch_driver.quit()


