import logging

class BotError(Exception):
    """Base class for bot-related errors"""
    pass

class InvalidUserError(BotError):
    """Raised when an invalid user tries to access the bot"""
    pass

class InvalidOperatorError(BotError):
    """Raised when an invalid operator tries to access the bot"""
    pass

class GLPIError(BotError):
    """Raised when there is an error interacting with the GLPI API"""
    pass

class TelegramError(BotError):
    """Raised when there is an error interacting with the Telegram Bot API"""
    pass

class ChatSessionError(BotError):
    """Raised when there is an error with a chat session"""
    pass

def handle_error(logger: logging.Logger, error: BotError):
    """Logs the error in a standardized way"""
    logger.error(f"Error: {error.__class__.__name__}, {str(error)}")