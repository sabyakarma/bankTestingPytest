from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from UI.utilities.ConfigReader import ConfigReader


@pytest.fixture(scope='class')
def setup_and_teardown(request):
    chrome_options = Options()
    chrome_options.add_argument("--maximize")
    driver = webdriver.Chrome(service=(Service(ChromeDriverManager().install())), options=chrome_options)
    configreader = ConfigReader()
    driver.get(url=configreader.get_base_url())
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture()
def get_userDetails():
    configreader = ConfigReader()
    userDetails = {'username':configreader.get_user_name(),
                   'password':configreader.get_user_password()}
    return userDetails



# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         # always add url to report
#         extras.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
#         report.extras = extras


def pytest_html_report_title(report):
    report.title = "PARABANK TEST REPORT"


# # @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     # This allows adding metadata to the report
#
#     if hasattr(config, '_metadata'):
#         config._metadata['Project Name'] = 'My Automation Project'
#         config._metadata['Module'] = 'User Login'
#         config._metadata['Browser'] = 'Chrome'
#         config._metadata['Platform'] = 'Windows 10'
#         config._metadata['Tested By'] = 'QA Team'

