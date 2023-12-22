from Functons.WB_API import get_price
from Functons.WB_API import get_stat
from Functons.Json_functions import count_transaction, save_to_json, create_cards, update_info_cars
from Functons.Push_to_SQL import push_first_data_to_mySQL, add_column
from Functons.Classes import Cards


def main():
    file_path = r"C:\\Users\\lenovo\\PycharmProjects\\wb_test\\"

    price_data = get_price()
    save_to_json(price_data, 'price_info', file_path)
    # create_cards(file_path)
    # update_info_cars(file_path, '2023-11-20', '2023-11-26')

    date_from = input('input date from: (YYYY-MM-DD):')
    date_to = input('input date to (YYYY-MM-DD):')

    stat_data = get_stat(date_from, date_to)
    save_to_json(stat_data, f'stat_info_from_{date_from}_to_{date_to}', file_path)

    # count_data = count_transaction(file_path, date_from, date_to)

    # column_name = f'sold {date_from} {date_to}'
    # column_definition = 'INT'

    # add_column(column_name)
    # push_first_data_to_mySQL(count_data)
    return None
# гит ты работаешь?


if __name__ == "__main__":
    main()
