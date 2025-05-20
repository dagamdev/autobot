from telegram import Update, constants, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot import variables
import threading
import pyautogui
import time
from bot.lib import auto_farm

def autoclick_loop():
  while variables.autoclick_enabled:
    pyautogui.click()
    time.sleep(0.02)

async def update_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
  query = update.callback_query
  if not query:
    return
  
  if query.data == 'auto_click':
    try:
      variables.autoclick_enabled = not variables.autoclick_enabled
      if variables.autoclick_enabled:
        variables.autoclick_thread = threading.Thread(target=autoclick_loop, daemon=True)
        variables.autoclick_thread.start()
        
      await query.answer()
      keyboard = [
        [
          InlineKeyboardButton('Disable auto click' if variables.autoclick_enabled  else 'Enable auto click', callback_data='auto_click'),
          InlineKeyboardButton('Close', callback_data='close_auto_click'),
        ]
      ]

      # Edita el mensaje original con nuevo texto
      await query.edit_message_text('<b>🟢 Auto click enabled</b>' if variables.autoclick_enabled else'<b>🔴 Auto click disabled</b>',
        parse_mode=constants.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(keyboard)
      )

    except Exception as e:
      print(f"Error in handle callback auto_click command: {e}")

  if query.data in ['close_auto_click', 'close_chainers_farm']: 
    await query.answer()
    await query.edit_message_reply_markup()

  if query.data == 'chainers_farm':
    try:
      auto_farm.auto_chainersfarm = not auto_farm.auto_chainersfarm
      if auto_farm.auto_chainersfarm:
        auto_farm.auto_chainersfarm_thread = threading.Thread(target=auto_farm.auto_chainersfarm_loop, daemon=True)
        auto_farm.auto_chainersfarm_thread.start()
        
      await query.answer()
      keyboard = [
        [
          InlineKeyboardButton('Disable auto farm' if auto_farm.auto_chainersfarm  else 'Enable auto farm', callback_data='chainers_farm'),
          InlineKeyboardButton('Close', callback_data='close_chainers_farm'),
        ]
      ]

      # Edita el mensaje original con nuevo texto
      await query.edit_message_text('<b>🟢 Chainers farm automation enabled</b>' if auto_farm.auto_chainersfarm else'<b>🔴 Chainers farm automation disabled</b>',
        parse_mode=constants.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(keyboard)
      )

    except Exception as e:
      print(f"Error in handle callback chainers_farm command: {e}")
