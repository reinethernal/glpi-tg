import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TELEGRAM_API_TOKEN

# Initialize the bot and dispatcher
bot = Bot(token=TELEGRAM_API_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def send_message(chat_id: int, text: str, reply_markup=None):
    """
    Send a message to a user or group chat.
    """
    try:
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)
    except Exception as e:
        logging.error(f"Failed to send message to chat {chat_id}: {e}")

async def answer_callback_query(callback_query_id: str, text: str = None):
    """
    Answer a callback query from a button press.
    """
    try:
        await bot.answer_callback_query(callback_query_id=callback_query_id, text=text)
    except Exception as e:
        logging.error(f"Failed to answer callback query {callback_query_id}: {e}")