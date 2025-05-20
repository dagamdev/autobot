from telegram import Update, constants, InlineKeyboardButton, InlineKeyboardMarkup

async def chainers_farm (update: Update, context):
  if not update.message:
    return
  
  try:
    keyboard = [
      [
        InlineKeyboardButton('Enable auto farm', callback_data='chainers_farm'),
        InlineKeyboardButton('Close', callback_data='close_chainers_farm')
      ]
    ]

    await update.message.reply_text('<b>🔴 Chainers farm automation disabled</b>',
      parse_mode=constants.ParseMode.HTML,
      reply_markup=InlineKeyboardMarkup(keyboard)
    )

  except Exception as e:
    print(f"Error in autoclick command: {e}")