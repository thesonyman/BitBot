# Module principal du bot, routing only

import controller
import time

class Bitbot():
    controller;
    speed = 60; # Amount of loop per minute
    running = False;
    
    def __init__(self):
        self.controller = Controller();
        self.run()
        
    def run(self):
        while True:
            self.controller.execute()
            time.sleep(60 / self.speed)