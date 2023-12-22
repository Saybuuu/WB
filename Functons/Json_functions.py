import json
from typing import Any
from Functons.Classes import Cards


def create_cards(path: str) -> list:
    with open(f'{path}price_info.json', 'r', encoding='utf-8') as price_file:
        price_information = json.load(price_file)

    list_of_cards = []

    for item in price_information:
        new_card = {
            'article': item['nmId']
        }

        list_of_cards.append(new_card)

    return list_of_cards


# def update_info_cars(path, date_from, date_to): #НЕ ДОДЕЛАННО
#     with open(f'{path}stat_info_from_{date_from}_to_{date_to}.json', 'r', encoding='utf-8') as stat_file:
#         sell_statistics_info = json.load(stat_file)
#
#     for item in sell_statistics_info:
#
#         New_card = {
#             'Article': item['nm_id'],
#             'Price': item["retail_price"],
#             'Sales': item["quantity"],
#             'Brand_name': item["brand_name"],
#             'Product_name': item["subject_name"]
#         }
#     return None


def count_transaction(path: str, date_from: str, date_to: str) -> list:
    with open(f'{path}price_info.json', 'r', encoding='utf-8') as file:
        price_info = json.load(file)

    with open(f'{path}stat_info_from_{date_from}_to_{date_to}.json', 'r', encoding='utf-8') as file2:
        sell_statistics_info = json.load(file2)

    count_dict = {}

    Sell_statistics_info_card = []

    for items in price_info:
        article_ = items['nmId']
        count_dict[article_] = 0

    for item in sell_statistics_info:
        value = item['nm_id']

        if value in count_dict:
            count_dict[value] += item["quantity"]

        New_card = {
            'Article': item['nm_id'],
            'Price': item["retail_price"],
            'Sales': count_dict[item['nm_id']],
            'Brand_name': item["brand_name"],
            'Product_name': item["subject_name"]
        }

        key_to_check = 'Article'
        value_to_check = item['nm_id']

        for dict_ in Sell_statistics_info_card:
            if dict_[key_to_check] == value_to_check:
                Sell_statistics_info_card.remove(dict_)

        Sell_statistics_info_card.append(New_card)

    return Sell_statistics_info_card


def save_to_json(data: Any, fileName: str, path: str):
    with open(F'{path}{fileName}.json', 'w', encoding='utf-8') as info:
        json.dump(data, info, ensure_ascii=False, indent=4)
    print(f"Данные успешно записаны в файл '{fileName}.json'")
    return None
