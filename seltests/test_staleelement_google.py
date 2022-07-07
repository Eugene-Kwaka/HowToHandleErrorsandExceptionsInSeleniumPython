import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


ch_capabilities = {
    'LT:Options': {
        "user": "<username>",
        "accessKey": "<accesskey>",
        "build": "StaleElementReferenceException Test on Chrome",
        "name": "StaleElementReferenceException Test on Chrome",
        "platformName": "Windows 10"
    },
    "browserName": "Chrome",
    "browserVersion": "102.0",
}


def test_ecommerceplayground_staleelement():
    # LambdaTest Profile username
    user_name = "<username>"
    # LambdaTest Profile access_key
    app_key = "<accesskey>"
    # Remote Url to connect to our instance of LambdaTest
    remote_url = "https://" + user_name + ":" + \
        app_key + "@hub.lambdatest.com/wd/hub"
    # creating an instance of Firefox based on the remote url and the desired capabilities
    ch_driver = webdriver.Remote(
        command_executor=remote_url, desired_capabilities=ch_capabilities)
    ch_driver.get(
        'https://ecommerce-playground.lambdatest.io/index.php?route=account/login')

    emailElement = ch_driver.find_element(By.ID, "input-email")
    passwordElement = ch_driver.find_element(By.ID, "input-password")

    emailElement.send_keys("kwakaeugene@gmail.com")

    ch_driver.find_element(By.XPATH, "//input[@type='submit']").click()

    passwordElement.send_keys("password")

    ch_driver.quit()


