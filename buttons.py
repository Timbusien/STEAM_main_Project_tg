from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def choice_buttons():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    register = types.KeyboardButton('Регистрация')
    buttons.add(register)

    return buttons


def main(get_case_name_id):
    buttons = InlineKeyboardMarkup()
    order = InlineKeyboardButton(text='Оформление', callback_data='order')
    cart = InlineKeyboardButton(text='Ваша Корзина', callback_data='cart')
    all_products = [InlineKeyboardButton(text=f'{i[0]}', callback_data=str(i[1])) for i in get_case_name_id()]
    buttons.row(order)
    buttons.add(*all_products)
    buttons.row(cart)

    return buttons


def choose_count(plus_or_minus='', current_ammount=1):
    buttons = InlineKeyboardMarkup(row_width=3)
    plus = InlineKeyboardButton(text='+', callback_data='plus')
    minus = InlineKeyboardButton(text='-', callback_data='minus')
    count =InlineKeyboardButton(text=str(current_ammount), callback_data=str(current_ammount))
    add_cart = InlineKeyboardButton(text='Добавить в вашу Корзину', callback_data='add_cart')
    back = InlineKeyboardButton(text='Назад', callback_data='back')
    delete = InlineKeyboardButton(text='Удалить продукт', callback_data='delete')

    if plus_or_minus == 'plus':
        new_ammount = int(current_ammount)
        count = InlineKeyboardButton(text=str(new_ammount), callback_data='delete')

    elif plus_or_minus == 'minus':
        if int(current_ammount) > 1:
            new_ammount = int(current_ammount) - 1
            count = InlineKeyboardButton(text=str(new_ammount), callback_data=str(new_ammount))

    buttons.add(minus, count, plus)
    buttons.row(add_cart)
    buttons.row(back)
    buttons.row(delete)

    return buttons


def get_cart():
    buttons =InlineKeyboardMarkup(row_width=1)
    cls = InlineKeyboardButton('Очистить Корзину', callback_data='cls')
    order = InlineKeyboardButton('Оформить заказ', callback_data='order')
    back = InlineKeyboardButton('Назад', callback_data='back')
    buttons.add(cls, order, back)

    return buttons

