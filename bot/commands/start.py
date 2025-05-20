from telegram import Update
from telegram.ext import ContextTypes
from bot import variables

async def start_command (update: Update, context: ContextTypes.DEFAULT_TYPE): 
  if not update.message:
    return
  content = [
    '<b>🤖 Available commands:</b>\n',
    *[f'\n<b>/{c.name}</b> - {c.description}' for c in variables.command_list],
  ]
  await update.message.reply_html(''.join(content), reply_to_message_id=update.message.id)