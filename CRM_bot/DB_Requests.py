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

def PIN_check(message2, i):
    mycursor = mydb.cursor(buffered=True)
    sql = f'Select Point_{pin_codes.index(i)} from race_db.competitors where race_db.competitors.name = "{message2.from_user.username}"'
    mycursor.execute(sql)
    q = mycursor.fetchall()
    print(f'{i}:{q}')
    mydb.commit()

    if q[0][0] == None:
        bot.send_message(message2.chat.id,
                         "Вы не ввели PIN-код от предыдущего контрольного пункта. Ввод данного PIN-кода недопустим.")
        return 'stop cycle'

def Point_check(message2, i):
    mycursor = mydb.cursor(buffered=True)
    sql = f'Select Point_{pin_codes.index(i) + 1} from race_db.competitors where race_db.competitors.name = "{message2.from_user.username}"'
    mycursor.execute(sql)
    mydb.commit()
    None_check = mycursor.fetchall()[0][0]
    return None_check

def Point_update(message2, i):
    mycursor = mydb.cursor()
    sql = f'Update race_db.competitors Set race_db.competitors.Point_{pin_codes.index(i) + 1} = SYSDATE() where race_db.competitors.name = "{message2.from_user.username}";'
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()

def admin_id_call():
    mycursor = mydb.cursor(buffered=True)
    sql = f'Select Count(id) FROM race_db.admin'
    mycursor.execute(sql)
    mydb.commit()

    telegram_id = mycursor.fetchall()[0][0]

    return telegram_id

def start(start_message):
    mycursor = mydb.cursor(buffered=True)
    sql = f'Select Name from race_db.competitors where race_db.competitors.name = "{start_message.from_user.username}"'
    mycursor.execute(sql)
    mydb.commit()
    None_check = mycursor.fetchall()
    mycursor.close()
    return None_check

def registration(registration):
    mycursor = mydb.cursor()
    sql = "INSERT INTO race_db.competitors (Name) VALUES ( %s)"
    val = (registration)  # Не забудьте проверку на длину списка!
    mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()

def registration_admin(registration_admin, password):
    mycursor = mydb.cursor()
    sql = "INSERT into race_db.admin (Telegram_Name, Passwrd) VALUES (%s, %s)"
    val = [registration_admin, password]  # Не забудьте проверку на длину списка!
    print(val)
    mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()