import telebot
import cases
import buttons
import re
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


bot = telebot.TeleBot('6450268677:AAGGV8QeP_le-662m1CwWtkH2DiG6MxqiEk')
costumer = {}
cases.add_cases('Кейс «Разлом»', 6000, 4,
                'data:image/jpeg;base64,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',
                'кейс разлом выпадающий в после операции "хищные воды"')
cases.add_cases('Гремучий кейс', 5000, 6,
                'data:image/jpeg;base64,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',
                'выпадает часто стоит средне')
cases.add_cases('Кейс "змеиный укус"', 3000, 2,
                'data:image/jpeg;base64,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',
                'самый дешевый кейс последнего года в игре ')


@bot.message_handler(commands=['start'])
def start_bot(message):
    user_id = message.from_user.id
    print(user_id)
    print(message)
    skan = cases.skan(user_id)

    if skan:
        product = cases.get_case_name_id()
        print(product)
        bot.send_message(user_id, 'Здравствуйте!', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Зарегистрируйтесь', buttons.main(product))
    elif not skan:
        bot.send_message(user_id, 'Отправьте ваш ник в стиме')
    bot.register_next_step_handler(message, get_nick)


def get_nick(message):
    user_id = message.from_user.id
    user = message.text
    bot.send_message(user_id, 'Отправьте вашу трейд ссылку', reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, user_id, user)


# noinspection PyUnreachableCode
def get_trade(message, name, email):
    user_id = message.from_user.id

    if re.fullmatch(regex, email):
        cases.register(user_id, name, email)
        bot.send_message(user_id, 'Вы в внесены в базу', reply_markup=telebot.types.ReplyKeyboardRemove())
        products = cases.get_case_name_id()
        bot.send_message(user_id, 'Выберите опцию', reply_markup=buttons.main(products))
        return True
    else:
        bot.send_message(user_id, 'Отправьте вашу ссылку корректнее')
        return False

    bot.register_next_step_handler(mmessage, group_chat, user_id, email)


@bot.callback_query_handler(lambda call: call.data in ['plus', 'minus', 'add_cart', 'back'])
def get_product_count(call):
    user_id = call.message.chat.id
    if call.data == 'plus':
        actual = costumer[user_id]['product_quantity']
        costumer[user_id]['product_quantity'] += 1
        bot.edit_message_reply_markup(chat_id=user_id, message_id=call.message.message_id,
                                      reply_markup=buttons.choose_count('plus', actual))

    elif call.data == 'minus':
        actual = costumer[user_id]['product_quantity']

        costumer[user_id]['product_quantity'] -= 1
        bot.edit_message_reply_markup(chat_id=user_id, message_id=call.message.message_id,
                                      reply_markup=buttons.choose_count('minus', actual))

    elif call.data == 'back':
        products = cases.get_case_name_id()
        bot.edit_message_text('Выберите пункт меню', user_id, call.message.message_id,
                              reply_markup=buttons.main(products))

    elif call.data == 'add_cart':
        product_count = costumer[user_id]['product_quantity']
        user_product = costumer[user_id]['pr_name']

        cases.append(user_id, user_product, product_count)
        products = cases.get_case_name_id()
        bot.edit_message_text('Продукт был добавлен в вашу корзину\n Что-то ещё?',
                              user_id, call.message.message_id,
                              reply_markup=buttons.main(products))

    elif call.data == 'delete':
        product_count = costumer.pop('product quantity')
        cases.remove(product_count)
        bot.edit_message_text('Продукт был успешно удалён', user_id, call.message.message_id,
                              reply_markup=buttons.main(product_count))

def group_chat(message, user_id, user_nick, email):
    user_id = message.text
    bot.send_message(-1001500295547, f'New order!\n\n Client name {user_nick}\n'
                                          f'trade link {email}')

    bot.send_message(user_id, 'Successfull')
    bot.register_next_step_handler(message, start_bot)

@bot.callback_query_handler(lambda call: call.data in ['order', 'cart', 'clear_cart'])
def main_menu(call):
    user_id = call.message.chat.id
    message_id = call.message.user_id
    if call.data == 'order':
        bot.delete_message(user_id, message_id)
        bot.register_next_step_handler(call.message, start_bot)
    elif call.data == 'cart':
        user_cart = cases.get_cart(user_id)

        full = 'Ваша корзина:\n\n'
        total = 0

        for i in user_cart:
            full += f'{i[0]} * {i[1]} = {i[2]}\n'
            total += i[2]

        full = f'\n Всего ко оплате: {total}'

        bot.edit_message_text(full, user_id, message_id, reply_markup=buttons.get_cart())






bot.infinity_polling()