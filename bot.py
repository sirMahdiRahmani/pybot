import constans as k
import api as api

from telegram.ext import *
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext

from telegram import Update
from telegram import ReplyKeyboardMarkup



print("bot start...")




def start_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    print(chat_id)
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    update.message.reply_text("Hello {} {}.\nWelcome to SR WORLD CUP bot!!!\n if you need tap /help".format(first_name, last_name))
    main_menu_handler(update, context)


def sum_handler(update: Update, context: CallbackContext):
    numbers = context.args
    result = sum(int(i) for i in numbers)
    update.message.reply_text(result)



def main_menu_handler(update: Update, context: CallbackContext):
    buttons = [
        ["Group Stage", "Knock out Stage"],
        ["All Teams"]
    ]
    update.message.reply_text(
        text="choose option from menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )



def groups_menu(update: Update, context: CallbackContext):
    buttons = [
            ['Group A', 'Group B'],
            ['Group C', 'Group D'],
            ['Group E', 'Group F'],
            ['Group G', 'Group H'],
    ]
    update.message.reply_text(
        text="Choose Group for Stats:",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )



def message_handler(update: Update, context: CallbackContext):
    user_text = update.message.text
    count = 0 
    team = []
    if user_text in ('All Teams'):
        for i in api.teams:
            count = count + 1
            i = ("{}. {}".format(count, i))
            team.append(i)
        
        update.message.reply_text(text = "\n".join(team))
    
    if user_text in('Group Stage'):
        groups_menu(update, context)



def main():
    updater = Updater(k.API_KEY, use_context=True)
    dp = updater.dispatcher
    

    dp.add_handler(CommandHandler("sum", sum_handler))
    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    # dp.add_handler(MessageHandler(Filters.regex("Group Stage"), groups_menu))

    updater.start_polling()
    updater.idle()





main()