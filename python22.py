import logging
import json
from telegram.ext import *
from telegram import ReplyKeyboardMarkup
from telegram import InputFile
from telegram import *
from telegram import InputFile
import time


class Bot:
    def __init__(self):
        self.reply_keyboard = [['/gert', '/help'],
                               ['/button_1', '/button_2'],
                               ['/button_3', '/button_4']]
        self.markup = ReplyKeyboardMarkup(self.reply_keyboard, one_time_keyboard=False)
        self.n = 0
        self.logginn = logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
        self.tokenn = '6806407429:AAG3frXZuXwxL8TjG8KVdByYkG90CN2oVcI'
        self.logger = logging.getLogger(__name__)


    async def start(self, update, context, **kwargs):
        self.user = update.effective_user
        self.keyboard = [[InlineKeyboardButton("сайт",
                                               url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')],
                         [InlineKeyboardButton("сайт",
                                               url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')]]
        self.reply_markup = InlineKeyboardMarkup(self.keyboard)
        await update.message.reply_html(rf"Привет {self.user.mention_html()}! Я бот куратор", reply_markup=self.markup)
        time.sleep(2)
        await update.message.reply_text('Полезные материалы можно посмотреть тут', reply_markup=self.reply_markup)
        # bb = [[KeyboardButton('кноdfasdfпка', request_contact=None, request_location=None, **kwargs)]]
        # self.qq = ReplyKeyboardMarkup(bb)


    async def help(self, update, context):
        await update.message.reply_text("команда помощь")


    async def gert(self, update, context):
        if self.n >= 1:
            await update.message.reply_text(f"вы здесь отмечались {self.n}")
        else:
            self.n += 1
            await update.message.reply_text(f"вы здесь не отмечались")


    async def button_1(self, update, context):
        try:
            await update.message.reply_document('текстовый_документ.txt')
        except BaseException as a:
            print(a)


    async def button_2(self, update, context):
        n = context.args
        mn = " ".join(n)
        try:
            await update.message.reply_text(mn)
        except BaseException as q:
            await update.message.reply_text('''Вы не ввели сообщения.
Для ввода сообщения вам нужно написать команду и ввести ваше сообщение''')


    async def button_3(self, update, context):
        await update.message.reply_text('кнопка 3')


    async def button_4(self, update, context):
        await update.message.reply_text('кнопка 4')