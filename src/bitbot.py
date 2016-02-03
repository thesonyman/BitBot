# Module principal du bot, routing only

import urllib.request
import time

base_url = "https://blockchain.info/fr/charts/"
chart = "market-price"
timespan = "all"

url = base_url+chart+"?format=json&timespan="+timespan

start = time.time()

response = urllib.request.urlopen(url)

print(response.read().decode("utf-8"))
print("in "+str(round(time.time()-start, 3))+" s")