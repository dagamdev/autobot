from obswebsocket import obsws, requests
from me import config

client = obsws(config.obs_host, int(config.obs_port), config.obs_password)

def connect ():
  try:
    client.connect()
    print("✅ Conectado a OBS")
  except Exception as e:
    print(f"❌ Error al conectar con OBS: {e}")

def start_recording ():
  return client.call(requests.StartRecording())

def stop_recording ():
  return client.call(requests.StopRecording())