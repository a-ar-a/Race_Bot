from telebot import *
import DB_Requests
import Race_Func_Bot
import mysql.connector
import Main_Race_File
import Buttons

bot = telebot.TeleBot('6130887915:AAGsdSKt-u-zgCWQU7-mAV6Bhiy78to9WT8')
prepassword = ''


def create_password(password_message):
    global prepassword
    Buttons.quick_delete_message(password_message.chat.id, password_message.id)
    Buttons.quick_delete_message(password_message.chat.id, password_message.id-1)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Пароль верен', callback_data='Password_right'))
    markup.add(types.InlineKeyboardButton('Ввести заново', callback_data='Type_again'))
    markup.add(types.InlineKeyboardButton('Отменить регистрацию', callback_data='Stop_registration'))

    password = password_message.text
    prepassword = password
    bot.send_message(password_message.chat.id,
                     f'Подтверди правильность пароля: {password}', reply_markup=markup)

    return password


# @bot.callback_query_handler(func=lambda callback: True)
# def registration_reply(reg_callback):
#     if reg_callback.data == 'Password_right':
#         registration = []
#         registration.append(reg_callback.from_user.username)
#         DB_Requests.registration(registration)
#         bot.send_message(reg_callback.chat.id,
#                          'Регистрация выполнена успешно!')
#
#         Buttons.long_delete_message(reg_callback.chat.id, reg_callback.id)
#         Buttons.long_delete_message(reg_callback.chat.id, reg_callback.id - 1)
#     if reg_callback.data == 'Type_again':
#         pass
#     if reg_callback.data == 'Stop_registration':
#         pass


