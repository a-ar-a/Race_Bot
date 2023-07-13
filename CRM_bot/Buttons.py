from telebot import *
import Main_Race_File
import mysql.connector
import Admin_Console
import DB_Requests
import time
import pprint



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="5689",
  database="race_db"
)

bot = telebot.TeleBot('6130887915:AAGsdSKt-u-zgCWQU7-mAV6Bhiy78to9WT8')

coordinats = ['60.01497128546239, 30.387450096732746', '60.013855616292474, 30.392593654153046', '60.0132858799618, 30.39950397565958', '60.01683896715482, 30.401275701810054']
pin_codes = ['1111', '1234', '2345', '3456']
url_list = ['https://is.gd/jlRZ4H', 'https://is.gd/aHW19l', 'https://is.gd/qV9LUl', 'https://is.gd/GJX9bG']
points = dict(zip(pin_codes, coordinats))

def password_reply(message):
    password = []
    password.append(Main_Race_File.message)
    if len(password) == 0:
        password_reply(message)
    else:
        Admin_Console.create_password(message)


def Stop_registration(callback):
    bot.send_message(callback.from_user.id,
                     'Регистрация отменена')
    long_delete_message(callback.message.chat.id, callback.message.message_id)
    long_delete_message(callback.message.chat.id, callback.message.message_id+1)


def Password_right(callback):
    print(callback)
    registration_admin = []
    registration_admin.append(callback.from_user.username)
    password = []
    password.append(Admin_Console.prepassword)

    DB_Requests.registration_admin(registration_admin[0], password[0])
    bot.send_message(callback.from_user.id,
                     'Регистрация выполнена успешно!')
    quick_delete_message(callback.message.chat.id, callback.message.id)
    long_delete_message(callback.message.chat.id, callback.message.id + 1)

def Type_again(callback):
    Admin_Console.create_password(callback)

def long_delete_message(chat_id, message_id):
    time.sleep(5)
    bot.delete_message(chat_id, message_id)

def quick_delete_message(chat_id, message_id):
    bot.delete_message(chat_id, message_id)
