from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

async def auto_click (update: Update, context):
  if not update.message:
    return
  
  try:
    keyboard = [
      [
        InlineKeyboardButton('Enable auto click', callback_data='auto_click'),
        InlineKeyboardButton('Close', callback_data='close_auto_click')
      ]
    ]
      
    await update.message.reply_html('<b>🔴 Auto click disabled</b>', reply_markup=InlineKeyboardMarkup(keyboard))

  except Exception as e:
    print(f"Error in autoclick command: {e}")