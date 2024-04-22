import logging
from telegram.ext import *
from telegram import ReplyKeyboardMarkup
from telegram import InputFile
from telegram import *
import json
from telegram import InputFile
import time


reply_keyboard = [['/fio', '/audio'],
                  ['/file', '/useful_materials'],
                  ['/write', '/start_otz'],
                  ['/photo', '/start']]
reply_keyboard_2 = [['/function']]
CONST = 1
FILE = 2
PHOTO = 11
MN = 10
M = 12
W = 5
O = 8
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
nm = 0
markup_2 = ReplyKeyboardMarkup(reply_keyboard_2, one_time_keyboard=False)
logginn = logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
tokenn = '6806407429:AAG3frXZuXwxL8TjG8KVdByYkG90CN2oVcI'
logger = logging.getLogger(__name__)


async def start(update, context):
    await update.message.reply_text('Выберите функцию', reply_markup=markup_2)


async def function(update, context):
    await update.message.reply_text('Нажмите еще раз, чтобы потвердить что вы не робот')
    return CONST


class Name:
    def __init__(self, name, surname, text):
        self.name = name
        self.surname = surname
        self.text = text

    def jsonfile(self):
        with open('file.json', 'r', encoding='utf-8') as files:
            v = json.load(files)
            v[self.name + ' ' + self.surname] = self.text
        with open('fille.txt', 'a+') as filebase:
            filebase.write(str(self.text + ' '))
        with open('file.json', 'w', encoding='utf-8') as files_1:
            json.dump(v, files_1, indent=4)

    def json_n_file(self):
        with open('file.json', 'r', encoding='utf-8') as files:
            v = json.load(files)
            n = v[self.name + ' ' + self.surname]
            v[self.name + ' ' + self.surname] = []
            v[self.name + ' ' + self.surname].append(n)
            v[self.name + ' ' + self.surname].append(self.text)
            with open('file.json', 'w', encoding='utf-8') as file_:
                json.dump(v, file_, indent=4)

async def write(update, context):
    await update.message.reply_text('Напишите сначала Фамилия имя а затем что вы знаете о питоне')
    return W


async def otzivi(update, context):
    await update.message.reply_text('Напишите сначала фамилия имя и потом отзыв о работе бота')
    return O


async def otzivi1(update, context):
    try:
        s = str(update.message.text).split()
        s1 = s[0]
        s2 = s[1]
        s3 = s[2]
        a = Name(s1, s2, s3)
        a.json_n_file()
    except BaseException as nn:
        await update.message.reply_text('Напишите сначала имя фамилия черз пробел а затем текст')
    return ConversationHandler.END


async def work_write(update, context):
    try:
        string = str(update.message.text).split()
        m1 = string[0]
        m2 = string[1]
        m3 = string[2]
        n = Name(m1, m2, m3)
        n.jsonfile()
        await update.message.reply_text('Данные сохранены')
    except IndexError as error:
        await update.message.reply_text('некоректные данные')
    return ConversationHandler.END


async def work_start(update, context):
    user = update.effective_user
    await update.message.reply_html(rf"Привет {user.mention_html()}! Я бот куратор", reply_markup=markup)
    time.sleep(0.5)
    await update.message.reply_text('Нажмите на кнопку, чтобы обновить бота нажмите "/start"')
    return ConversationHandler.END


async def help(update, context):
    await update.message.reply_text("команда помощь")


async def file_text(update, context):
    try:
        await update.message.reply_document('В_ТЕКСТОВОМ_ДОКУМЕНТЕ.docx')
    except BaseException as m:
        print(m)


async def button_3(update, context):
    keyboard = [[InlineKeyboardButton("сайт",
                                      url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')],
                         [InlineKeyboardButton("сайт",
                                               url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')]]
    repply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Полезные материалы можно посмотреть тут", reply_markup=repply_markup)


async def command_text(update, context):  # старт анализа (Криптовалюта)
    await update.message.reply_text('Напишите Ваше фамилию имя отчество')
    return MN


async def text_file(update, context):
    a = str(update.message.text).split()
    with open('file.txt', 'a+', encoding='utf-8') as d:
        d.write(a[0])
    return ConversationHandler.END


async def button_4(update, context):
    file_audio = 'sample-15s.mp3'
    await update.message.reply_text('аудио')
    await update.message.reply_audio(audio=file_audio)


async def photo(update, context):
    await update.message.reply_photo('фото.jpg')
