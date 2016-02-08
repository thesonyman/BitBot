# Command line manager

import sys
import os
sys.path.insert(0, '/Users/Zack/Code/BitBot/src')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")

from database.db_core.models import *

def start():
    run = Parameter.objects.get(name="run")
    run.value = "1";
    run.save()
    from robot.bitbot import Bitbot
    bot = Bitbot()
    bot.fire()
    
def stop():
    run = Parameter.objects.get(name="run")
    run.value = "0";
    run.save()
    print("robot stopped")

if(sys.argv[1] == 'start'):
    start()
    
if(sys.argv[1] == 'stop'):
    stop()