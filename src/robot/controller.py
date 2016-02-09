# Control module to manage other components like catching, analyse, action...

import sys
sys.path.insert(0, '/Users/Zack/Code/BitBot/src')

from . import analyse
from . import decision
from . import action
from . import strategy


class Controller:
    
    def __init__(self):
        self.strategy = strategy.Strategy()
        
    def run(self):
        analyse.analyse()
        decision.take_decision(self.strategy)
        action.execute()

