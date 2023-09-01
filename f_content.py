import requests 

def retrive_forecast():
    """
    A function that retrives the wheather forecast information for the next 24 hr
    by an API call to the open-meteo.org
    args: 
    returns: a list of temperatures in the next 24 hours
    """

    url = "https://api.open-meteo.com"
    end_point = "/v1/forecast?"
    params = "latitude=40.7143&longitude=-74.006&hourly=temperature_2m&timezone=America%2FNew_York&forecast_days=1"
    query = url + end_point + params

    response = requests.get(query)
    if response.status_code == 200:
        print('API call was successfull')
        api_data_temp = response.json()['hourly']['temperature_2m']
    else:
        print('API call was not successfull')
        api_data_temp = 0

    return api_data_temp

if __name__ == "__main__":
    temperature_forecast = retrive_forecast()