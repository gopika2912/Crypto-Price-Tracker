import requests

def get_crypto_price(crypto="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url).json()
    return response[crypto]["usd"]

if __name__ == "__main__":
    crypto_name = input("Enter cryptocurrency name: ")
    price = get_crypto_price(crypto_name.lower())
    print(f"Current price of {crypto_name}: ${price}")
