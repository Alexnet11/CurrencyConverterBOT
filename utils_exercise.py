import requests
import json
from config_exercise import keys, API_KEY


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote:str, base:str, amount:str):

        if quote == base:
            raise ConvertionException(f"Невозможно конвертировать одинаковые валюты {base}.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удаётся обработать валюту{quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удаётся обработать валюту{base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не коректно указано количество конвертируемой валюты {amount}")

        r = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{keys[quote]}/{keys[base]}/{amount}')
        total_base = json.loads(r.content)["conversion_result"]
        return total_base