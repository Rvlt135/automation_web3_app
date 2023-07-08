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

contract = w3.eth.contract(APP_CONTRACT_ADDRESSES, abi=ABI_NFT_CONTRACT_TEST)
account_addresses = w3.eth.account.from_key(private_key=PRIVATE_TEST_KEY).address
# parameters for deployCollection
name = 'tester'
symbol = 'TST'
baseURI = 'test.io'

nonce = w3.eth.get_transaction_count(ACCOUNT_ADDRESSES)

transaction = contract.functions.deployCollection(name, symbol, baseURI).build_transaction({
    'from': account_addresses,
    'nonce': nonce,
    'gasPrice': w3.to_wei(2, 'gwei')  # Gas Price в 2 Gwei,
    # 'gas': 200000
})

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_TEST_KEY)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Ожидание подтверждения транзакции
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Проверка статуса транзакции
if tx_receipt['status']:
    print("Транзакция успешно выполнена.")
else:
    print("Ошибка при выполнении транзакции.")
