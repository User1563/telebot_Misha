from telegram.ext import *
from python22 import *
from python22 import tokenn, CONST, FILE, MN



def main() -> None:
    application = Application.builder().token(tokenn).build()
    # application.add_handler(CommandHandler("start", bb.start))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("gert", gert))
    application.add_handler(CommandHandler("file", file_text))
    application.add_handler(CommandHandler("useful_materials", button_3))
    application.add_handler(CommandHandler("audio", button_4))
    # application.add_handler(CommandHandler("button_4", button_4))
    application.add_handler(CommandHandler('keyboard', start))
    application.add_handler(CommandHandler('photo', photo))
    conv_handler_4 = ConversationHandler(
        entry_points=[CommandHandler("fio", command_text)],
        states={
            MN: [MessageHandler(filters.TEXT, text_file)]
        },
        fallbacks=[CommandHandler("text", text_file)],
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("function", function)],
        states={
            CONST: [MessageHandler(filters.TEXT, work_start)],
        },
        fallbacks=[CommandHandler("work_start", work_start)],
    )

    conv_handler_5 = ConversationHandler(
        entry_points=[CommandHandler("fio", command_text)],
        states={
            MN: [MessageHandler(filters.TEXT, text_file)]
        },
        fallbacks=[CommandHandler("text", text_file)],
    )

    conv_handler_6 = ConversationHandler(
        entry_points=[CommandHandler("write", write)],
        states={
            W: [MessageHandler(filters.TEXT, work_write)],
        },
        fallbacks=[CommandHandler("work_write", work_write)],
    )

    conv_handler_7 = ConversationHandler(
        entry_points=[CommandHandler("start_otz", otzivi)],
        states={
            O: [MessageHandler(filters.TEXT, otzivi1)]
        },
        fallbacks=[CommandHandler("otz", otzivi)],
    )
    application.add_handler(conv_handler_5)
    application.add_handler(conv_handler)
    application.add_handler(conv_handler_6)
    application.add_handler(conv_handler_4)
    application.add_handler(conv_handler_7)


    # application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()

