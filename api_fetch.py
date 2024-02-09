import requests

city = 'london'
country = 'england'
api_key = '5XEpw81RMTnnTc3IogjVWg==VB0n51BA4N7GkDVM'
api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}&country={}'.format(city, country)
response = requests.get(api_url + city, headers={'X-Api-Key': api_key})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
