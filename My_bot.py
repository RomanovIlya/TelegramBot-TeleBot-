import telebot
from telebot import TeleBot
from telebot import types
import os

token='5525233414:AAFVldwNs5zJq3ikO-Z2BsNkqTbITkiOthw'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
  svaz = types.KeyboardButton("Соцсети")
  video = types.KeyboardButton("Мои проекты")
  talk = types.KeyboardButton("Отправить что-то автору")
  library = types.KeyboardButton("Книги по IT")
  markup.add(svaz, video, talk, library)
  bot.send_message(message.chat.id,f"Добро пожаловать. Нажми на одну из кнопок",reply_markup=markup)

@bot.message_handler(commands=['send'])
def per(message):
    back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton("Отмена")
    back_markup.add(btn_back)
    send_message = bot.send_message(message.chat.id,"Следующее сообщение увидет автор. Также можно отправлять фото, документ и видео размером до 20 мегабайт.", reply_markup=back_markup)
    bot.register_next_step_handler(send_message, talk_with1)

@bot.message_handler(commands=['social_network'])
def soc(message):
    smarkup = types.InlineKeyboardMarkup(row_width=1)
    tg = types.InlineKeyboardButton("Телеграмм канал", "https://t.me/progatiktok")
    discord=types.InlineKeyboardButton("Дискорд канал", "https://discord.gg/RpWywVhMSF")
    tiktok = types.InlineKeyboardButton("Тик-Ток", url="https://www.tiktok.com/@__programming__")
    smarkup.add(tg, discord,tiktok)
    bot.send_message(message.chat.id, "Вот мои соцсети:", reply_markup=smarkup)

@bot.message_handler(content_types=["text"])
def get_text(message):
  if message.text == 'Соцсети':
    smarkup = types.InlineKeyboardMarkup(row_width=1)
    tg = types.InlineKeyboardButton("Телеграмм канал", "https://t.me/progatiktok")
    discord=types.InlineKeyboardButton("Дискорд канал", "https://discord.gg/RpWywVhMSF")
    tiktok = types.InlineKeyboardButton("Тик-Ток", url="https://www.tiktok.com/@__programming__")
    smarkup.add(tg, discord,tiktok)
    bot.send_message(message.chat.id, "Вот мои соцсети:", reply_markup=smarkup)
  if message.text == 'Мои проекты':
    smarkup = types.InlineKeyboardMarkup(row_width=1)
    tg = types.InlineKeyboardButton("Python", "https://drive.google.com/drive/folders/1a5Hq4KiZ4ohl_NL_NIpjweRwe74H3Llq?usp=sharing")
    discord=types.InlineKeyboardButton("C++", "https://drive.google.com/drive/folders/1J2xs-VHe5py-G_XSv6BJdb-FwREDlGZg?usp=sharing")
    smarkup.add(tg, discord)
    bot.send_message(message.chat.id, "Вот мои проекты:", reply_markup=smarkup)
  if message.text == 'Отправить что-то автору':
     back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn_back = types.KeyboardButton("Отмена")
     back_markup.add(btn_back)
     send_message = bot.send_message(message.chat.id,"Следующее сообщение увидет автор. Также можно отправлять фото, документ и видео размером до 20 мегабайт.", reply_markup=back_markup)
     bot.register_next_step_handler(send_message, talk_with1)
  if message.text=='Книги по IT':
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
      svaz = types.KeyboardButton("Python")
      video = types.KeyboardButton("C++")
          #talk = types.KeyboardButton("C#")
      library = types.KeyboardButton("HTML и CSS")
      otm=types.KeyboardButton("Отмена")
      markup.add(svaz, video,library,otm)
      ms=bot.send_message(message.chat.id,f"Пожайлуста выберите язык",reply_markup=markup)
      bot.register_next_step_handler(ms, books)



def dowland_file_bot(message, c, img, send):
    file_photo = bot.get_file(c)

    filename, file_extension = os.path.splitext(file_photo.file_path)

    img = img
    chisl = 1

    b=img+str(chisl)+file_extension

    while os.path.exists(b)!=False:
        b = img+str(chisl)+file_extension
        chisl+=1

    save_photo = bot.download_file(file_photo.file_path)
    with open(b, 'wb') as new_file:
        new_file.write(save_photo)

    if message.chat.last_name == None:
        message.chat.last_name = "0"
    if message.chat.username == None:
        message.chat.username = "0"
    print(message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text,
          " !!! ", b, sep="", end=" /// ")
    with open('talk_with_autor.txt', 'a', encoding="utf-8") as f:
        s = ''.join((message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", "0",
                     " !!! ", b, " /// "))
        f.write(s)

    send_message = bot.send_message(message.chat.id,f"Автор увидит это {send}. Теперь отправьте ещё одно или напишите что-то!")
    bot.register_next_step_handler(send_message, talk_with1)
def talk_with1(message):
    try:
        if message.text == "Отмена":
            s(message)
        elif message.content_type == "photo":
            dowland_file_bot(message, message.photo[-1].file_id, "photo", "фото")
        elif message.content_type == "video":
            dowland_file_bot(message, message.video.file_id, "video", "видео")
        elif message.content_type == "text":
            talk_with2(message)
        elif message.content_type == "document":
            dowland_file_bot(message, message.document.file_id, "document", "файл")
        else:
            send_message = bot.send_message(message.chat.id, "Отправьте либо текст, либо фото, либо видео, либо документ!")
            bot.register_next_step_handler(send_message, talk_with1)
    except:
        print("ERROR1")
        with open("error.txt", "a", encoding="utf-8") as f:
            f.write("ERROR1\n")
        bot.send_message(message.chat.id, "ОШИБКА, ПОПРОБУЙТЕ ЗАНОВО!")

def reply_to_user(message):
    bot.send_message(message.chat.id, message.text)

def talk_with2(message):
    print(message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text, sep="")
    if message.chat.last_name == None:
        message.chat.last_name = "0"
    if message.chat.username == None:
        message.chat.username = "0"

    with open('talk_with_autor.txt', 'a', encoding="utf-8") as f:
        s = ''.join((message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text, "\n",))
        f.write(s)
    bot.send_message(message.chat.id, "Автор увидит это сообщение, но вы уже вышли из режима общения с автором")

def books(message):
    while message.text != 'Отмена':
        if message.text=="Отмена":
            s(message)
        elif message.text=='Python':
            smarkup = types.InlineKeyboardMarkup(row_width=1)
            first=types.InlineKeyboardButton('Основы Python.','https://t.me/c/1679219435/9')
            second=types.InlineKeyboardButton('Простой Python','https://t.me/c/1679219435/8')
            smarkup.add(first, second)
            bot.send_message(message.chat.id, "Вот учебники по Python:", reply_markup=smarkup)
            break
        elif message.text=='C++':
            mmarkup = types.InlineKeyboardMarkup(row_width=1)
            first=types.InlineKeyboardButton('Изучаем C++ через программирование игр','https://t.me/c/1679219435/7')
            second=types.InlineKeyboardButton(' C++20 STL Cookbook','https://t.me/c/1679219435/10')
            mmarkup.add(first, second)
            bot.send_message(message.chat.id, "Вот учебники по C++:", reply_markup=mmarkup)
            break
        elif message.text=="HTML и CSS":
            fmarkup = types.InlineKeyboardMarkup(row_width=1)
            first=types.InlineKeyboardButton('📔 Отзывчивый дизайн на HTML5 и CSS3 для любых устройств. 3-е изд.','https://t.me/c/1679219435/11')
            fmarkup.add(first)
            bot.send_message(message.chat.id, "Вот учебники по HTML и CSS:", reply_markup=fmarkup)
            break
    s(message)
def s(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
  svaz = types.KeyboardButton("Соцсети")
  video = types.KeyboardButton("Мои проекты")
  talk = types.KeyboardButton("Отправить что-то автору")
  library = types.KeyboardButton("Книги по IT")
  markup.add(svaz, video, talk, library)
  bot.send_message(message.chat.id,f"Нажми на одну из кнопок",reply_markup=markup)

#RUN
bot.polling(none_stop=True)
