from brownie import ERC20Basic, accounts, config, network

def main():
    account = accounts.add(config["wallets"]["from_key"])
    TC = ERC20Basic[-1]
    transfer = TC.transfer(input('Enter destination Address: '), int(input('Enter amount')), {'from': account})
    transfer.wait(1)
    print('Success')
    