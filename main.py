# Setup
from web3 import Web3

url_test_polygon = "https://rpc.ankr.com/polygon_mumbai"

client_web3 = Web3(Web3.HTTPProvider(url_test_polygon))

# Print if web3 is successfully connected
print(client_web3.is_connected())
