# clima tempo com dados da internet
import pyowm

# You MUST provide a valid API key
owm = pyowm.OWM('API_KEY', language='pt')


def get_city(cities):
    print("{:>10} {:10} {:10}".format("ID", "Cidade", "País"))
    for i, c in enumerate(cities):
        print("{:>10} {:10} {:10}".format(i, c[1], c[2]))

    return cities[int(input('\nDigite o ID da cidade: '))]


def run(entry):
    cities = reg.ids_for(entry)

    if cities:
        city = get_city(cities)

        # Search for current weather in London (Great Britain)
        observation = owm.weather_at_id(city[0])
        # print(observation)
        w = observation.get_weather()
        # <Weather - reference time=2013-12-18 09:20,
        # print(w)
        # status=Clouds>
        print("\n", city[1], city[2])
        # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        print("Temperatura: {} °C".format(
            w.get_temperature('celsius')['temp']))
        print("Huminadade: {}%".format(w.get_humidity()))  # 87
        # {'speed': 4.6, 'deg': 330}
        print("Vento: {} m/s".format(w.get_wind()['speed']))

    else:
        print("Não encontrei merda nenhuma...")


if __name__ == '__main__':
    # Get all math names
    reg = owm.city_id_registry()
    entry = input('Digite o nome de sua cidade: ')

    run(entry)
