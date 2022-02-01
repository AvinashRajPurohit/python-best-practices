"""
Cohesion is the degree to which elements of a certain class or function belong together.

"""


class CurrencyType:
    name: str
    country: str
    market_value_in_usd_per_coin: float

    def __init__(self, name: str, market_value_in_usd_per_coin: float, country: str):
        self.name = name
        self.market_value_in_usd_per_coin = market_value_in_usd_per_coin
        self.country = country


class Currencies:
    available_currencies: dict[str, CurrencyType] = {}

    def add_currency(self, name: str, market_value_in_usd_per_coin: float, country: str):
        currency_type = CurrencyType(name, market_value_in_usd_per_coin, country)
        self.available_currencies[name] = currency_type
        return self.available_currencies

    def get_available_currencies(self):
        print("Name        Country        Market Value (USD)")
        for c_type in self.available_currencies.values():
            print(f"{c_type.name}            {c_type.country}               {c_type.market_value_in_usd_per_coin}")


class Currency_Convertor:

    def __init__(self, convert_from: str, convert_to: str) -> None:
        self.convert_from: str = convert_from
        self.convert_to: str = convert_to
        self.available_currencies: dict = Currencies().available_currencies

    def get_available_currency(self):
        """Function for checking the currency is available or not
        """
        convert_to = self.available_currencies.get(self.convert_to, None)
        convert_from = self.available_currencies.get(self.convert_from, None)
        return convert_to, convert_from

    def get_currency_diffrences_and_convert(self):
        """Function for get converted currency value
        """
        convert_to, convert_from = self.get_available_currency()

        if convert_to is None or convert_from is None:
            return "Currency is not available"

        convert_form_part_usd: float = round(1/convert_from.market_value_in_usd_per_coin, 2)
        convert_to_part_usd: float = round(1/convert_to.market_value_in_usd_per_coin, 2)
        converted_per_currency: float = round(convert_to_part_usd/convert_form_part_usd, 2)
        return converted_per_currency
        
    def convert_currency(self, how_much: float):
        """Function for convert the currency
        """
        converted_per_currency = self.get_currency_diffrences_and_convert()
        return how_much * converted_per_currency


cur = Currencies()
cur.add_currency("USD", 1, "USA")
cur.add_currency("RS", 0.013, "India")
cur.add_currency('DIRHAM', 0.27, 'UAE')
cur.add_currency("YEN", 0.0087, 'Japan')
cur.get_available_currencies()
print('___'*35)
cur_conv = Currency_Convertor("YEN", "RS")
op = cur_conv.convert_currency(10)
print(op)