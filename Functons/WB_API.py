import requests


def get_price() -> list[dict]:
    """

    :param dateFrom: use format YYYY-MM-DD (string)
    :param dateTo: use format YYYY-MM-DD (string)
    :return: info about all opened cards

    """
    token_price = 'eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjMxMDI1djEiLCJ0eXAiOiJKV1QifQ' \
                  '.eyJlbnQiOjEsImV4cCI6MTcxNjQ0NjkzNSwiaWQiOiI5ODM0YzMzNC0xMTdhL' \
                  'TQ1MDktYTEzYy1lNzhiNzk0YjNjM2IiLCJpaWQiOjg2MDU2NDEyLCJvaWQiOjg' \
                  'zOTQ5MiwicyI6MTA3Mzc0MTgzMiwic2lkIjoiYzFkY2Y4NDctMGVmNS00NGMxL' \
                  'Tk2NmEtZjAyN2YwM2U5MGIzIiwidWlkIjo4NjA1NjQxMn0._LUIjly0QapabyqZ' \
                  'NoQCMH33ORHLQPEw0F8HaDsothF0M0TzggECcthHbnoWk3_Kz3bc1yqWaoUVWf4' \
                  'R5Ie21A '

    headers = {
        'Authorization': f'{token_price}'
    }

    price_response = requests.get(url='https://suppliers-api.wildberries.ru/public/api/v1/info', headers=headers)

    if price_response.status_code == 200:
        data = price_response.json()

        # with open('../price_info.json', 'w', encoding='utf-8') as price_info:
        #     json.dump(data, price_info, ensure_ascii=False, indent=4)
        # print("Данные успешно записаны в файл 'price_info.json'")
    else:
        print(f"Ошибка запроса: {price_response.status_code}")
        print("Текст ошибки:", price_response.text)
    return data


def get_stat(dateFrom: str, dateTo: str) -> list[dict]:
    """

    :param dateFrom: use format YYYY-MM-DD (string)
    :param dateTo: use format YYYY-MM-DD (string)
    :return: Sales report

    """
    token_stat = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjMxMDI1djEiLCJ0eXAiOiJKV1QifQ" \
                 ".eyJlbnQiOjEsImV4cCI6MTcxNzE0MTEwNywiaWQiOiI5ZWFmNDc3Mi1jZWVjL" \
                 "TQxN2UtOTFiYi1lOWVjMDZhMjBhNDQiLCJpaWQiOjg2MDU2NDEyLCJvaWQiOjg" \
                 "zOTQ5MiwicyI6MTA3Mzc0MTg1Niwic2lkIjoiYzFkY2Y4NDctMGVmNS00NGMxL" \
                 "Tk2NmEtZjAyN2YwM2U5MGIzIiwidWlkIjo4NjA1NjQxMn0.jbVguOL_Bwq65rn" \
                 "hqWVwS8fr0uoRW_3AYE4TrXlJT1-V5Kr67k0D4Zi4xPbLUzN2IfPsfHv40k0cTEUahO9vVQ "

    headers = {
        'Authorization': f'{token_stat}'
    }

    params = {
        'dateFrom': f'{dateFrom}',
        'dateTo': f'{dateTo}',
        'rrdid': '0',
        'limit': '1000000'
    }

    url = 'https://statistics-api.wildberries.ru/api/v1/supplier/reportDetailByPeriod'

    stat_response = requests.get(url=url, params=params, headers=headers)

    if stat_response.status_code == 200:
        stat_data = stat_response.json()

        # with open('../stat_info.json', 'w', encoding='utf-8') as stat_info:
        #     json.dump(data, stat_info, ensure_ascii=False, indent=4)
        #     print('Данные успешно сохранены в файл "stat_info.json"')
    else:
        print(f'Статус ошибки:{stat_response.status_code}')
        print('Текст ошибки:', stat_response.text)
    return stat_data
