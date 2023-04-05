import asyncio
from aiogram import types
from config import OPERATORS_CHAT_ID
from glpi_api_operator_request_actions import get_ticket, get_tickets_assigned_to_operator, assign_ticket_to_operator, update_ticket_status, create_ticket
from telegram_api import bot

async def operator_chat_handler():
    """
    Function for handling operator chats
    """
    while True:
        for ticket in await get_tickets_assigned_to_operator():
            if ticket['status'] == 'New':
                operator = await assign_ticket_to_operator(ticket)
                message = f'New chat from user {ticket["user_name"]}.'
                await bot.send_message(chat_id=OPERATORS_CHAT_ID, text=message)
                await bot.send_message(chat_id=operator['telegram_chat_id'], text='You have a new chat request!')
            elif ticket['status'] == 'Pending':
                operator = await get_ticket(ticket['id'])['operator']
                await bot.send_message(chat_id=operator['telegram_chat_id'], text=ticket['last_message'])
            elif ticket['status'] == 'Closed':
                continue
            else:
                message = f'Error: Unknown ticket status {ticket["status"]}.'
                await bot.send_message(chat_id=OPERATORS_CHAT_ID, text=message)
        await asyncio.sleep(10)

async def operator_message_handler(message: types.Message):
    """
    Function for handling operator side messages
    """
    ticket_id = message.reply_to_message.text.split(' ')[-1]
    ticket = await get_ticket(ticket_id)
    if not ticket:
        await bot.send_message(chat_id=message.chat.id, text='Invalid ticket ID.')
        return
    if ticket['status'] == 'Closed':
        await bot.send_message(chat_id=message.chat.id, text='This ticket is closed.')
        return
    await update_ticket_status(ticket_id, 'Pending')
    user = {'telegram_chat_id': ticket['user_telegram_chat_id'], 'name': ticket['user_name']}
    await bot.send_message(chat_id=user['telegram_chat_id'], text=message.text)
    await bot.send_message(chat_id=OPERATORS_CHAT_ID, text=f'Operator {message.from_user.full_name} replied to ticket {ticket_id}.')