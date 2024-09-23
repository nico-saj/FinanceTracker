import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import *

load_dotenv()

from database import get_db_session
from models.index import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with get_db_session() as session:
        # Extract user info from Telegram
        user_id = update.message.from_user.id
        username = update.message.from_user.username

        # Check if the user is already in the database
        user = session.query(User).filter_by(user_telegram_id=user_id).first()

        if user:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome back, {username}!")
        else:
            # Add the user to the database
            new_user = User(user_telegram_id=user_id, username=username)
            session.add(new_user)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello, {username}! You've been added to the database.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('API_KEY')).build()

    application.add_handler(CommandHandler('start', start_command))

    application.run_polling()