import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode, ChatActions
from aiogram.dispatcher import filters
from config import TELEGRAM_API_TOKEN

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

# States
class LiveChatUserStates:
    CHAT = "chat"

# Conversation starters
async def start_chatting(chat_id: int, state: FSMContext):
    await bot.send_message(chat_id, "Hello, how can I assist you today? Type /cancel to end the chat.")
    await state.set_state(LiveChatUserStates.CHAT)

# Handle messages
@dp.message_handler(state=LiveChatUserStates.CHAT)
async def handle_chat_message(message: types.Message, state: FSMContext):
    # Forward message to operator's chat ID
    operator_chat_id = get_operator_chat_id()
    if operator_chat_id:
        await bot.forward_message(operator_chat_id, message.chat.id, message.message_id)
    else:
        await bot.send_message(message.chat.id, "Sorry, there are no operators available at the moment.")
    # Set typing action
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)

# Handle /cancel command
@dp.message_handler(commands=["cancel"], state="*")
async def cancel_chat(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.chat.id, "Chat ended.")

# Start the bot
if __name__ == '__main__':
    asyncio.run(start_polling(dp))