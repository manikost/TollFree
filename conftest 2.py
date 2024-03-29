import allure
import pytest
import requests


from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from data import Data
from Links import Links
from locators import Locator
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import shutil


driver = None
stand = None

pytest_plugins = []

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

    parser.addoption(
        "--stand", action="store", default="qa"
    )

@pytest.fixture(scope="function")

def driver(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":

        with open("env.py","w") as env:
            env.write("env = 'Chrome'")
            env.close()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        driver: WebDriver = webdriver.Chrome(chrome_options=chrome_options)
        # driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        request.cls.driver = driver

        yield
        driver.delete_all_cookies()
        driver.close()
        driver.quit()

    elif browser == "firefox":

        with open("env.py","w") as env:
            env.write("env = 'Firefox'")
            env.close()

        driver: WebDriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver = driver

        yield
        driver.delete_all_cookies()
        driver.close()
        driver.quit()



    elif browser == "edge":
        # with open(".env.py","w") as env:
        #     env.write("env = 'Edge'")
        #     env.close()
        driver: WebDriver = webdriver.Edge(executable_path="Drivers/MicrosoftWebDriver.exe")
        request.cls.driver = driver
        yield
        driver.delete_all_cookies()
        driver.close()
        driver.quit()


    elif browser == "safari":



        # with open("../env.py","w") as env:
        #     env.write("env = 'Safary'")
        #     env.close()
        desired_cap = {
            'browser': 'Safari',
            'browser_version': '12.0',
            'os': 'OS X',
            'os_version': 'Mojave',
            'resolution': '1920x1080',
            'name': 'Bstack-[Python] Sample Test',
            'browserstack.sendKeys': 'True',
            'browserstack.local': 'True'
        }
        driver: WebDriver = webdriver.Remote(
            command_executor='https://igornikolaev3:CSxj6qm7K8zpuggWyqNx@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)


        request.cls.driver = driver

        yield
        driver.delete_all_cookies()

        driver.quit()


    elif browser == "chrome_78":

        capabilities = {
            "browserName": "chrome",
            "version": "78.0",
            "enableVNC": True,
            "enableVideo": False
        }

        driver: WebDriver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities)
        request.cls.driver = driver

        yield
        driver.delete_all_cookies()
        driver.quit()
        return driver


    elif browser == "ff69":



        capabilities = {
            "browserName": "firefox",
            "version": "69.0",
            "enableVNC": True,
            "enableVideo": False
        }

        driver: WebDriver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities)
        request.cls.driver = driver

        yield
        driver.delete_all_cookies()
        driver.quit()
        return driver


@pytest.fixture(scope="function")
def choose_stand(request):

    stand = request.config.getoption("--stand")

    if stand == "qa":
        request.cls.stand = stand
        ### Data for login ###
        Data.CORRECT_DIAL = "(775) 360-1641"  # Write here toll-free number from account
        Data.CORRECT_ACCESS = "531144"  # Write here access code from account
        Data.CORRECT_PIN = "6910"  # Write here your PIN

        #################################################################################################
        #                             WE ANNOUNCE DATA FOR ALL PAGE LINKS                               #
        #################################################################################################
        Data.TOLL_NUMBER = "(775) 360-1642"
        Data.PLAYBACK_NUMBER = "(775) 360-1643"

        Links.account = Links.qa_account
        Links.contact_us = Links.qa_contact_us
        Links.home = Links.qa_home
        Links.login = Links.qa_login
        Links.sign_up = Links.qa_sign_up
        Links.faq = Links.qa_faq
        Links.recordings = Links.qa_recordings
        Data.registration_letter_title = "//span[text()='QA MODE:SimpleTollFree.com Account Registration']"



    elif stand == "prod":
        request.cls.stand = stand
        ### Data for login ###
        Data.CORRECT_DIAL = "(877) 216-1555"  # Write here your toll-free number
        Data.CORRECT_ACCESS = "661400"  # Write here your access code
        Data.CORRECT_PIN = "1756"  # Write here your PIN




@pytest.fixture(scope="function")
def canceled_account():
    payloads = {"id": "213124"}
    r = requests.get("https://ya.ru", params=payloads)
    print(r.url)








