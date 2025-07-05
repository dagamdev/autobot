from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

async def hold_right_click (update: Update, context):
  if not update.message:
    return
  
  try:
    keyboard = [
      [
        InlineKeyboardButton('Enable hold right click', callback_data='hold_right_click'),
        InlineKeyboardButton('Close', callback_data='close_hold_right_click')
      ]
    ]
      
    await update.message.reply_html('<b>🔴 Hold right click disabled</b>', reply_markup=InlineKeyboardMarkup(keyboard))

  except Exception as e:
    print(f"Error in autoclick command: {e}")