import requests


def get_temp_hum(district, state=None, month=None):

    with open(".api_key.txt", "r") as file:
        API_KEY = file.read().strip()

    # Use the API key

    url = f"https://api.openweathermap.org/data/2.5/weather?q={district}&appid={API_KEY}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        print(response.text)
        raise Exception(f"Unable to get the temperature for {district}")

    data = response.json()
    humidity = data['main']['humidity']
    temp = (data['main']['temp_min']+data['main']['temp_max'])/2-273.15
    return (temp, humidity)
