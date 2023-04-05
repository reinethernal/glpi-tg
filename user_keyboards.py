from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """
    Returns a ReplyKeyboardMarkup containing the main menu options for the user.
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("🆕 Create new request"))
    keyboard.add(KeyboardButton("📝 My requests"))
    keyboard.add(KeyboardButton("💬 Live chat"))
    return keyboard

def get_categories_keyboard(categories: List[str]) -> ReplyKeyboardMarkup:
    """
    Returns a ReplyKeyboardMarkup containing the given categories as options for the user.
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories:
        keyboard.add(KeyboardButton(category))
    return keyboard

def get_cancel_keyboard() -> ReplyKeyboardMarkup:
    """
    Returns a ReplyKeyboardMarkup containing a cancel button for the user.
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("❌ Cancel"))
    return keyboard