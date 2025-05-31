from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

async def hold_click (update: Update, context):
  if not update.message:
    return
  
  try:
    keyboard = [
      [
        InlineKeyboardButton('Enable hold click', callback_data='hold_click'),
        InlineKeyboardButton('Close', callback_data='close_hold_click')
      ]
    ]
      
    await update.message.reply_html('<b>🔴 Hold click disabled</b>', reply_markup=InlineKeyboardMarkup(keyboard))

  except Exception as e:
    print(f"Error in autoclick command: {e}")