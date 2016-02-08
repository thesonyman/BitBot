# Main bot module that starts all the processes

import time
import sys
import os
sys.path.insert(0, '/Users/Zack/Code/BitBot/src')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")

from database.db_core.models import *
from .controller import *

class Bitbot:
    
    def __init__(self):
        self.controller = Controller()

    def fire(self):
        while int(Parameter.objects.get(name="run").value) == 1:
            controller = Controller()
            time.sleep(60 / int(Parameter.objects.get(name="speed").value))