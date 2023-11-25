from selene import browser


def test_github_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com')

    yield
    browser.quit()


def test_github_mobile():
    browser.config.window_width = 872
    browser.config.window_height = 872
    browser.open('https://github.com')
    yield
    browser.quit()
