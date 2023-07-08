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


class w3Client:
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

    def __init__(self):
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
        account_addresses = self.w3_client.eth.account.from_key(private_key=PRIVATE_TEST_KEY).address
        return account_addresses

    def get_nonce_account(self):
        nonce = self.w3_client.eth.get_transaction_count(ACCOUNT_ADDRESSES)
        return nonce


