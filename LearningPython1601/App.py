import requests
import time
from libs.OpenExchange import OpenExchangeClient

APP_ID = 'db1c59962b1640e1bfc0d85c04d15c66'
ENDPOINT = 'https://openexchangerates.org/api/latest.json'

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
inr_amount = 1000

start = time.time()

gbp_amount = client.convert(usd_amount, "USD", "GBP")

gbp_amount1 = client.convert(inr_amount, "INR", "GBP")

end = time.time()
print(end-start)

print(f'USD {usd_amount} is GBP {gbp_amount:.2f}.')
print(f'INR {usd_amount} is GBP {gbp_amount1:.2f}.')


