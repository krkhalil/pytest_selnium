# BDD Automation Project (pytest-bdd + Selenium)

## What's included
- PyTest + Selenium framework using Page Object Model (POM)
- BDD using `pytest-bdd` and `.feature` files
- WebDriver management via `webdriver-manager`
- Screenshot capture on failure
- Sample `login` feature + step definitions
- Allure + pytest-html configuration examples

## How to use
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests (pytest-bdd):
   ```bash
   pytest -v
   ```
4. Run with HTML report:
   ```bash
   pytest -v --html=reports/report.html
   ```
5. Run with Allure (if installed):
   ```bash
   pytest --alluredir=reports/allure-results
   allure serve reports/allure-results
   ```

## Notes
- Update `utils/config.py` to change base_url or credentials.
- Add more Page Objects under `pages/` and feature files under `features/`.
 - This project uses pytest-bdd for BDD tests. If you attempt to run the feature
    files with a different runner (e.g., `behave`) you may encounter "Undefined
    step" errors because behave expects step definitions under
    `features/steps/` and uses the behave API. The repository contains both a
    pytest-bdd step file (`steps/test_login_steps.py`) and a simple behave
    compatibility step (`features/steps/login_steps.py`). Running `pytest` will
    use the pytest-bdd steps.
