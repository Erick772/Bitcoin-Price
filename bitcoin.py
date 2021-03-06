# Mostra 1 BTC (bitcoin) na moeda especificada (USD, BRL, CAD, etc)
# exemplo.py BRL
# 1 BTC = R$ X,Y BRL

import requests
import json
from sys import argv

moeda = argv[1]

info = json.loads(requests.get('https://blockchain.info/ticker').text)

print('1 BTC = %s %.2f %s' % (info[moeda]['symbol'], info[moeda]['buy'], moeda))
