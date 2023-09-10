from selenium.webdriver.common.by import By


# Локаторы страницы авторизации
class AuthLocators:
    AUTH_PHONE_TAB = (By.ID, 't-btn-tab-phone')
    AUTH_EMAIL_TAB = (By.ID, 't-btn-tab-mail')
    AUTH_LOGIN_TAB = (By.ID, 't-btn-tab-login')
    AUTH_LS_TAB = (By.ID, 't-btn-tab-ls')
    USER_NAME = (By.ID, "username")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.ID, 'ks-login')

    AUTH_EMAIL = (By.ID, "email")
    AUTH_PHONE = (By.XPATH, '//*[@id="username"]')

    AUTH_REG_IN = (By.XPATH, "//a[@id='kc-register']")
    AUTH_REG_IN_TEMP_CODE = (By.ID, 'back_to-otp_btn')
    LOGOUT_BTN = (By.ID, 'logout-btn')
