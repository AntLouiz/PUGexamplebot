from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler,
    Filters
)

# criando uma instancia de Updater
updater = Updater(token="474302941:AAH-t-lDgmscYAME0-R3WEh9cOi2mcc1YVY")

# capturando a instancia do Dispatcher
dispatcher = updater.dispatcher

# criando os callbacks para os handlers
def start(bot, update):
    """
        Um callback que retorna uma mensagem
        para o inicio de uma conversa.
    """
    user_first_name = update.message.chat.first_name

    msg = "Hi {}".format(user_first_name)
    chat_id = update.message.chat_id

    bot.send_message(chat_id=chat_id, text=msg)


def bye(bot, update):

    user_first_name = update.message.chat.first_name
    msg = "Bye {}, thanks for message me.".format(user_first_name)
    chat_id = update.message.chat_id

    user_msg = update.message.text

    if user_msg.lower() == 'bye':
        bot.send_message(chat_id=chat_id, text=msg)


# criando um handler de comando e um de mensagem.
start_handler = CommandHandler('start', start)
bye_handler = MessageHandler(Filters.text, bye)

# registrando os handlers para o dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(bye_handler)

# rodando o updater para capturar todas as mensagens que serao enviadas para o bot.
updater.start_polling()
