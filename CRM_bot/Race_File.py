import Main_Race_File
import DB_Requests

from telebot import *
import mysql.connector


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

@bot.message_handler(commands=['start'])
def start(start_message):

    None_check = DB_Requests.start(start_message)
    if None_check == []:
        registration = []
        registration.append(start_message.from_user.username)
        DB_Requests.registration(registration)
        bot.send_message(start_message.chat.id, 'Добро пожаловать на заезд.\n\nЦель гонки - быстрее всех найти контрольные пункты и приехать на финиш.\n\nНа каждом пункте есть PIN-код, при вводе которого ты получишь координаты следующей контрольной точки.\n\nPIN-код для получения следующих координат:\n\n1111')

    else:
        bot.send_message(start_message.chat.id,
                         'Добро пожаловать на заезд.\n\n'
                         'Цель гонки - быстрее всех найти контрольные пункты и приехать на финиш.\n\n'
                         'На каждом пункте есть PIN-код, при вводе которого ты получишь координаты следующей контрольной точки.\n\n'
                         'PIN-код для получения координат первого контрольного пункта введи:\n\n'
                         '1111')


adress = Main_Race_File.adress
user_message = Main_Race_File.temp
if user_message == 'Залупа':
    bot.send_message(adress.from_user.username, 'Принято')


if __name__=='__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue