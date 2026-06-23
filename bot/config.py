from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN") or ''
CHAT_ID = getenv("CHAT_ID")
CHAT_ID = int(CHAT_ID) if CHAT_ID else 0