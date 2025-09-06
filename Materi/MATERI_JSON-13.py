print("------------MATERI 13 -JSON API-----------")

import requests
url = "https://api.aladhan.com/v1/timingsByCity/28-08-2025?city=Jakarta&country=Indonesia&method=5"
response = requests.get(url) # HTTP get
data_json = response.json() #konversi ke json
print(data_json['data']['timings'])

#print di terminal (python app.py)





