import requests

API_KEY = "YourEtherscanAPIKey"

def get_transactions(address):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={API_KEY}"
    response = requests.get(url).json()

    if response["status"] != "1":
        print(f"No transactions found for {address}")
        return

    latest_tx = response["result"][0]

    print(f"\nWallet: {address}")
    print(f"Hash: {latest_tx['hash']}")
    print(f"From: {latest_tx['from']}")
    print(f"To: {latest_tx['to']}")
    print(f"Value: {int(latest_tx['value']) / 10**18} ETH")

def main():
    with open("wallets.txt") as f:
        wallets = [line.strip() for line in f if line.strip()]

    for wallet in wallets:
        get_transactions(wallet)

if __name__ == "__main__":
    main()
