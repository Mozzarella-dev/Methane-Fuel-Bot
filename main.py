from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='', use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

# TODO: usare database per utente
# TODO: comando /settings per modificare i valori come Km or Miles, EUR o USD
# TODO: comando /month per vedere la media di questo mese con grafico
# TODO: comando /week per vedere la media di questa settimana con grafico
# TODO: comando /year per vedere la media dell'ultimo anno con grafico
# TODO: comando /alltime per vedere tutto con grafico
# TODO: trovare modo di fare grafici
# TODO: comando /add per aggiungere km totali della macchina e costo pieno di metano
# TODO: /info comando per spiegare il funzionamento del bot
# TODO: /about me comando per il mio github