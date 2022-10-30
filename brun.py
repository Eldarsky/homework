import sqlite3
from sqlite3 import Error
def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)







def create_product(conn, product: tuple):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)



def create_products(conn):
    create_product(conn, ('Кефир', 17.80, 7))  # 1
    create_product(conn, ('Мороженое: Бахрома', 60.53, 30))  # 2
    create_product(conn, ('Пепси 2л', 135.00, 4))  # 3
    create_product(conn, ('NITRO', 62.40, 12))  # 4
    create_product(conn, ('Контик', 34.90, 5))  # 5
    create_product(conn, ('Жидкое мыло', 67.89, 2))  # 6
    create_product(conn, ('Мыло детское', 108.60, 7))  # 7
    create_product(conn, ('Кириешки Flint', 26.12, 20))  # 8
    create_product(conn, ('Семечки Джин', 59.99, 6))  # 9
    create_product(conn, ('Гамбургер "Тойбосс"', 105.00, 3))  # 10
    create_product(conn, ('Alpen Gold', 114.59, 4))  # 11
    create_product(conn, ('Asu!', 33.40, 8))  # 12
    create_product(conn, ('Моющее средство', 73.70, 4))  # 13
    create_product(conn, ('Порошок', 250.00, 3))  # 14
    create_product(conn, ('Подсолнечное Масло', 240.00, 5))  # 15
def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)
def update_product_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)
def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)
def select_product(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
def search_by_price_and_quantity(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100.00 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
connection = create_connection(r"hw.db")
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
PRODUCT_TITLE VARCHAR(200) NOT NULL,
PRICE DOUBLE(10,2) NOT NULL DEFAULT 0.0,
QUANTITY INTEGER(5) NOT NULL DEFAULT 0,
)
'''

if connection is not None:
    print('Connected successfully')
    create_table(connection, sql_create_products_table)
    create_product(connection, (29.80, 5))
    update_product_quantity(connection, (8, 1))
    update_product_price(connection, (29.80, 5))
    delete_product(connection, 1)
    select_product(connection)
    print('---------------------------')
    search_by_price_and_quantity(connection)
    print('---------------------------')
    search_by_word(connection, 'мыло')
    print('---------------------------')
