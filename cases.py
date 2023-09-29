import sqlite3
from datetime import datetime

db = sqlite3.connect('my_inventory.db')

inventory = db.cursor()


inventory.execute('CREATE TABLE IF NOT EXISTS user'
                  '(nick TEXT, trade_link TEXT, telegram_id INT, date DATETIME);')

inventory.execute('CREATE TABLE IF NOT EXISTS store'
                  '(product_id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT, price REAL, product_quantity INT, product_des TEXT,  photo TEXT, product_data DATETIME);')

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

def check_case(name):
    db = sqlite3.connect('my_inventory.db')

    inventory = db.cursor()

    check = inventory.execute('SELECT product_name, product_quantity FROM store WHERE product_name=?;', (name, )).fetchone()

    if check:
        return check
    else:
        return False


def add_cases(product_name, price, product_quantity, photo, product_des):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()
    checker = check_case(product_name)
    if checker != False:
        # try:
        new_quantity = product_quantity + checker[1]
        inventory.execute('UPDATE store SET product_quantity=? WHERE product_name=?;', (new_quantity, product_name))
        # except:
        #     pass
    else:
        inventory.execute('INSERT INTO store'
                        '(product_name, price, product_quantity, product_des, photo, product_data) VALUES'
                        '(?, ?, ?, ?, ?, ?);', (product_name, price, product_quantity, product_des, photo, datetime.now()))
    db.commit()


def get_case_name_id():
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    product = inventory.execute('SELECT product_id, product_name, product_quantity FROM store;').fetchall()

    sorted_pr = [(i[1], i[0]) for i in product if i[2] > 0]

    return sorted_pr


def get_cs_id():
    db = sqlite3.connect('my_inventory.db')

    inventory = db.cursor()

    product = inventory.execute('SELECT product_id, product_quantity FROM store;').fetchall()
    sorted_pr = [(i[0]) for i in product if i[1] > 0]

    return sorted_pr


def get_case_id(product_id):
    db = sqlite3.connect('my_inventory.db')

    inventory = db.cursor()

    product_id = inventory.execute('SELECT *'
                                   'FROM store WHERE product_id=?;', (product_id, )).fetchone()[2]
    print(product_id)
    return product_id


def append(user_id, user_product, quantity):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    price_case = get_case_id(user_product)

    inventory.execute('INSERT INTO cart'
                      '(user_id, user_product, quantity, total)'
                      'VAlUES (?, ?, ?, ?);', (user_id, user_product, quantity, quantity * price_case))
    db.commit()


def remove(user_id):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    inventory.execute('DELETE FROM cart WHERE user_id=?;', (user_id, ))


def get_cart(user_id):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    user_cart = inventory.execute('SELECT store.product_name, cart.quantity, cart.total FROM store INNER JOIN cart ON store.product_id=cart.user_product WHERE cart.user_id=?;',
                                  (user_id, )).fetchall()

    print(user_cart)

    return user_cart


def get_user_trade_link(user_id):
    db = sqlite3.connect('my_inventory.db')
    inventory = db.cursor()

    trade_link = inventory.execute('SELECT nick, trade_link FROM user WHERE telegram_id=?;', (user_id, ))

    return trade_link.fetchone()

