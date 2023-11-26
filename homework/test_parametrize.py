import pytest
from selene import browser, be, have


@pytest.mark.desktop
@pytest.mark.parametrize("github_desktop", [(1120, 820)], indirect=True)
def test_github_sign_in_desktop(github_desktop):
    # GIVEN
    browser.open('https://github.com')

    # WHEN
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()

    # THEN
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
@pytest.mark.parametrize("github_mobile", [(600, 600)], indirect=True)
def test_github_sign_in_mobile(github_mobile):
    # GIVEN
    browser.open('https://github.com')

    # WHEN
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()

    # THEN
    browser.element('#login').should(have.text('Sign in to GitHub'))
