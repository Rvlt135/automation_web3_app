import allure


@allure.feature('API тесты')
@allure.story('Api проверки созданных коллекций')
def test_api_create_user(api_client):
    # with allure.step('Выполняем запрос на проверку коллекций'):
    nft_collection = api_client.get_deploy_collection()
    print(nft_collection)