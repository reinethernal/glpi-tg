import datetime
import pytz
import aiogram

# Helper function to format date and time
def format_datetime(dt: datetime.datetime) -> str:
    tz = pytz.timezone('UTC')
    local_dt = dt.astimezone(tz)
    return local_dt.strftime("%Y-%m-%d %H:%M:%S")

# Helper function to send notification to operators
async def send_notification(bot: aiogram.Bot, chat_id: int, message: str) -> None:
    try:
        await bot.send_message(chat_id, message)
    except aiogram.utils.exceptions.ChatNotFound:
        print(f"Failed to send notification: chat with id {chat_id} not found")
        
def setup_logger(name: str, log_file: str, level: int = logging.INFO):
    """Function to set up a logger with a specified name and log file"""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger