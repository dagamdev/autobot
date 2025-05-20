from dotenv import load_dotenv
from os import getenv

load_dotenv()

api_id = getenv('API_ID')
api_id = int(api_id) if api_id else 0
api_hash = getenv('API_HASH') or ''
dev_mode = False

obs_host = getenv('OBS_HOST') or 'localhost'
obs_port = getenv('OBS_PORT') or '4444'
obs_password = getenv('OBS_PASSWORD') or ''