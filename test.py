# import sys

# sys.path.append('C:/Users/STANLEY NUMONDE/Downloads/data/')

from My_module import MyOperandFinder

import unittest

class TestOperandFinder(unittest.TestCase):
    def test_operand(self):
        operand = MyOperandFinder.findOperand(89)
        calc_sum = 89 - operand
        self.assertTrue(calc_sum < operand)
        

