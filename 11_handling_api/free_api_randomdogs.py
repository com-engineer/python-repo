import requests

def get_random_dog():
    url = "https://api.freeapi.app/api/v1/public/dogs/dog/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        dog_data = data["data"]
        name = dog_data["name"]
        temperament = dog_data["temperament"]
        return name,temperament
    else:
        print("data is not received")

def main():
    try:
        name,temperament = get_random_dog()
        print(f"Name of the dog: {name},\nTemprament of the dog: {temperament}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()