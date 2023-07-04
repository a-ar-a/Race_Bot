import Admin_Console
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


@bot.message_handler(commands=['admin_console'])
def admin(message0):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Стать админом', callback_data='became_admin'))
    markup.add(types.InlineKeyboardButton('Открыть редактор', callback_data='open_redactor'))
    bot.send_message(message0.chat.id,
                     'Выберите необходимое действие',
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_messages(callback):
    if callback.data == 'became_admin':
        count_admin_check = admin_id_call()
        print(count_admin_check)
        if count_admin_check < 4:
            Admin_Console.admin_script(None)

        else:
            bot.send_message(callback.from_user.id,
                             "Достигнуто максимальное количество администраторов.")



@bot.message_handler(commands=['start'])
def start(message1):
    start()

    if None_check == []:

        registration = []
        registration.append(message1.from_user.username)
        mycursor = mydb.cursor()
        sql = "INSERT INTO race_db.competitors (Name) VALUES ( %s)"
        val = (registration)  # Не забудьте проверку на длину списка!
        mycursor.execute(sql, val)

        mydb.commit()
        mycursor.close()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message1.chat.id, 'Добро пожаловать на заезд.\n\nЦель гонки - быстрее всех найти контрольные пункты и приехать на финиш.\n\nНа каждом пункте есть PIN-код, при вводе которого ты получишь координаты следующей контрольной точки.\n\nPIN-код для получения следующих координат:\n\n1111', reply_markup=markup)
        mycursor.close()
    else:
        bot.send_message(message1.chat.id,
                         'Добро пожаловать на заезд.\n\nЦель гонки - быстрее всех найти контрольные пункты и приехать на финиш.\n\nНа каждом пункте есть PIN-код, при вводе которого ты получишь координаты следующей контрольной точки.\n\nPIN-код для получения координат первого контрольного пункта введи:\n\n1111')


@bot.message_handler(content_types=['text'])

def codes(message2):
    markup = types.InlineKeyboardMarkup()

    text = message2.text

    if text not in pin_codes:
        bot.send_message(message2.chat.id, f"Введён неверный PIN-код")

    for i in pin_codes:
        if i == text:
            if pin_codes.index(i) > 0:
                print(pin_codes.index(i))
                pin_check = PIN_check(message2, i)
                if pin_check == 'stop cycle':
                    break

            point_check = Point_check(message2, i)

            if point_check == None:

                markup.add(types.InlineKeyboardButton('Отметка на карте', url=url_list[pin_codes.index(i)]))
                bot.send_message(message2.chat.id, f"Вы собрали {pin_codes.index(i)+1}/{len(pin_codes)} контрольных пунктов.\nСледующий пункт:\n{points[i]}\nВведи следующий PIN-код для получения дальнейших указаний.", reply_markup=markup)

                Point_update(message2, i)

            else:
                bot.send_message(message2.chat.id,
                                         "Вы уже ввели данный PIN-код. Проследуйте к следующему пункту.")




if __name__=='__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue


