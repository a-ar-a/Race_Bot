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
        bot.send_message(start_message.chat.id, 'Добро пожаловать на заезд.\n\n'
                                                'Цель гонки - быстрее всех найти контрольные пункты и приехать на финиш.\n\n'
                                                'На каждом пункте есть PIN-код, при вводе которого ты получишь координаты следующей контрольной точки.\n\n'
                                                'PIN-код для получения следующих координат:\n\n'
                                                '1111')

    else:
        bot.send_message(start_message.chat.id,
                         'Добро пожаловать на заезд.\n\n'
                         'Цель гонки - быстрее всех найти контрольные пункты и приехать на финиш.\n\n'
                         'На каждом пункте есть PIN-код, при вводе которого ты получишь координаты следующей контрольной точки.\n\n'
                         'PIN-код для получения координат первого контрольного пункта введи:\n\n'
                         '1111')



@bot.message_handler(commands=pin_codes)
def codes(message_pin_codes):
    markup = types.InlineKeyboardMarkup()

    text = str(message_pin_codes.text).strip('/')

    if text not in pin_codes:
        bot.send_message(message_pin_codes.chat.id, f"Введён неверный PIN-код")

    for i in pin_codes:
        if i == text:
            if pin_codes.index(i) > 0:
                pin_check = DB_Requests.PIN_check(message_pin_codes, i)

                if pin_check == 0:
                    break

            point_check = DB_Requests.Point_check(message_pin_codes, i)
            print('Point_check before cycle:', point_check)

            if point_check[0][0] == None:
                print(f'Point_check after_cycle = {point_check}')
                markup.add(types.InlineKeyboardButton('Отметка на карте', url=url_list[pin_codes.index(i)]))
                bot.send_message(message_pin_codes.chat.id,
                               f"Вы собрали {pin_codes.index(i) + 1}/{len(pin_codes)} контрольных пунктов.\n"
                               f"Следующий пункт:\n"
                               f"{points[i]}\n"
                               f"Введи следующий PIN-код для получения дальнейших указаний.",
                               reply_markup=markup)

                DB_Requests.Point_update(message_pin_codes, i)

            else:
                bot.send_message(message_pin_codes.chat.id,
                             "Вы уже ввели данный PIN-код. Проследуйте к следующему пункту.")

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
    buttons_callback = {'became_admin': admin_script,
                        'Password_right': Buttons.Password_right,
                        'Type_again': admin_script,
                        'Stop_registration': Buttons.Stop_registration
                        }
    button = buttons_callback[callback.data]
    if callback.data == 'became_admin':
        count_admin_check = DB_Requests.admin_id_call()
        print(count_admin_check)
        name_admin_check = DB_Requests.admin_check(callback)
        if name_admin_check == [] and count_admin_check < 4:
                button(callback)
        if count_admin_check >= 4:
            bot.send_message(callback.from_user.id,
                             "Достигнуто максимальное количество администраторов.")

        if name_admin_check != []:
            bot.send_message(callback.from_user.id,
            'Вы уже являетесь администратором.')
    else:
        button(callback)




def admin_script(admin_message):
    Buttons.quick_delete_message(admin_message.message.chat.id, admin_message.message.message_id)

    sent = bot.send_message(admin_message.from_user.id, "Твой аккаунт телеграмм будет зарегистрирован.\n"
                                                      "Для завершения регистрации придумай пароль.")
    bot.register_next_step_handler(sent, Admin_Console.create_password)

    Buttons.quick_delete_message(admin_message.message.chat.id, admin_message.message.message_id-1)
    Buttons.quick_delete_message(admin_message.message.chat.id, admin_message.message.message_id)


temp = str()
adress = str()

@bot.message_handler(content_types=['text'])
def message(incoming_messages):
    global temp
    global adress
    text = incoming_messages.text

    temp = text
    adress = incoming_messages
    bot.send_message(incoming_messages.chat.id,
                     'Принято')
    return text

def review(incoming_messages):
    message_to_save = incoming_messages
    return message_to_save





if __name__=='__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue