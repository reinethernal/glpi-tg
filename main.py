import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TELEGRAM_API_TOKEN
from utils import setup_logger
from requests_from_telegram import on_start_command, on_new_request_command, on_view_requests_command, on_live_chat_command, on_user_message, on_callback_query
from glpi_operator_login import operator_login

# Set up logging
setup_logger()

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_API_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Initialize operator login
operator_login()

# Register handlers for commands, messages, and callbacks
dp.register_message_handler(on_start_command, commands=['start'])
dp.register_message_handler(on_new_request_command, commands=['new_request'])
dp.register_message_handler(on_view_requests_command, commands=['view_requests'])
dp.register_message_handler(on_live_chat_command, commands=['live_chat'])
dp.register_message_handler(on_user_message)
dp.register_callback_query_handler(on_callback_query)

# Start the event loop
async def main():
    logging.info("Starting bot...")
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())