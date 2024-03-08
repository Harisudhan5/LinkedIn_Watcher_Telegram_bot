from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token : Final ="6585262021:AAES-Gcxj408-AlM5UGQqNb8d2yvDycjEEU"
Bot_Username : Final = "@Linked_watch_bot"

async def start_command(update : Update, context):
    await update.message.reply_text("Hello! Its me Harisudhan.S")
    
async def help_command(update : Update, context):
    await update.message.reply_text("Hello! Its me Harisudhan.S")
    
async def custom_command(update : Update, context):
    await update.message.reply_text("Custom answer for bot")

def handle_responses(text):
    if 'hello' in text:
        return "hey it's hello bro please continue"
    return 'i cant understand'

async def handle_message(update:Update,context):
    message_type = update.message.chat.type
    text = update.message.text
    print(f'user {update.message.chat.id} in {message_type} : {text}')
    if message_type == "group":
        if Bot_Username in text:
            new_text = text.replace(Bot_Username,' ').strip()
            response = handle_responses(new_text)
        else:
            return 
    else:
        response = handle_responses(text)
    print("Bot : ",response)
    await update.message.reply_text(response)

async def error(update:Update,context):
    print(f'update {update} caused error {context.error}')

if __name__ == '__main__':
    print("Starting Bot .........")
    app = Application.builder().token(Token).build()
    app.add_handler(CommandHandler("start",start_command))
    app.add_handler(CommandHandler("help",help_command))
    app.add_handler(CommandHandler("custom",custom_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    app.add_error_handler(error)
    
    print("Pooling ......")
    app.run_polling(poll_interval = 3)
