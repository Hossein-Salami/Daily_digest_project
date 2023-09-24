import requests 
from matplotlib import pyplot as plt

def retrive_forecast():
    """
    A function that retrives the weather forecast information for the next 24 hr
    by an API call to the open-meteo.org
    args: 
    returns: a list of temperatures in the next 24 hours
             saves a figure plotting the temp in the next 24 hours
    """

    url = "https://api.open-meteo.com"
    end_point = "/v1/forecast?"
    params = "latitude=40.7143&longitude=-74.006&hourly=temperature_2m&timezone=America%2FNew_York&forecast_days=1"
    query = url + end_point + params

    # api call to retrive the temp
    response = requests.get(query)
    if response.status_code == 200:
        print('Weather API call was successfull')
        api_data_temp = response.json()['hourly']['temperature_2m']
    else:
        print('Weather API call was not successfull')
        api_data_temp = 0

    """
    # preparing and saving the temp plot
    plt.figure()
    plt.plot(api_data_temp, 'o--', color='g', alpha=0.5, markersize=12)
    plt.xticks([0, 6, 12, 18, 24])
    plt.xlabel('Time [hr]', fontsize=16)
    plt.ylabel('Temprature [oC]', fontsize=16)
    plt.savefig('.\\artwork_design\\temp_plot.jpg', dpi=300, bbox_inches='tight')
    """

    return api_data_temp


#############################################
if __name__ == "__main__":
    temperature_forecast = retrive_forecast()
    print(temperature_forecast)