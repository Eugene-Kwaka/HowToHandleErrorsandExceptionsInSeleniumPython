# Pytest is used for Unit Testing and provides mechanism for Parameterized testing
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

ch_capabilities = {
		'LT:Options' : {
			"user" : "<username>",
			"accessKey" : "<accesskey>",
			"build" : "StaleElementReferenceException Handling Test on Chrome",
			"name" : "StaleElementReferenceException Handling Test on Chrome",
			"platformName" : "Windows 10"
		},
		"browserName" : "Chrome",
		"browserVersion" : "102.0",
	}

def test_lambdatest_nosuchelement():
    # LambdaTest Profile username
    user_name = "<username>"
    # LambdaTest Profi<accesskey>ey
    app_key = "hrvYNwscfUKvdpNDeVI7pEJODFEvReuClkmtyFjogafe0xeMpf"
    # Remote Url to connect to our instance of LambdaTest
    remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    # creating an instance of Firefox based on the remote url and the desired capabilities
    ch_driver = webdriver.Remote(
        command_executor=remote_url, desired_capabilities = ch_capabilities)
    ch_driver.get('https://www.lambdatest.com/selenium-playground/')
    ch_driver.maximize_window()

    try:
    # 'By' is used to locate the element by its property
        ch_driver.find_element(By.CLASS_NAME, "p-10")
        ch_driver.click()
    except NoSuchElementException:
        print("Exception Handled")
        
    ch_driver.quit()   

