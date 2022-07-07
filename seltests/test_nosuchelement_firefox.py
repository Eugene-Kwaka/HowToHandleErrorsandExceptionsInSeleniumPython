import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Desired Capabilities according to SELENIUM 4
ff_capabilities = {
		'LT:Options' : {
			"user" : "<username>",
			"accessKey" : "<accesskey>",
			"build" : "NoSuchElementException Test for LambdaTest (Firefox)",
			"name" : "NoSuchElementException Test Test for LambdaTest (Firefox)",
			"platformName" : "Windows 10"
		},
		"browserName" : "Firefox",
		"browserVersion" : "101.0",
	}


def test_lambdatest_nosuchelement():
    # LambdaTest Profile username
    user_name = "<username>"
    # LambdaTest Profile access_key
    app_key = "<accesskey>"
    # Remote Url to connect to our instance of LambdaTest
    remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    # creating an instance of Firefox based on the remote url and the desired capabilities
    ff_driver = webdriver.Remote(
        command_executor=remote_url, desired_capabilities = ff_capabilities)
    ff_driver.get('https://www.lambdatest.com/selenium-playground/')
    # This will maximize the window interface of the driver class in this case it's FIREFOX
    ff_driver.maximize_window()
    # Will find an element by its NAME property in the page and click it
    ff_driver.find_element(By.CLASS_NAME, "p-10").click()
    ff_driver.quit()
