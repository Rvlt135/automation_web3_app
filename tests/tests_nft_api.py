import allure
import time
import logging

name = "tester"
symb = "test"
uri = "tester@test.io"
tokenID = "1234"


@allure.story('Api test deploy collection')
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
        time.sleep(10)
    with allure.step('Request on get collections'):
        nft_collection = api_client.get_deploy_collection()
        for deploy_collection in nft_collection:
            if 'CollectionCreated' in deploy_collection.get('eventName'):
                assert deploy_collection.get('symbol') == symb


@allure.story('Api test create NFT and check')
def test_api_nft_mint_collection(api_client, w3_client_polygon):
    with allure.step('Request get on NFT collection ID'):
        transaction_deploy_dict = {
            'from': w3_client_polygon.get_account_addresses(),
            'nonce': w3_client_polygon.get_nonce_account(),
            'gasPrice': w3_client_polygon.w3_client.to_wei(2, 'gwei')  # Gas Price в 2 Gwei,
        }

        nft_collection_id = api_client.get_deploy_collection_id()
    with allure.step('Request on get collections'):
        w3_client_polygon.transaction_mint_nft(
            nft_collection_id,
            w3_client_polygon.get_account_addresses(),
            tokenID,
            transaction_deploy_dict
        )
        events_list = api_client.get_deploy_collection()
        for deploy_collection in events_list:
            if 'TokenMinted' in deploy_collection.get('eventName'):
                assert deploy_collection.get('collection') == nft_collection_id
