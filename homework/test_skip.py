import pytest
from selene import browser, be, have


@pytest.mark.desktop
def test_github_sign_in_desktop(is_github_desktop):
    # GIVEN
    if not is_github_desktop:
        pytest.skip(reason='Тест для декстопа')

    browser.open('https://github.com')

    # WHEN
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()

    # THEN
    browser.element('#login').should(have.text('Sign in to GitHub'))

    browser.quit()


@pytest.mark.mobile
def test_github_sign_in_mobile(is_github_mobile):
    # GIVEN
    if not is_github_mobile:
        pytest.skip(reason='Тест для мобилок')

    browser.open('https://github.com')

    # WHEN
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()

    # THEN
    browser.element('#login').should(have.text('Sign in to GitHub'))
