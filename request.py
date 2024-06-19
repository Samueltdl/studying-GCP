import requests
import os
from dotenv import load_dotenv

def get_lati_longi(api_key, address):

    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    params = {

        "address": address,

        "key": api_key

    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        if data["status"] == "OK":

            location = data["results"][0]["geometry"]["location"]

            lat = location["lat"]

            lng = location["lng"]

            return lat, lng

        else:

            print(f"Error: {data['error_message']}")

            return 0, 0

    else:

        print("Failed to make the request.")

        return 0, 0
    
    
def get_dist_dur(api_key, start, end):

    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {

        "origins": start,

        "destinations": end,

        "key": api_key

    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:

        data = response.json()

        if data["status"] == "OK":

            distance = data["rows"][0]["elements"][0]["distance"]["text"]

            duration = data["rows"][0]["elements"][0]["duration"]["text"]

            return distance, duration

        else:

            print("Request failed.")

            return None, None

    else:

        print("Failed to make the request.")

        return None, None


# pegando a key de API da .env
load_dotenv()
api_key = os.getenv("API_KEY")

################################### PRIMEIRO TESTE ###############################

# Lista de endereços a serem pesquisados
address_list = [
    'Rua Bento Gonçalves, 152, Centro, Rio Grande - RS, Brazil',
    'Avenida Buarque de Macedo, 240, Cidade Nova, Rio Grande - RS, Brazil',
    'Rua Domingos de Almeida, 389, Parque Marinha, Rio Grande - RS, Brazil',
    'Rua General Osório, 523, Cassino, Rio Grande - RS, Brazil',
    'Avenida Itália, 712, Vila Junção, Rio Grande - RS, Brazil',
    'Rua 24 de Maio, 91, Santa Rosa, Rio Grande - RS, Brazil',
    'Rua Riachuelo, 325, Getúlio Vargas, Rio Grande - RS, Brazil',
    'Avenida Presidente Vargas, 456, Vila São Miguel, Rio Grande - RS, Brazil',
    'Rua Silva Paes, 237, Junção, Rio Grande - RS, Brazil',
    'Rua Marechal Floriano, 678, Vila São João, Rio Grande - RS, Brazil'
]

# Pesquisando cada um dos endereços da lista e printando no terminal
print(f'\n------------ Endereços pesquisados -------------')
cont = 1
for address in address_list:

    lati, longi = get_lati_longi(api_key, address)

    print(f"Endereço {cont} => Latitude: {lati}, Longitude: {longi}")
    cont += 1

######################################### SEGUNDO TESTE ##################################
print(f'\n------------ Distância entre endereços -------------')

start = "Palace Lucerna, Nové Město"

end = "Project FOX, Praha 3-Žižkov"


distance, duration = get_dist_dur(api_key, start, end)

if distance and duration:

    print(f"Driving Distance: {distance}")

    print(f"Driving Duration: {duration}")
