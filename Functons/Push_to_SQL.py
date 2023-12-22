import mysql.connector


def push_first_data_to_mySQL(data: list[dict]):
    my_db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Oop123_S',
        port='3306',
        database='test_db'
    )

    cursor = my_db.cursor()

    try:
        for card in data:
            check_duplicate_query = (
                "SELECT * FROM opened_cards "
                "WHERE Article = %(Article)s AND Price = %(Price)s AND Sales = %(Sales)s "
                "AND Brand_name = %(Brand_name)s AND Product_name = %(Product_name)s"
            )

            cursor.execute(check_duplicate_query, card)
            existing_record = cursor.fetchone()

            if not existing_record:
                add_card = ("INSERT INTO opened_cards"
                            "(Article, Price, Brand_name, Product_name, Sales)"
                            "VALUES (%(Article)s, %(Price)s, %(Brand_name)s, %(Product_name)s, %(Sales)s)")

                new_data_in_card = {
                    'Article': card.get('Article', None),
                    'Price': card.get('Price', None),
                    'Brand_name': card.get('Brand_name', None),
                    'Product_name': card.get('Product_name', None),
                    'Sales': card.get('Sales', None)
                }
                cursor.execute(add_card, new_data_in_card)

        my_db.commit()

    except Exception as exception_:
        print(f"Ошибка: {exception_}")
        my_db.rollback()

    finally:
        print('Данный записаны в базу')
        cursor.close()
        my_db.close()

    return None


def add_column(column_name):
    my_db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Oop123_S',
        port='3306',
        database='test_db'
    )

    cursor = my_db.cursor()

    alter_query = (
        "ALTER TABLE opened_cards "
        f"ADD COLUMN sold_{column_name} DATE"
    )

    try:
        cursor.execute(alter_query)
        # my_db.commit()
        print(f'Колонка {column_name} добавлена')

    except Exception as ex:
        print(f'Произошла ошибка{ex}')

    finally:
        cursor.close()
        my_db.close()
