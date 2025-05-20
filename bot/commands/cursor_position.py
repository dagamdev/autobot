from telegram import Update, constants
import asyncio
import pyautogui

async def cursor_position (update: Update, context):
  if not update.message:
    return
  
  try:
    message = await update.message.reply_text('You have 5s to position the cursor at the point you want')
    await asyncio.sleep(5)
    position = pyautogui.position()
    await message.edit_text(f'<b>Cursor position:</b>\n\nx: <code>{position.x}</code>\ny: <code>{position.y}</code>', parse_mode=constants.ParseMode.HTML)

  except Exception as e:
    print(f"Error in autoclick command: {e}")