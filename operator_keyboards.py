from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def generate_operator_keyboard():
    """Generate a custom keyboard for operators."""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton('📩 Open Requests'))
    keyboard.row(KeyboardButton('👥 Assigned Requests'), KeyboardButton('🔍 Search Requests'))
    keyboard.row(KeyboardButton('📝 Create Ticket'))
    return keyboard

def generate_request_keyboard(requests):
    """Generate a custom keyboard for selecting a request."""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for request in requests:
        keyboard.row(KeyboardButton(f'{request["id"]}: {request["title"]}'))
    return keyboard