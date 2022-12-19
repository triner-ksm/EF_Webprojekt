import json

#JSON-Datei öffnen
f = open('weather.json')

#JSON-Datei in einen Dictionary überführen
data = json.load(f)

#JSON-Datei schliessen
f.close()

#Inhalt der JSON-Datei ausgeben
print(data)

#Einzelne Attribute ausgeben
print(data['coord'])