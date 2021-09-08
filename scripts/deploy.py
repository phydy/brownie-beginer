from brownie import FirstContract, config, accounts
 
def deployContract():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    FirstContract.deploy({'from': account})
 
def main():
    deployContract()
