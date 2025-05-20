from telegram import Update, constants
import psutil
from datetime import datetime, timedelta

async def battery_status (update: Update, context):
  if not update.message:
    return
  
  try:
    battery = psutil.sensors_battery()
    now_time = datetime.now()
    new_time = now_time
    times = []
    hours = battery.secsleft // 3600
    if hours > 0:
      times.append(f'{hours}h')

    minutes = (battery.secsleft % 3600) // 60
    if minutes > 0:
      times.append(f'{minutes}m')

    seconds = battery.secsleft % 60
    if seconds > 0:
      times.append(f'{seconds}s')


    if not battery.power_plugged:
      new_time = now_time + timedelta(seconds=battery.secsleft)
    
    await update.message.reply_text(f'Battery percent: <b>{battery.percent}%</b>\n{'🔌 Is charging' if battery.power_plugged else f'Is not charging\nEstimated battery drains in <b>{' '.join(times)}</b>, at <b>{new_time.strftime('%H:%M:%S')}</b>'}', parse_mode=constants.ParseMode.HTML)
  except Exception as e:
    print(f"Error in batteryStatus command: {e}")