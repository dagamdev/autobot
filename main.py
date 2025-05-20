import bot.main as Bot
import logging

logging.basicConfig(format='[%(levelname) %(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

if __name__ == '__main__':
  Bot.start_bot()