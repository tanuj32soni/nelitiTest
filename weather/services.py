import requests


class WeatherService:
    service_url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'
    headers = {
        'User-Agent': 'Weather App'
    }

    @classmethod
    def get_weather_info(cls, lat, lon):
        response = requests.get(cls.service_url, params={
            "lat": lat,
            "lon": lon
        }, headers=cls.headers)
        response.raise_for_status()
        return response.json()
