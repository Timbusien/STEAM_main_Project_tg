import sqlite3
from datetime import datetime

db = sqlite3.connect('my_inventory.db')

inventory = db.cursor()


inventory.execute('CREATE TABLE IF NOT EXISTS user'
                  '(nick TEXT, trade_link TEXT, telegram_id INT, date DATETIME)')

inventory.execute('CREATE TABLE IF NOT EXISTS store'
                  '(product_name TEXT, product_des TEXT, price REAL, product_id INTEGER PRIMARY KEY AUTOINCREMENT, product_quantity INT, product_data DATETIME, photo TEXT)')

inventory.execute('CREATE TABLE IF NOT EXISTS cart'
                  '(user_id INT, user_product TEXT, quantity INT, total REAL);')


def register(telegram_id, nick, email):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    inventory.execute('INSERT INTO user'
                      '(telegram_id, nick, trade_link, date) VALUES'
                      '(?, ?, ?, ?);', (telegram_id, nick, email, datetime.now()))
    db.commit()

def skan(user_id):
    db = sqlite3.connect('my_inventory.db')

    inventory = db.cursor()

    check = inventory.execute('SELECT telegram_id FROM user WHERE telegram_id=?;', (user_id, ))

    if check.fetchone():
        return True
    else:
        return False


def add_cases(product_name, price, product_quantity, photo, product_des):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    inventory.execute('INSERT INTO store'
                      '(product_name, price, product_quantity, product_des, photo, product_data) VALUES'
                      '(?, ?, ?, ?, ?, ?);', (product_name, price, product_quantity, product_des, photo, datetime.now()))
    db.commit()


def get_case_name_id():
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    product = inventory.execute('SELECT product_name, product_id, product_id, product_quantity FROM store;').fetchall()
    sorted_pr = [(i[0], i[1]) for i in product if i[2] > 0]

    return sorted_pr


def get_case_id(product_id):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    product = inventory.execute('SELECT product_name, product des, photo, price'
                                'FROM store WHERE product_id=?;', (product_id, )).fetchone()


    return product


def append(user_id, user_product, quantity):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    price_case = get_case_id(user_product)[2]

    inventory.execute('INSERT INTO cart'
                      '(user_id, user_product, quntity)'
                      'VAlUES (?, ?, ?);', (user_id, user_product, quantity, quantity * price_case))
    db.commit()


def remove(product_id):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    inventory.execute('DELETE FROM cart WHERE user_product=?;', (product_id, ))


def get_cart(user_id):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    user_cart = inventory.execute('SELECT store.product_name, cart.quantity, cart.total, FROM store INNER JOIN cart ON store.user_product WHERE user_id=?;', (user_id, )).fetchall()

    return user_cart



