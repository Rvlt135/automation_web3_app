from selenium.webdriver.common.by import By


check_box_terms_of_use = (By.CSS_SELECTOR, '[id="onboarding__terms-checkbox"]')
button_import_an_exist_wallet = (By.CSS_SELECTOR, '[data-testid="onboarding-import-wallet"]')
button_i_agree_auth = (By.CSS_SELECTOR, '[data-testid="metametrics-i-agree"]')
# field_secret_value = (By.CSS_SELECTOR, '[data-testid="import-srp__srp-word-0"]')
button_confirm_import = (By.CSS_SELECTOR, '[data-testid="import-srp-confirm"]')
new_password_input = (By.CSS_SELECTOR, '[data-testid="create-password-new"]')
new_password_repeat_input = (By.CSS_SELECTOR, '[data-testid="create-password-new"]')
check_box_confirm_password = (By.CSS_SELECTOR, '[data-testid="create-password-terms"]')
button_confirm_import_wallet = (By.CSS_SELECTOR, '[data-testid="create-password-import"]')
button_success_auth = (By.CSS_SELECTOR, '[data-testid="onboarding-complete-done"]')
secret_recovery_1 = (By.CSS_SELECTOR, '[data-testid="import-srp__srp-word-0"]')
secret_recovery_2 = (By.CSS_SELECTOR, '[data-testid="import-srp__srp-word-1"]')

"""fields_secret_recovery_and_locators_dict = {
    'input[data-testid="import-srp__srp-word-0"]': 'seek',
    'input[data-testid="import-srp__srp-word-1"]': 'series',
    'input[data-testid="import-srp__srp-word-2"]': 'fossil',
    'input[data-testid="import-srp__srp-word-3"]': 'useless',
    'input[data-testid="import-srp__srp-word-4"]': 'song',
    'input[data-testid="import-srp__srp-word-5"]': 'dose',
    'input[data-testid="import-srp__srp-word-6"]': 'issue',
    'input[data-testid="import-srp__srp-word-7"]': 'habit',
    'input[data-testid="import-srp__srp-word-8"]': 'bamboo',
    'input[data-testid="import-srp__srp-word-9"]': 'shoulder',
    'input[data-testid="import-srp__srp-word-10"]': 'wrestle',
    'input[data-testid="import-srp__srp-word-11"]': 'trip'
}"""