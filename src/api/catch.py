# API Requesting module to get data from distant sources (but not DB)
# Database can be access directly through the project by using Django backends

import urllib.request
import json

base_url = "https://blockchain.info/fr/"

def get_last_price(currency):
    json_str = urllib.request.urlopen(base_url + "ticker").read().decode("utf-8");
    json_arr = json.loads(json_str)
    return json_arr[currency]['last']
