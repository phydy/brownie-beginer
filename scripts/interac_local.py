from brownie import FirstContract, config, accounts, network
 
def main():
    account = accounts.add(config['wallets']['from_key']) or accounts[0]
    myFirstContract = FirstContract[-1]
    tx = myFirstContract.addPhonenos('phidel', 722705110,{'from': account})
    tx.wait(1)
    print("Number is", myFirstContract.showPhoneno('phidel'))