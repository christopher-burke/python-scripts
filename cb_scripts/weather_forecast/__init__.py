#!/usr/bin/env python3

"""Weather from OpenWeatherMap."""

import os
import requests
import json


class WeatherData:
    """Weather from OpenWeatherMap."""

    def __init__(self, units="imperial"):
        self.weather_api_key = os.environ['OPEN_WEATHER_API']
        self.postal_code = os.environ['POSTAL_CODE']
        self.base_url = 'https://api.openweathermap.org/data/2.5'
        self.units = units
        self.current = self.current_data()
        self.forecast = self.forecast_data()

    def current_data(self):
        url = f"{self.base_url}/weather?zip={self.postal_code},us&APPID={self.weather_api_key}&units={self.units}"
        response = requests.get(url)
        results = json.loads(response.content)

        return results

    def forecast_data(self):
        url = f"{self.base_url}/forecast?zip={self.postal_code},us&APPID={self.weather_api_key}&units={self.units}"
        response = requests.get(url)
        results = json.loads(response.content)

        return results


def main():
    data = WeatherData()
    print(data.current)
    print(data.forecast)


if __name__ == "__main__":
    main()
