import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browserr = testdata['browser']


# Опции только для хрома
# options = webdriver.ChromeOptions()


@pytest.fixture()               #@pytest.fixture(scope='session')
def browser():
    if browserr == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# @pytest.fixture
# def site(scope='session'):
#     site_instance = Site(testdata['address'])
#     yield site_instance
#     site_instance.close()


# @pytest.fixture
# def element2():
#     x_selector3 = """//*[@id="app"]/main/nav/a/span"""
#     return x_selector3
#
#
# @pytest.fixture
# def result2():
#     return "Home"
#
#
# @pytest.fixture
# def create_post():
#     return """//*[@id="create-btn"]"""
#
#
# @pytest.fixture
# def title():
#     return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
#
#
# @pytest.fixture
# def description():
#     return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
#
#
# @pytest.fixture
# def content():
#     return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
#
#
# @pytest.fixture
# def create_post_finish():
#     return """//*[@id="create-item"]/div/div/div[7]/div/button"""
#
#
# @pytest.fixture
# def post():
#     return """//*[@id="app"]/main/div/div[1]/div/div[3]"""
#
#
# @pytest.fixture
# def title_post():
#     return "Special for you"
