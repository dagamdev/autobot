from telegram import Update
from telegram.ext import ContextTypes
import webbrowser
from urllib.parse import urlparse

async def open_page (update: Update, context: ContextTypes.DEFAULT_TYPE):
  if not update.message:
    return

  if not context.args:
    await update.message.reply_text('Proporciona el enlace a abrir', reply_to_message_id=update.message.id)
    return
  url = context.args[0]
  try:
    result = urlparse(url)
    if not all([result.scheme, result.netloc]):
      await update.message.reply_text('El argumento no es una url valida', reply_to_message_id=update.message.id)
    
    webbrowser.open(url)
    await update.message.reply_text('La url se ha habierto en el navegador', reply_to_message_id=update.message.id)
  except ValueError:
    return False