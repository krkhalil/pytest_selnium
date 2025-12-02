import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

REPORTS_DIR = os.path.join(os.getcwd(), "reports")
SCREENSHOT_DIR = os.path.join(REPORTS_DIR, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture(scope='session')
def base_url():
    # edit utils/config.py for real values; this is a fallback
    return "https://example.com"

@pytest.fixture
def browser():
    # Setup Chrome driver via webdriver-manager
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Uncomment for headless execution:
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Capture screenshots on failure and attach to report if possible
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        browser = item.funcargs.get("browser")
        if browser:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            fname = f'screenshot_{item.name}_{timestamp}.png'
            path = os.path.join(SCREENSHOT_DIR, fname)
            try:
                browser.save_screenshot(path)
                # try to attach to pytest-html if available
                extra = getattr(rep, 'extra', [])
                try:
                    from pytest_html import extras
                    extra.append(extras.image(path))
                    rep.extra = extra
                except Exception:
                    pass
            except Exception as e:
                print("Failed to take screenshot:", e)
