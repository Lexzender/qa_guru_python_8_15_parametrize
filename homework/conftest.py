import pytest
from selene import browser


@pytest.fixture(params=[(3840, 2160), (1920, 1080)], scope='function')
def github_desktop(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open('https://github.com')

    yield
    browser.quit()


@pytest.fixture(params=[(1024, 768), (800, 600), (872, 872)], scope='function')
def github_mobile(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open('https://github.com')
    yield
    browser.quit()


@pytest.fixture(params=[(3840, 2160), (1920, 1080), (1024, 768), (800, 600), (872, 872)])
def is_github_desktop(request):
    resolution = request.param
    if resolution in [(3840, 2160), (1920, 1080)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False


@pytest.fixture(params=[(3840, 2160), (1920, 1080), (1024, 768), (800, 600), (872, 872)])
def is_github_mobile(request):
    resolution = request.param
    if resolution in [(1024, 768), (800, 600), (872, 872)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False
