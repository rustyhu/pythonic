"This should be a very good unittest example"

import unittest
from .calc_interpreter import *


class calcTest(unittest.TestCase):
    def testStage1(self):
        "Stage1: The execution of evaluation"
        self.assertEquals(Exp('+', ))

    def testStage2(self):
        self.assertEqual(calc_eval(calc_parse("+(3, 6)")), 9)

    # def testStage3(self):
    #     pass

# if __name__ == "__main__":
    # unittest.main()
