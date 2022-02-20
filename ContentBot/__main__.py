# Powered By TeamIndia 
# © @PiroXPower | @FriDayOp
import glob
from pathlib import Path
from ContentBot.utils import load_plugins
import logging
from . import bot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "ContentBot/Modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))


print("Your Bot Deployed Successfully!")
print("By Sammy • @IndianUpdatesOfficial")

if __name__ == "__main__":
    bot.run_until_disconnected()
