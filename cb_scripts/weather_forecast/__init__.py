#!/usr/bin/env python3

"""Weather from OpenWeatherMap."""

import os
import requests
import json
from datetime import datetime
from dateutil import tz
from dataclasses import dataclass


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


@dataclass
class WeatherDataDay:
    """Weather Data for a given day."""

    datetime_utc: str
    datetime_local: datetime
    temp_current: float
    temp_hi_low: dict
    wind: float
    sun: dict
    humidity: int
    today: bool = False

    def __post_init__(self):
        self.utc_to_local()
        self.today = self.todays_weather()

    def todays_weather(self):
        return datetime.today().date() == self.datetime_local.date()

    def utc_to_local(self):
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        utc = datetime.utcfromtimestamp(int(self.datetime_utc))
        utc = utc.replace(tzinfo=from_zone)
        self.datetime_local = utc.astimezone(to_zone)


def main():
    """Get Weather Data."""
    data = WeatherData()

    wd = WeatherDataDay(
        datetime_utc=data.current['dt'],
        datetime_local=data.current['dt'],
        temp_current=data.current['main']['temp'],
        temp_hi_low={'high': data.current['main']['temp_max'],
                     'low': data.current['main']['temp_min'], },
        wind=data.current['wind']['speed'],
        sun={'rise': data.current['sys']['sunrise'],
             'set': data.current['sys']['sunset'], },
        humidity=data.current['main']['humidity']
    )

    print(wd)


if __name__ == "__main__":
    main()
