from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from default_messages import START_COMMAND_MESSAGE, HELP_COMMAND_MESSAGE, CUSTOM_COMMAND_MESSAGE, BOT_USERNAME, INFO_COMMAND_MESSAGE

TOKEN: Final = ""


# ------------------------------COMMANDS------------------------------#
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_COMMAND_MESSAGE)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_COMMAND_MESSAGE)

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(CUSTOM_COMMAND_MESSAGE)

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(INFO_COMMAND_MESSAGE)

# ------------------------------GAME COMMANDS--------------------------#
async def start_game_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('')

# ------------------------------RESPONSES------------------------------#
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return "Hi!"
    return "I don't understand"

# ------------------------------PRIV/GROUP------------------------------#
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    response: str = ''

    print(f'User ({update.message.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text: # When the bot is mentioned in the group
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
        else:
            return
    else: # Private chat
        response = handle_response(text)
    
    print('BOT: ', response)
    await update.message.reply_text(response)

# ------------------------------ERRORS------------------------------#
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('START...')

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('info', info_command))
    app.add_handler(CommandHandler('start', start_game_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('POLLING...')
    app.run_polling(poll_interval=3)
