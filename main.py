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

w3 = Web3(Web3.HTTPProvider(URL_TESTNET_POLYGON))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(w3.is_connected())

nonce = w3.eth.get_transaction_count(ACCOUNT_ADDRESSES)
account_addresses = w3.eth.account.from_key(private_key=PRIVATE_TEST_KEY).address

name = "tester"
symb = "symbol"
uri = "tester@test.io"

transaction_dict = {
    'from': account_addresses,
    'nonce': nonce,
    'gasPrice': w3.to_wei(2, 'gwei')  # Gas Price в 2 Gwei,
    # 'gas': 200000
}


def transaction_deploy_collection(collection_name: str,
                                  symbol: str,
                                  baseURI: str,
                                  test_data_transaction: dict):

    contract = w3.eth.contract(APP_CONTRACT_ADDRESSES, abi=ABI_NFT_CONTRACT_TEST)
    collection_name = collection_name
    symbol = symbol
    baseUri = baseURI
    build_transaction_dict = test_data_transaction

    # Создание транзакции
    transaction_data_for_deploy_collection = contract.functions.deployCollection(collection_name, symbol,
                                                                                 baseUri).build_transaction(build_transaction_dict)

    # Подпись и отправка транзакции
    signed_txn = w3.eth.account.sign_transaction(transaction_data_for_deploy_collection, private_key=PRIVATE_TEST_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Ожидание подтверждения транзакции
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Проверка статуса транзакции
    if tx_receipt['status']:
        print("Транзакция успешно выполнена.")
    else:
        print("Ошибка при выполнении транзакции.")



transaction_deploy_collection(name, symb, uri, transaction_dict)

