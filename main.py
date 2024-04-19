from telegram.ext import *
from python22 import Bott


class Bot2(Bott):
    def main(self) -> None:
        bb = Bott()
        application = Application.builder().token(self.tokenn).build()
        # application.add_handler(CommandHandler("start", bb.start))
        application.add_handler(CommandHandler("help", bb.help))
        application.add_handler(CommandHandler("gert", bb.gert))
        application.add_handler(CommandHandler("file", bb.file_text))
        application.add_handler(CommandHandler("button_2", bb.button_2))
        application.add_handler(CommandHandler("useful_materials", bb.button_3))
        application.add_handler(CommandHandler("button_4", bb.button_4))
        # application.add_handler(CommandHandler("button_4", bb.button_4))
        # application.add_handler(CommandHandler('keyboard', b.start))
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", Bott().start)],
            states={
                bb.CONST: [MessageHandler(filters.TEXT, Bott().work_start)]
            },
            fallbacks=[CommandHandler("work_start", Bott().work_start)],
        )

        application.add_handler(conv_handler)
        application.run_polling()


b = Bot2()
b.main()




