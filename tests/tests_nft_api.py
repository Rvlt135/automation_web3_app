import allure
import time
import logging

name = "tester"
symb = "symbol"
uri = "tester@test.io"


@allure.feature('API тесты')
@allure.story('Api проверки созданных коллекций')
def test_api_nft_deploy_collections(api_client, w3_client_polygon):
    with allure.step('Request on deploy collections NFT'):
        transaction_deploy_dict = {
            'from': w3_client_polygon.get_account_addresses(),
            'nonce': w3_client_polygon.get_nonce_account(),
            'gasPrice': w3_client_polygon.w3_client.to_wei(2, 'gwei')  # Gas Price в 2 Gwei,
        }

        w3_client_polygon.transaction_deploy_collection(name,
                                                        symb,
                                                        uri,
                                                        transaction_deploy_dict)
        time.sleep(15)
    with allure.step('Request on get collections'):
        nft_collection = api_client.get_deploy_collection()
        for deploy_collection in nft_collection:
            if 'CollectionCreated' in deploy_collection.get('eventName'):
                assert deploy_collection.get('name') == name


@allure.feature('API тесты')
@allure.story('Api проверки созданных коллекций')
def test_api_nft_deploy_collections(api_client, w3_client_polygon):
    with allure.step('Request on deploy collections NFT'):
        transaction_deploy_dict = {
            'from': w3_client_polygon.get_account_addresses(),
            'nonce': w3_client_polygon.get_nonce_account(),
            'gasPrice': w3_client_polygon.w3_client.to_wei(2, 'gwei')  # Gas Price в 2 Gwei,
        }
        nft_collection_id = api_client.get_deploy_collection()

        w3_client_polygon.transaction_deploy_collection(name,
                                                        symb,
                                                        uri,
                                                        transaction_deploy_dict)
        time.sleep(15)
    with allure.step('Request on get collections'):
        nft_collection = api_client.get_deploy_collection()
        for deploy_collection in nft_collection:
            if 'CollectionCreated' in deploy_collection.get('eventName'):
                assert deploy_collection.get('name') == name
