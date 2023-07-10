# Setup
from web3 import Web3
from web3.middleware import geth_poa_middleware
from data.config import (
    ABI_NFT_CONTRACT_TEST,
    APP_CONTRACT_ADDRESSES,
    ACCOUNT_ADDRESSES,
    PRIVATE_TEST_KEY,
    URL_TESTNET_POLYGON
)


# from data.test_data import transaction_deploy_dict

class w3Client:
    """Main client for work blockchain net"""

    def __init__(self, url: str,
                 contract: str,
                 contract_abi: str,
                 account: str,
                 private_key: str):
        self.url = url
        self.contract_address = contract
        self.contract_abi = contract_abi
        self.account_1_addresses = account
        self.private_key = private_key


class w3Polygon(w3Client):
    """client for word Polygon net"""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'w3_client'):
            super().__init__(url=URL_TESTNET_POLYGON,
                             contract=APP_CONTRACT_ADDRESSES,
                             contract_abi=ABI_NFT_CONTRACT_TEST,
                             account=ACCOUNT_ADDRESSES,
                             private_key=PRIVATE_TEST_KEY)

            self.w3_client = Web3(Web3.HTTPProvider(self.url))
            self.w3_client.middleware_onion.inject(geth_poa_middleware, layer=0)
            if self.w3_client.is_connected():
                print("Connect is True")
            else:
                print("Connect is False")

    def init_contract(self):
        app_contract_addresses = APP_CONTRACT_ADDRESSES
        abi_contract = ABI_NFT_CONTRACT_TEST
        return self.w3_client.eth.contract(app_contract_addresses, abi=abi_contract)

    def get_account_addresses(self):
        """return: account addresses client"""

        account_addresses = self.w3_client.eth.account.from_key(private_key=PRIVATE_TEST_KEY).address
        return account_addresses

    def get_nonce_account(self):
        """return: nonce account transaction"""
        nonce = self.w3_client.eth.get_transaction_count(ACCOUNT_ADDRESSES)
        return nonce

    def transaction_deploy_collection(self, collection_name: str,
                                      symbol: str,
                                      baseUri: str,
                                      test_data_transaction: dict):
        contract = self.w3_client.eth.contract(APP_CONTRACT_ADDRESSES, abi=ABI_NFT_CONTRACT_TEST)

        # Создание транзакции
        transaction_data_for_deploy_collection = contract.functions.deployCollection(collection_name, symbol,
                                                                                     baseUri).build_transaction(
            test_data_transaction)

        # Подпись и отправка транзакции
        signed_txn = self.w3_client.eth.account.sign_transaction(transaction_data_for_deploy_collection,
                                                                 private_key=PRIVATE_TEST_KEY)
        tx_hash = self.w3_client.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Ожидание подтверждения транзакции
        tx_receipt = self.w3_client.eth.wait_for_transaction_receipt(tx_hash)

        # Проверка статуса транзакции
        if tx_receipt['status']:
            print("Транзакция успешно выполнена.")
        else:
            print("Ошибка при выполнении транзакции.")

    def transaction_mint_nft(self, collection_id: str,
                             addresses_account_mint: str,
                             tokenId: str,
                             test_data_transaction: dict):
        contract = self.w3_client.eth.contract(APP_CONTRACT_ADDRESSES, abi=ABI_NFT_CONTRACT_TEST)

        # Создание транзакции
        transaction_data_for_deploy_collection = contract.functions.deployCollection(collection_id,
                                                                                     addresses_account_mint,
                                                                                     tokenId).build_transaction(
            test_data_transaction)

        # Подпись и отправка транзакции
        signed_txn = self.w3_client.eth.account.sign_transaction(transaction_data_for_deploy_collection,
                                                                 private_key=PRIVATE_TEST_KEY)
        tx_hash = self.w3_client.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Ожидание подтверждения транзакции
        tx_receipt = self.w3_client.eth.wait_for_transaction_receipt(tx_hash)

        # Проверка статуса транзакции
        if tx_receipt['status']:
            print("Транзакция на отправку NFT успешно выполнена.")
        else:
            print("Ошибка при выполнении транзакции на отправку NFT ")
