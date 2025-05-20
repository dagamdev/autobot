autoclick_enabled = False
autoclick_thread = None
battery_percent = 0
CHAT_ID = 7843992668

class CommandData:
  def __init__(self, name: str, description: str): 
    self.name = name
    self.description = description

command_list = (
  CommandData('start', 'Start my PC bot'),
  CommandData('openpage', "📄 Open the provided page in my PC's browser"),
  CommandData('batterystatus', '🔋 Shows the battery status of my PC'),
  CommandData('cursorposition', '📌 Gets the position of the cursor on the screen'),
  CommandData('autoclick', '👆 Enables or disables cursor auto-click'),
  CommandData('chainersfarm', '🧑‍🌾 Manages Chainers farm automation')
)