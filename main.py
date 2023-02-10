from telegram.ext import *
import secret
 
print("Server is running.... ")
 
def start_function(update, context):
    update.message.reply_text("Hello there! I'm AskPython Bot.")
 
def help_function(update, context):
    update.message.reply_text(
        """
    Available commands:
 
    /start : Starts up the bot
    /help : Help topics
    /about : About text
    /askpython : Go to AskPython Offical Website
    /custom : Other custom commands 
 
    """
    )
 
def about_function(update, context):
    update.message.reply_text("I am a bot and also a Python Genie.")
 
def ask_python_function(update, context):
    update.message.reply_text("AskPython Website: https://www.askpython.com/")
 
def custom_function(update, context):
    update.message.reply_text("Some other custom reply")
 
def message_handler_function(update, context):
    update.message.reply_text(f"Custom reply to message: '{update.message.text}'")
 
def error_handler_function(update, context):
    print(f"Update: {update} caused error: {context.error}")
 
# Connecting our app with the Telegram API Key and using the context
updater = Updater(secret.API_KEY, use_context=True)
my_dispatcher = updater.dispatcher
 
# Adding CommandHandler from telegram.ext to handle defined functions/commands
my_dispatcher.add_handler(CommandHandler("start", start_function))
my_dispatcher.add_handler(CommandHandler("help", help_function))
my_dispatcher.add_handler(CommandHandler("about", about_function))
my_dispatcher.add_handler(CommandHandler("askpython", ask_python_function))
my_dispatcher.add_handler(CommandHandler("custom", custom_function))
 
# Handing Incoming Messages
my_dispatcher.add_handler(MessageHandler(Filters.text, message_handler_function))
 
# Error Handling if any
my_dispatcher.add_error_handler(error_handler_function)
 
# Starting the bot using polling() function and check for messages every sec
updater.start_polling(1.0)
updater.idle()