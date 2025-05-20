import psutil
from telegram import constants
from telegram.ext import Application
from bot import variables
import asyncio

async def check_battery(app: Application):
  while True:
    battery = psutil.sensors_battery()

    if battery.percent == 100 and battery.power_plugged and battery.percent != variables.battery_percent:
      await app.bot.send_message(variables.CHAT_ID, f'🔋 Charged battery <i>({battery.percent}%)</i>', parse_mode=constants.ParseMode.HTML)
      variables.battery_percent = battery.percent
    elif battery.percent <= 20 and not battery.power_plugged and abs(battery.percent - variables.battery_percent) > 2:
      await app.bot.send_message(variables.CHAT_ID, f'🪫 Low battery <i>({battery.percent}%)</i>', parse_mode=constants.ParseMode.HTML)
      variables.battery_percent = battery.percent

    await asyncio.sleep(60)