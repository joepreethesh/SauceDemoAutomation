import os
import time

import allure
from selenium import webdriver
def before_scenario(context, scenario):
    print("chrome driver executing")
    chrome_driver_path = os.path.abspath(os.path.join('webdriver', 'chromedriver.exe'))
    print("Chromedriver Path:", chrome_driver_path)
    #print("System PATH:", os.environ['PATH'])
    #os.environ['PATH'] = f"{os.environ['PATH']}:{os.path.dirname(chrome_driver_path)}"
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com")
    time.sleep(5)
    #context.driver.maximize_window()

def after_step(context, step):
    try:
        if step and step.status == "failed":
            allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                              attachment_type=allure.attachment_type.PNG)
        elif step:
            allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                              attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(f"Error in after_step: {str(e)}")

def after_scenario(context, scenario):
    print("executing after scenario")
    context.driver.quit()


