import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

load_dotenv()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("API_KEY")).build()

    application.add_handler(CommandHandler('start', start_command))

    application.run_polling()