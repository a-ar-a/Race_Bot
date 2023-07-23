from telebot import *
import DB_Requests
import Race_Func_Bot
import mysql.connector
import Main_Race_File
import Buttons

bot = telebot.TeleBot('6130887915:AAGsdSKt-u-zgCWQU7-mAV6Bhiy78to9WT8')


user_dict = {}

class Admin_Reg: #создаём класс юзер с параметрами
    def __init__(self, name):
        self.name = name

def create_password(password_message):

    chat_id = password_message.chat.id  # задаем значения, вытаскивая переменный из тела письма
    name = password_message.from_user.id  # задаем значения, вытаскивая переменный из тела письма
    userid = Admin_Reg(name)  # создаём объект класса на основании полученного сообщения
    user_dict[chat_id] = userid

    #Buttons.quick_delete_message(password_message.chat.id, password_message.id)
    #Buttons.quick_delete_message(password_message.chat.id, password_message.id-1)



    password = password_message.text
    userid = user_dict[chat_id]
    userid.password = password

    answer(password_message)

def answer(password_message):
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton('Пароль верен', callback_data='Password_right'))
    markup.add(types.InlineKeyboardButton('Ввести заново', callback_data='Type_again'))
    markup.add(types.InlineKeyboardButton('Отменить регистрацию', callback_data='Stop_registration'))

    bot.send_message(password_message.chat.id,
                     f'Подтверди правильность пароля: {user_dict[password_message.chat.id].password}', reply_markup=markup)




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


