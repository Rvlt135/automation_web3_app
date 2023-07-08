from data.config import (
    ABI_NFT_CONTRACT_TEST,
    APP_CONTRACT_ADDRESSES,
    ACCOUNT_ADDRESSES,
    PRIVATE_TEST_KEY,
    URL_TESTNET_POLYGON
)
from data.test_data import transaction_deploy_dict
from blockchain_clients.w3_client import w3Polygon

w3 = w3Polygon()
client = w3.w3_client
nonce = client.eth.get_transaction_count(ACCOUNT_ADDRESSES)
account_addresses = client.eth.account.from_key(private_key=PRIVATE_TEST_KEY).address

name = "tester"
symb = "symbol"
uri = "tester@test.io"


def transaction_deploy_collection(collection_name: str,
                                  symbol: str,
                                  baseUri: str,
                                  test_data_transaction: dict):
    contract = client.eth.contract(APP_CONTRACT_ADDRESSES, abi=ABI_NFT_CONTRACT_TEST)

    # Создание транзакции
    transaction_data_for_deploy_collection = contract.functions.deployCollection(collection_name, symbol,
                                                                                 baseUri).build_transaction(
        test_data_transaction)

    # Подпись и отправка транзакции
    signed_txn = client.eth.account.sign_transaction(transaction_data_for_deploy_collection,
                                                     private_key=PRIVATE_TEST_KEY)
    tx_hash = client.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Ожидание подтверждения транзакции
    tx_receipt = client.eth.wait_for_transaction_receipt(tx_hash)

    # Проверка статуса транзакции
    if tx_receipt['status']:
        print("Транзакция успешно выполнена.")
    else:
        print("Ошибка при выполнении транзакции.")


transaction_deploy_collection(name, symb, uri, transaction_deploy_dict)
