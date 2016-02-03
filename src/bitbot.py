import urllib.request

base_url = "https://blockchain.info/fr/charts/"
chart = "market-price"
timespan = "all"

url = base_url+chart+"?format=json&timespan="+timespan

response = urllib.request.urlopen(url)

print(response.read())