# Mostra 1 BTC (bitcoin) na moeda especificada (USD, BRL, CAD, etc)
# exemplo.py BRL
# 1 BTC = R$ X,Y BRL

import requests
import json
from sys import argv

moeda = argv[1]

r = requests.get('https://blockchain.info/ticker')

info = json.loads(r.text)

print('1 BTC = %s %.2f %s' % (info[moeda]['symbol'], info[moeda]['buy'], moeda))
