# Tutorial from here
# http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html

import datetime
import unittest

# Here is our "unit"
class DatePattern:

    def __init__(self, year, month, day, weekday=0):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday

    def matches(self, date):
        return (self.yearMatches(date) and
                  self.monthMathces(date) and
                  self.dayMatches(date) and
                  self.weekdayMatches(date))

    def yearMatches(self, date):
        if not self.year: return True # If use wildcard = 0
        # Alternatively can write return not self.year
        return self.year == date.year

    def monthMathces(self, date):
        if not self.month: return True
        return self.month == date.month

    def dayMatches(self, date):
        if not self.day: return True
        return self.day == date.day

    def weekdayMatches(self, date):
        if not self.weekday: return True
        return self.weekday == date.weekday()

# Here is our test
class FooTests(unittest.TestCase):

    def testMatches(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 28)
        self.failUnless(p.matches(d))

    def testMatchesFalse(self):
        p = DatePattern(2005, 4, 9)
        d = datetime.date(2005, 4, 10)
        self.failIf(p.matches(d))

    def testMatchesYearAsWildCard(self):
        p = DatePattern(0, 4, 10)
        d = datetime.date(2005, 4, 10)
        self.failUnless(p.matches(d))

    def testMatchesYearAndMonthAsWildCards(self):
        p = DatePattern(0, 0, 10)
        d = datetime.date(2005, 4, 10)
        self.failUnless(p.matches(d))

    def testMatchesWeekday(self):
        p = DatePattern(0, 0, 0, 2) # 2 is Wednesday
        d = datetime.date(2004, 9, 29)
        self.failUnless(p.matches(d))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
