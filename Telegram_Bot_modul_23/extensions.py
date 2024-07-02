import requests
import json


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        url = f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}"
        response = requests.get(url)
        data = response.json()

        if 'Response' in data and data['Response'] == 'Error':
            raise APIException(f"Error from API: {data['Message']}")

        try:
            rate = data[quote]
            converted_amount = float(amount) * rate
            return converted_amount
        except KeyError:
            raise APIException(f"Invalid currency code: {quote}")
        except ValueError:
            raise APIException("Amount must be a valid number")
