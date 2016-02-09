# Fake wallet module to simulate

import sys
import os
sys.path.insert(0, '/Users/Zack/Code/BitBot/src')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")

def increase(amount):
    parameter = Parameter.objects.get(name="wallet")
    int_val = int(parameter.value)
    int_val += amount
    parameter.value = str(str(int_val))
    parameter.save()
    
def decrease(amount):
    parameter = Parameter.objects.get(name="wallet")
    int_val = int(parameter.value)
    int_val -= amount
    parameter.value = str(str(int_val))
    parameter.save()
    
def get_money():
    return int(Parameter.objects.get(name="wallet").value)