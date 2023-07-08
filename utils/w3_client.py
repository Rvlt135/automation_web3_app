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

        self.w3 = Web3(Web3.HTTPProvider(self.url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        print(self.w3.is_connected())


class w3Polygon(w3Client(url=URL_TESTNET_POLYGON,
                         contract=APP_CONTRACT_ADDRESSES,
                         contract_abi=ABI_NFT_CONTRACT_TEST,
                         account=ACCOUNT_ADDRESSES,
                         private_key=PRIVATE_TEST_KEY)):

    def init_contract(self):
        app_contract_addresses = APP_CONTRACT_ADDRESSES
        abi_contract = ABI_NFT_CONTRACT_TEST
        return self.w3.eth.contract(app_contract_addresses, abi=abi_contract)
