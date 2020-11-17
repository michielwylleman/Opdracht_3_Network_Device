#De volgende script zorgt er voor dat we een nieuwe interface make

#Hier importeren weren functies die we nodig hebben voor de volgende scripts
import json
import requests
#schakelt waarschuwinging uit voor de HTTP client
requests.packages.urllib3.disable_warnings()
#De API waar we een ticken zullen aanvragen. In dit geval is het een apparaat op een sandbox van ciscodevnet.
api_url="https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback3" #headers met de volgende gegevens.
#headers met de volgende gegevens.
headers = {
    "Accept":"application/yang-data+json",
    "Content-type":"application/yang-data+json"
    }
#een simpele authenticatie voor de het apparaat.
basicauth = ("cisco", "cisco_1234!")
#in deze dictionary zitten de configuraties gegevens van onze nieuwe interface op onze router.
yangConfig = {
    "ietf-interfaces:interface":{
        "name":"Loopback3",
        "description":"Gemaakt voor Opdracht_3",
        "type":"iana-if-type:softwareLoopback",
        "enabled":True,
        "ietf-ip:ipv4": {
            "address": [
                {
                   "ip": "3.3.3.3",
                   "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }
## Maakt de aanvraag naar de API.
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
#Deze if statement zorgt ervoor  dat we de HTTP STATUS code te zien zullen krijgen.
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))
