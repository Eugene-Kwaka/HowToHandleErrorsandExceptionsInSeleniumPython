import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

# Desired Capabilities according to SELENIUM 4
ff_capabilities = {
		'LT:Options' : {
			"user" : "<username>",
			"accessKey" : "<accesskey>",
			"build" : "StaleElementReferenceException Handling Test for LambdaTest (Firefox)",
			"name" : "StaleElementReferenceException Handling Test for LambdaTest (Firefox)",
			"platformName" : "Windows 10"
		},
		"browserName" : "Firefox",
		"browserVersion" : "101.0",
	}

def test_ecommerceplayground_staleelement():
     # LambdaTest Profile username
    user_name = "<username>"
    # LambdaTest Profile access_key
    app_key = ""
    # Remote Url to connect to our instance of LambdaTest
    remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    # creating an instance of Firefox based on the remote url and the desired capabilities
    ff_driver = webdriver.Remote(
        command_executor=remote_url, desired_capabilities = ff_capabilities)
    ff_driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/login')

    emailElement = ff_driver.find_element(By.ID, "input-email")
    passwordElement = ff_driver.find_element(By.ID, "input-password")

    emailElement.send_keys("kwakaeugene@gmail.com")
    
    ff_driver.find_element(By.XPATH, "//input[@type='submit']").click()

    try:
        passwordElement.send_keys("password")
    
    except StaleElementReferenceException:
        print('StaleElementReferenceException handled')
        passwordElement = ff_driver.find_element(By.ID, "input-password")
        passwordElement.send_keys("password")

    ff_driver.quit()
