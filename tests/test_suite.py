import unittest

from test_base_record import TestRecordBase
from test_income_expense import TestIncomeExpense
from test_summary import TestSummary
from test_insights import TestInsights


def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(TestRecordBase))
    s.addTest(unittest.makeSuite(TestIncomeExpense))
    s.addTest(unittest.makeSuite(TestSummary))
    s.addTest(unittest.makeSuite(TestInsights))
    return s


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
