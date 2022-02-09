import finnhub
import datetime
import os


def mini(liste):
    mini = len(liste[0])
    for i in range(1, len(liste)):
        if len(liste[i]) < mini:
            mini = len(liste[i])
    return mini

with open("clef.txt", "r") as f:
    clef = f.readline()

finnhub_client = finnhub.Client(api_key=clef)

debut = 1600000000
fin = 1640000000

date_debut, heure_debut = str(datetime.datetime.fromtimestamp(debut)).split(" ")
date_debut = date_debut.split("-")
date_fin, heure_fin = str(datetime.datetime.fromtimestamp(fin)).split(" ")
date_fin = date_fin.split("-")

print("Récupération et insertion des données allant du", date_debut[2]+"/"+date_debut[1]+"/"+date_debut[0], "à", heure_debut, "au", date_fin[2]+"/"+date_fin[1]+"/"+date_fin[0], "à", heure_fin)

SYMBOLS = ["AAPL", "TSLA", "ATVI", "DIS", "AMZN", "BINANCE:BTCUSDT"]
results = [[], [], [], [], [], []]

path = os.path.dirname(__file__)
print("PATH:", path[:path.rfind("/")]+"/candle_sample.txt")

for x in SYMBOLS:
    api_call = finnhub_client.stock_candles(x, 1, debut, fin)
    for i in range(len(api_call['t'])):
        try:
            newdict = {x: {'c': api_call['c'][i], 'h': api_call['h'][i], 'l': api_call['l'][i], 'o': api_call['o'][i], 's': 'ok', 't': api_call['t'][i], 'v': api_call['v'][i]}}
        except:
            newdict = {x: {'s': 'no_data'}}
        results[SYMBOLS.index(x)].append(newdict)

with open(path+"/candle_sample.txt", "w+") as f:
    f.truncate(0)
    for i in range(mini(results[0])):
        for j in range(6):
            f.write(str(results[j][i])+"\n")