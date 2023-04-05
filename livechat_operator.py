import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

from config import TELEGRAM_API_TOKEN

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create bot and dispatcher instances
bot = Bot(token=TELEGRAM_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Define States
class LiveChatOperator(StatesGroup):
    waiting_for_user = State()
    waiting_for_operator_response = State()

# Handle "/start" command
@dp.message_handler(commands=["start"], state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    # Clear state
    await state.finish()

    # Send welcome message and start chat
    await message.answer("Welcome to the live chat operator! Please wait for a user to connect.")
    await LiveChatOperator.waiting_for_user.set()

# Handle message from user
@dp.message_handler(state=LiveChatOperator.waiting_for_user)
async def user_message_received(message: types.Message, state: FSMContext):
    # Save user chat ID
    await state.update_data(user_chat_id=message.chat.id)

    # Notify operator
    await bot.send_message(chat_id=OPERATORS_CHAT_ID, text=f"User {message.chat.username} has connected.")

    # Wait for operator response
    await message.answer("You are now connected to an operator. Please wait for a response.")
    await LiveChatOperator.waiting_for_operator_response.set()

# Handle message from operator
@dp.message_handler(chat_id=OPERATORS_CHAT_ID, state=LiveChatOperator.waiting_for_operator_response)
async def operator_message_received(message: types.Message, state: FSMContext):
    # Get user chat ID
    data = await state.get_data()
    user_chat_id = data.get("user_chat_id")

    # Forward message to user
    await bot.send_message(chat_id=user_chat_id, text=message.text)

    # Wait for user response
    await LiveChatOperator.waiting_for_user.set()

# Handle "/cancel" command
@dp.message_handler(commands=["cancel"], state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    # Clear state
    await state.finish()

    # Send cancel message and end chat
    await message.answer("Chat cancelled.")