import DB_Requests
import Admin_Console
from telebot import *
import mysql.connector
import Buttons


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="5689",
  database="race_db"
)

bot = telebot.TeleBot('6130887915:AAGsdSKt-u-zgCWQU7-mAV6Bhiy78to9WT8')




user_dict = {}

class User: #создаём класс юзер с параметрами
    def __init__(self, name):
        self.name = name
        self.accumulation_rub = 0
        self.income_rub = 0
        self.expense_rub = 0
        self.profit_rub = 0
        self.memory_sum = 0
        self.memory_sum_old = 0

@bot.message_handler(commands=['help', 'start']) #создаем декоратор принимающий команду на старт
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Введите x')
    bot.register_next_step_handler(msg, next_step_valuey) #ожидаем значение Х, после передаем его в функцию next_step_value

def next_step_valuey(message): #принимаем сообщение из прошлой функции
    chat_id = message.chat.id #задаем значения, вытаскивая переменный из тела письма
    name = message.from_user.id #задаем значения, вытаскивая переменный из тела письма
    userid = User(name) #создаём объект класса на основании полученного сообщения
    user_dict[chat_id] = userid #добавляем в словарь полученный объект класса
    print(user_dict)

    valuex = message.text #считываем текст сообщения пользователя
    userid = user_dict[chat_id] #приравниваем к userid значение в словаре по ключу id пользователя
    userid.valuex = valuex
    print(user_dict)

    msg = bot.send_message(message.chat.id, f'Введите y', parse_mode =
    'html')
    bot.register_next_step_handler(msg, next_step_valuesum)

def next_step_valuesum(message):
    chat_id = message.chat.id
    valuey = message.text
    userid = user_dict[chat_id]
    userid.valuey = valuey

    valuewalletsum = int(userid.valuex) + int(userid.valuey)
    userid.valuewalletsum = valuewalletsum


    bot.send_message(message.chat.id, f'x {userid.valuex} \n'
                                      f'y {userid.valuey} \n'    
                                      f'sum {userid.valuewalletsum}')


if __name__=='__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue