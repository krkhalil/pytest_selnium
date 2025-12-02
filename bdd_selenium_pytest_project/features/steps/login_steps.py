from behave import given
from urllib.request import urlopen
from urllib.error import URLError
from utils import config as cfg


@given('the application is available')
def step_impl(context):
    """
    Basic availability check to support running these feature files with
    `behave` (if someone prefers behave over pytest-bdd). This mirrors the
    pytest-bdd step but uses the behave fixtures / context.
    """
    base_url = cfg.config.get('base_url', 'https://example.com')
    try:
        with urlopen(base_url, timeout=5) as resp:
            status = getattr(resp, 'status', 200)
            if not (200 <= status < 400):
                assert False, f"Application returned status {status} at {base_url}"
    except URLError as e:
        assert False, f"Application appears unavailable at {base_url}: {e}"
    except Exception as e:
        assert False, f"Error checking application availability at {base_url}: {e}"
