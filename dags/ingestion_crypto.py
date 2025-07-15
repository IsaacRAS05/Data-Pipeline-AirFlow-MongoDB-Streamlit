import requests

headers = {
    'x-access-token':'coinrankingb4557ac4ed2662ce89e4a109d31cb5cf01dc76cf6070cc4b'
}

response = requests.request('GET', 'https://api.coinranking.com/v2/coin/Qwsogvtv82FCd/price-history?timePeriod=1h', headers = headers)

print(f'Bitcoin Price history:',response.text)

