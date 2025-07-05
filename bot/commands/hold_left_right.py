from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

async def hold_left_click (update: Update, context):
  if not update.message:
    return
  
  try:
    keyboard = [
      [
        InlineKeyboardButton('Enable hold left click', callback_data='hold_left_click'),
        InlineKeyboardButton('Close', callback_data='close_hold_left_click')
      ]
    ]
      
    await update.message.reply_html('<b>🔴 Hold left click disabled</b>', reply_markup=InlineKeyboardMarkup(keyboard))

  except Exception as e:
    print(f"Error in autoclick command: {e}")