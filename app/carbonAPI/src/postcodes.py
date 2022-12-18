import requests, pandas as pd

def postcode_data(postcodes): 
    data = {}

    headers = {'Accept': 'application/json'}
    for postcode in postcodes:
        req = requests.get(
            url= f'https://api.carbonintensity.org.uk/regional/postcode/{postcode}', 
            params={}, 
            headers = headers,
            )
        
        if req.status_code == 200:
            data[postcode] = { i['fuel']: i['perc'] for i in req.json()['data'][0]['data'][0]['generationmix'] }
        else:
            data[postcode] = [req.status_code]
    return pd.DataFrame(data)

if __name__ == '__main__':
    postcodes = [f'KY{i}'for i in range(40)]
    print(postcode_data(postcodes=postcodes))