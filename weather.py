# weather.py

from configparser import ConfigParser


def _get_api_key():
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]
