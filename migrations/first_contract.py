import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = 'build/contracts/FirstContract.json'
deployed_contract_address = '0xB16bEc01bfe4F13D5e85A2F75F51893D797Df1F7'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']

contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

result = contract.functions.setValue(5).transact() # use transact to store value in blockchain
print(result)
# message = contract.functions.getMessage().call()
# print(message)