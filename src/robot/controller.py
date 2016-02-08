# Control module to manage other components like catching, analyse, action...

import sys
import os
sys.path.insert(0, '/Users/Zack/Code/BitBot/src')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")

from database.db_core.models import *
import time

while int(Parameter.objects.get(name="run").value) == 1:
    print("Running")
    time.sleep(1)