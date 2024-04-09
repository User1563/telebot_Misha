import logging
from telegram.ext import *
from telegram import ReplyKeyboardMarkup


class Bot:
    def __init__(self):
        self.reply_keyboard = [['/gert', '/help'],
                               ['/button_1', '/button_2'],
                               ['/button_3', '/button_4']]
        self.markup = ReplyKeyboardMarkup(self.reply_keyboard, one_time_keyboard=False)
        self.n = 0
        self.logginn = logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
        self.tokenn = '7055353157:AAFJEZAiTJ6XaeiWcR_piFMipOCZ-WAIneo'
        self.logger = logging.getLogger(__name__)


    async def start(self, update, context):
        """Отправляет сообщение когда получена команда /start"""
        self.user = update.effective_user
        await update.message.reply_html(rf"Привет {self.user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!", reply_markup=self.markup)


    async def help_command(self, update, context):
        """Отправляет сообщение когда получена команда /help"""
        await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


    async def gert(self, update, context):
        if self.n >= 1:
            await update.message.reply_text(f"вы здесь отмечались {self.n}")
        else:
            self.n += 1
            await update.message.reply_text(f"вы здесь не отмечались {self.n}")


    async def button_1(self, update, context):
        await update.message.reply_text('кнопка 1')


    async def button_2(self, update, context):
        await update.message.reply_text('кнопка 2')


    async def button_3(self, update, context):
        await update.message.reply_text('кнопка 3')


    async def button_4(self, update, context):
        await update.message.reply_text('кнопка 4')


class Bot2(Bot):
    def main(self):
        b = Bot()
        application = Application.builder().token(self.tokenn).build()
        application.add_handler(CommandHandler("start", b.start))
        application.add_handler(CommandHandler("help", b.help_command))
        application.add_handler(CommandHandler("gert", b.gert))
        application.add_handler(CommandHandler("button_1", b.button_1))
        application.add_handler(CommandHandler("button_2", b.button_2))
        application.add_handler(CommandHandler("button_3", b.button_3))
        application.add_handler(CommandHandler("button_4", b.button_4))
        application.run_polling()


b = Bot2()
b.main()
