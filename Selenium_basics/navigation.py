import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webserver/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

print(source)