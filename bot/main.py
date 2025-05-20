from os import getenv
from dotenv import load_dotenv
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, Application, CallbackQueryHandler, ExtBot, JobQueue, ContextTypes
from typing import Any, Dict
import asyncio
import threading
from .commands import start_command, open_page, battery_status, auto_click, cursor_position, chainers_farm
from .handlers import update_callback
from bot import utils, variables
from me.main import start_me

AppType = Application[ExtBot[None], ContextTypes.DEFAULT_TYPE, Dict[Any, Any], Dict[Any, Any], Dict[Any, Any], JobQueue[ContextTypes.DEFAULT_TYPE]]


# Bot token can be obtained via https://t.me/BotFather
load_dotenv()
TOKEN = getenv("BOT_TOKEN") or ''


def start_bot():
  # asyncio.set_event_loop(asyncio.new_event_loop())
  app = ApplicationBuilder().token(TOKEN).build()

  app.add_handler(CommandHandler('start', start_command))
  app.add_handler(CommandHandler('openpage', open_page))
  app.add_handler(CommandHandler('batterystatus', battery_status))
  app.add_handler(CommandHandler('autoclick', auto_click))
  app.add_handler(CommandHandler('cursorposition', cursor_position))
  app.add_handler(CommandHandler('chainersfarm', chainers_farm))
  app.add_handler(CallbackQueryHandler(update_callback))
  
  async def on_startup(aplication: AppType): 
    asyncio.create_task(utils.check_battery(aplication))
    
    await aplication.bot.set_my_commands([BotCommand(c.name, c.description) for c in variables.command_list])
    print(f'🤖 The {aplication.bot.first_name} bot is ready')
    def go_me ():
      asyncio.run(start_me()) # type: ignore
    threading.Thread(target=go_me, daemon=True).start()
    
  app.post_init = on_startup # type: ignore

  try:
    app.run_polling(allowed_updates=Update.ALL_TYPES)
  except KeyboardInterrupt:
    print('⚠️ Bot detenido por usuario (Ctrl+C)')

if __name__ == '__main__':
  start_bot()