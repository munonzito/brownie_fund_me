from brownie import network, accounts, config, MockV3Aggregator


DECIMALS = 8
STARTING_PRICE = 200000000

FORK_LOCAL_ENVIROMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development","ganache-local"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS or network.show_active() in FORK_LOCAL_ENVIROMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) == 0:
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from":get_account()}
            )
    print("Mocks deployed!")
    return MockV3Aggregator[-1].address


    