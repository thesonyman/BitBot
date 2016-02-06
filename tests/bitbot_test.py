# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import os


class  Bitbot_TestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = Bitbot_()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_bitbot_(self):
        test_loader = unittest.defaultTestLoader
        test_runner = unittest.TextTestRunner()
        test_suite  = test_loader.discover(os.getcwd())
        test_runner.run(test_suite)


