import requests

def saa_temperatuur(api_voti, linn):
    # URL OpenWeatherMap API jaoks
    url = f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_voti}&units=metric"
    
    try:
        vastus = requests.get(url)
        if vastus.status_code == 200:
            andmed = vastus.json()
            temperatuur = andmed['main']['temp']
            return temperatuur
        else:
            print("Viga API päringuga. Kontrollige linna nime või API võtit.")
            return None
    except Exception as e:
        print(f"Viga temperatuuri päringuga: {e}")
        return None

def kontrolli_temperatuuri(temperatuur):
    if temperatuur is not None:
        print(f"Hetketemperatuur on: {temperatuur}°C")
        if temperatuur >= 21:
            print("Välistemperatuur on +21°C või rohkem.")
            print("Lülitan sisse põrandajahutuse.")
        else:
            print("Välistemperatuur on alla +21°C.")
            print("Põrandajahutus jääb välja lülitatuks.")
    else:
        print("Temperatuuri ei õnnestunud kontrollida.")

# Näide kasutamisest
api_voti = "e93b246bdb38f996314fd4da2689de88"
linn = input("Sisesta linna nimi: ")
valistemperatuur = saa_temperatuur(api_voti, linn)
kontrolli_temperatuuri(valistemperatuur)
