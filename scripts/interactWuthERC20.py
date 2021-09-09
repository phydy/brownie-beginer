from brownie import ERC20Basic, config, accounts, network
 
def main():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    myFirstContract = ERC20Basic[-1]
    tx = myFirstContract.totalSupply({'from': account})
    tx.wait(1)
    print("Total supply is", myFirstContract.totalSupply())
