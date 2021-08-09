pip install python-telegram-bot — upgrade

# Settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='1930200011:AAGT-HdoZSvvnFj6-1aq1gpiA4KoYQCfZ_4') # Telegram API Token
dispatcher = updater.dispatcher
# Command processing
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello, do you want to talk?')
def textMessage(bot, update):
    response = 'Got youre message: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

# Handlers
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Here we add the handlers to the dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Start search for updates
updater.start_polling(clean=True)
# Stop the bot, if Ctrl + C were pressed
updater.idle()

pip install apiai

# Settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater(token='1930200011:AAGT-HdoZSvvnFj6-1aq1gpiA4KoYQCfZ_4') # Telegram API Token
dispatcher = updater.dispatcher

def textMessage(bot, update):
    request = apiai.ApiAI('AIzaSyAvd_zOP_MIC7IqkdwPOVpXjCKlafmciwg').text_request() # Dialogflow API Token
    request.lang = 'en' 
    request.session_id = 'TheAmandabot' # ID dialog session (for bot training)
    request.query = update.message.text # Send request to AI with the user message
    
    

def textMessage(bot, update):
    request = apiai.ApiAI('AIzaSyAvd_zOP_MIC7IqkdwPOVpXjCKlafmciwg').text_request() # Dialogflow API Toke
    request.lang = 'en' 
    request.session_id = 'BatlabAIBot' # ID dialog session (for bot training)
    request.query = update.message.text # Send request to AI with the user message
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Take JSON answer
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='I dont understand!')
        

request.getresponse().read()

decode(‘utf-8’)

json.loads()

