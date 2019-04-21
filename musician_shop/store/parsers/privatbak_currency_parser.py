import datetime
import json
import urllib.request


def main():
    date_mode = "today"
    while True:
        today_date = set_date(date_mode)
        privatbank_dict = get_data_from_privatebank(today_date)

        if validate_data(privatbank_dict):
            break
        else:
            date_mode = "yesterday"
            continue

    curr_list = parse_pb_data(privatbank_dict)
    return curr_list


def validate_data(privatbank_dict):
    if privatbank_dict["exchangeRate"] == []:
        return False
    else:
        return True


def set_date(mode):
    now = datetime.datetime.now()
    if mode == "today":
        today_date = f"={now.day}.{now.month}.{now.year}"
    else:
        today_date = f"={now.day-1}.{now.month}.{now.year}"

    return today_date


def get_data_from_privatebank(today_date):
    url = "https://api.privatbank.ua/p24api/exchange_rates?json&date" + today_date
    my_req = urllib.request.urlopen(url)
    req_str = my_req.read().decode('utf-8')
    currency_dict = json.loads(req_str)

    return currency_dict


def parse_pb_data(privatbank_dict):
    all_currencies = privatbank_dict["exchangeRate"]
    all_currencies.pop(0)

    currency_list = []
    for current_currency_dict in all_currencies:
        if current_currency_dict["currency"] in ("EUR", "USD", "RUB"):
            currency_list.append((current_currency_dict["currency"], current_currency_dict["saleRateNB"]))

    return currency_list
