# Setup
from web3 import Web3
from web3.middleware import geth_poa_middleware
from data import config

url_polygon = config.URL_TESTNET_POLYGON
contract_addresses = config.APP_CONTRACT_ADDRESSES
contract_abi = config.ABI_NFT_CONTRACT_TEST
account_addresses = config.ACCOUNT_ADDRESSES

web3 = Web3(Web3.HTTPProvider(url_polygon))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
# Use account
wallet_address = web3.to_checksum_address(
    web3.eth.account.from_key(private_key=config.PRIVATE_TEST_KEY).address)

balance = web3.eth.get_balance(account_addresses)
print(web3.is_connected())
print(f'wallet address: {wallet_address} balance: {balance}')  # if change eth / 10 ** 18

# All change balance
ether_balance = web3.from_wei(balance, 'ether')  # Decimal('1')
gwei_balance = web3.from_wei(balance, 'gwei')  # Decimal('1000000000')
wei_balance = web3.to_wei(ether_balance, 'ether')  # 1000000000000000000

print(ether_balance)
print(gwei_balance)
print(wei_balance)


# contract = web3.eth.contract(address=contract_addresses, abi=contract_abi)
