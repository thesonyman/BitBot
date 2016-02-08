# API Requesting module to get data from distant sources (but not DB)
# Database can be access directly through the project by using Django backends

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