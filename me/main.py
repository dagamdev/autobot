from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji
import re
import webbrowser
import threading
from me import config, variables, lib, obs

meet_pattern = re.compile(r'https://meet\.google\.com/[a-z\-]+', re.IGNORECASE)
client: TelegramClient = TelegramClient('mi_sesion', config.api_id, config.api_hash)

@client.on(events.NewMessage())
async def messageHandler(event: events.NewMessage.Event):
  sender = await event.get_sender()
  text = event.raw_text

  if sender.username == variables.target_username and not variables.open_meet:
    match = meet_pattern.search(text)
    if match:
      print("¡Enlace de Meet detectado!", match[0])
      webbrowser.open(match[0])
      variables.open_meet = True
      await client(SendReactionRequest(
        peer=event.chat_id, # type: ignore
        msg_id=event.id,
        reaction=[ReactionEmoji(emoticon='🔥')]
      ))

  # Bot id
  if event.chat_id == 8169322411:
    if text == 'Te has unido al Meet':
      variables.recording = True
      try:
        variables.click_meet_thread = threading.Thread(target=lib.click_in_meet, daemon=True)
        variables.click_meet_thread.start()
        response = obs.start_recording()
        print(response)
        await client(SendReactionRequest(
          peer=event.chat_id, # type: ignore
          msg_id=event.id,
          reaction=[ReactionEmoji(emoticon='👍')]
        ))
      except Exception as e:
        variables.recording = False
        print(f"❌ Error al iniciar grabación: {e}")

    if text == 'El Meet ha terminado':
      try:
        response = obs.stop_recording()
        print(response)
        variables.open_meet = False
        variables.recording = False
        await client(SendReactionRequest(
          peer=event.chat_id, # type: ignore
          msg_id=event.id,
          reaction=[ReactionEmoji(emoticon='👍')]
        ))
      except Exception as e:
        print(f"❌ Error al detener grabación: {e}")

async def start_me ():
  await client.start() # type: ignore
  print('✅ Sesion iniciada')
  obs.connect()
  
  try:
    await client.run_until_disconnected()  # type: ignore
  except KeyboardInterrupt:
    print('⚠️ Bot detenido por usuario (Ctrl+C)')
  finally:
    await client.disconnect() # type: ignore
    print('✅ Bot desconectado')

