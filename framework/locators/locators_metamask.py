from selenium.webdriver.common.by import By


check_box_terms_of_use = (By.CSS_SELECTOR, '[data-testid="onboarding-terms-checkbox"]')
button_import_an_exist_wallet = (By.CSS_SELECTOR, '[data-testid="onboarding-import-wallet"]')
button_i_agree_auth = (By.CSS_SELECTOR, '[data-testid="metametrics-i-agree"]')
button_confirm_import = (By.CSS_SELECTOR, '[data-testid="import-srp-confirm"]')
new_password_input = (By.CSS_SELECTOR, '[data-testid="create-password-new"]')
new_password_repeat_input = (By.CSS_SELECTOR, '[data-testid="create-password-confirm"')
check_box_confirm_password = (By.CSS_SELECTOR, '[data-testid="create-password-terms"]')
button_confirm_import_wallet = (By.CSS_SELECTOR, '[data-testid="create-password-import"]')
button_success_auth = (By.CSS_SELECTOR, '[data-testid="onboarding-complete-done"]')
button_extension_next = (By.CSS_SELECTOR, '[data-testid="pin-extension-next"]')
button_extension_done = (By.CSS_SELECTOR, '[data-testid="pin-extension-done"]')
button_try_out = (By.CSS_SELECTOR, '[data-testid="pin-extension-done"]')
button_try_out_2 = (By.CSS_SELECTOR, '.button.btn--rounded.btn-primary.whats-new-popup__button')
pop_up_notification = (By.CSS_SELECTOR, '[class="whats-new-popup__notifications"]')
pop_up_button_try_out = (By.XPATH, '//button[text()="Try it out"]')
button_save_test_net = (By.CSS_SELECTOR, '.btn-primary')
change_test_net_button = (By.CSS_SELECTOR, '.home__new-network-added__switch-to-button')

metamask_button_next_account = (By.CSS_SELECTOR, '[data-testid="page-container-footer-next"]')
metamask_button_connect = '[data-testid="page-container-footer-next"]'