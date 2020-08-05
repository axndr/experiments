import requests


r = requests.get('https://httpbin.org/delay/2', timeout=3)

print(r)

