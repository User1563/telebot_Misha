from telegram.ext import *
from python22 import Bot


class Bot2(Bot):
    def main(self):
        b = Bot()
        application = Application.builder().token(self.tokenn).build()
        application.add_handler(CommandHandler("start", b.start))
        application.add_handler(CommandHandler("help", b.help))
        application.add_handler(CommandHandler("gert", b.gert))
        application.add_handler(CommandHandler("button_1", b.button_1))
        application.add_handler(CommandHandler("button_2", b.button_2))
        application.add_handler(CommandHandler("button_3", b.button_3))
        application.add_handler(CommandHandler("button_4", b.button_4))
        application.add_handler(CommandHandler("button_4", b.button_4))
        # application.add_handler(CommandHandler('keyboard', b.start))
        application.run_polling()


b = Bot2()
b.main()
