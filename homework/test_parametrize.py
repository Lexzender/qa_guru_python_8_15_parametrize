import pytest
from selene import browser, be, have



def test_github_sign_in_desktop(github_desktop):
    # GIVEN
    browser.open('https://github.com')

    # WHEN
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()

    # THEN
    browser.element('#login').should(have.text('Sign in to GitHub'))


def test_github_desktop(browser):
    pass


def test_github_mobile(browser):
    pass
