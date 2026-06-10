import requests

def fetch_random_product():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)# string of object
    data = response.json()

    if data["success"] and "data" in data:
        product_data = data["data"]
        name = product_data["title"]
        brand = product_data["brand"]
        price = product_data["price"]
        return name,brand,price
    else:
        print("Fails to fetch the data")


def main():
    try:
        name,brand,price = fetch_random_product()
        print(f"Product:{name}, Brand:{brand}, Price:{price}")
    except Exception as  e:
        print(e)

if __name__ == "__main__":
    main()