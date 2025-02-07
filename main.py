import requests
import json

shaxs = "uzb-muhammadsodikmu"
sura = 2

url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{shaxs}/{sura}.json"
response = requests.get(url).json()
oyatlar = response['chapter'][2:5]

# JSON faylga saqlash
with open("oyatlar.json", "w", encoding="utf-8") as file:
    json.dump(oyatlar, file, ensure_ascii=False, indent=4)

print("Ma'lumotlar 'oyatlar.json' fayliga saqlandi.")
