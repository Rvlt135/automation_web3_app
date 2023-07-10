import json
import os
import sys
from pathlib import Path

# PROXY CONTRACT NFT CREATED https://mumbai.polygonscan.com/address/0x54eede47850fe932f5466b6fa708bf1176371966#code
# ABI FROM https://mumbai.polygonscan.com/address/0x8d65237b16ef1f7e6bb3e8291368adc2a010f84b#code

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

URL_TESTNET_POLYGON = "https://rpc.ankr.com/polygon_mumbai"
# Нужно написать readjson функцию
ABIS_DIR = os.path.join(ROOT_DIR, 'abis')
ABI_NFT_CONTRACT_FILE_JSON = os.path.join(ABIS_DIR, 'nft_app_abi.json')
METAMSK_EXTENSION_FILE = os.path.join(ROOT_DIR, 'MetaMask.crx')
TYPE_SECRET_PHRASE_LIST = ['seek', 'series', 'fossil', 'useless', 'song', 'dose', 'issue', 'habit', 'bamboo', 'shoulder', 'wrestle', 'trip']

APP_CONTRACT_ADDRESSES = "0x54EEDe47850fE932f5466B6fa708bf1176371966"

ACCOUNT_ADDRESSES = '0xDF0D85Ba488cFBc36dd9e68ba956999a42F15879'

PRIVATE_TEST_KEY = 'ebc9c7c1536422bd042cbacf4384e78fe335e6fd67c5a2dfc33658257c363a53'

ABI_NFT_CONTRACT_TEST = """[
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "collection",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "symbol",
                "type": "string"
            }
        ],
        "name": "CollectionCreated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint8",
                "name": "version",
                "type": "uint8"
            }
        ],
        "name": "Initialized",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "collection",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "tokenURI",
                "type": "string"
            }
        ],
        "name": "TokenMinted",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "baseURI",
                "type": "string"
            }
        ],
        "name": "deployCollection",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract Collection",
                "name": "collection",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]"""
