#De bedoeling van deze script is dat we gegevens willen zien van onze apparaat in json-formaat

# Hier importeren weren functies die we nodig hebben voor de volgende scripts
import json
import requests
#schakelt waarschuwinging uit voor de HTTP client
requests.packages.urllib3.disable_warnings()
#De API waar we een ticken zullen aanvragen. In dit geval is het een apparaat op een sandbox van ciscodevnet.
api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback3"
#headers met de volgende gegevens.
headers = {
    "Accept":"application/yang-data+json",
    "Content-type":"application/yang-data+json"
    }
#een simpele authenticatie voor de het apparaat.
basicauth = ("cisco", "cisco_1234!")

# Maakt de aanvraag naar de API.
resp=requests.get(api_url, auth=basicauth, headers=headers, verify=False)
#conveert de gegevens naar json de in python formaat
response_json = resp.json()

#print de gegevens in json-formaat uit maar dan in het traditionele vorm.
print(json.dumps(response_json, indent=4))
