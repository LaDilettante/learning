import unittest
import datetime

class YearPattern:
    def __init__(self, year):
        self.year = year

    def matches(self, date):
        return self.year == date.year

class MonthPattern:
    def __init__(self, month):
        self.month = month

    def matches(self, date):
        return self.month == date.month

class DayPattern:
    def __init__(self, day):
        self.day = day

    def matches(self, date):
        return self.day == date.day

class WeekdayPattern:
    def __init__(self, weekday):
        self.weekday = weekday

    def matches(self, date):
        return self.weekday == date.weekday()

class CompositePattern:

    def __init__(self):
        self.patterns = []

    def add(self, pattern):
        self.patterns.append(pattern)

    def matches(self, date):
        for pattern in self.patterns:
            if not pattern.matches(date):
                return False
        return True

# Here's the test
class NewTests(unittest.TestCase):

    def testYearMatches(self):
        yp = YearPattern(2004)
        d = datetime.date(2004, 9, 29)
        self.failUnless(yp.matches(d))

    def testYearDoesNotMatch(self):
        yp = YearPattern(2004)
        d = datetime.date(2005, 9, 29)
        self.failIf(yp.matches(d))

    def testMonthMatches(self):
        mp = MonthPattern(9)
        d = datetime.date(2004, 9, 29)
        self.failUnless(mp.matches(d))

    def testMonthDoesNotMatch(self):
        mp = MonthPattern(8)
        d = datetime.date(2004, 9, 29)
        self.failIf(mp.matches(d))

    def testDayMatches(self):
        dp = DayPattern(29)
        d = datetime.date(2004, 9, 29)
        self.failUnless(dp.matches(d))

    def testDayDoesNotMatch(self):
        dp = DayPattern(28)
        d = datetime.date(2004, 9, 29)
        self.failIf(dp.matches(d))

    def testWeekdayMatches(self):
        wp = WeekdayPattern(2) # Wednesday
        d = datetime.date(2004, 9, 29)
        self.failUnless(wp.matches(d))

    def testWeekdayDoesNotMatch(self):
        wp = WeekdayPattern(1) # Tuesday
        d = datetime.date(2004, 9, 29)
        self.failIf(wp.matches(d))

    def testCompositeMatches(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(29))
        d = datetime.date(2004, 9, 29)
        self.failUnless(cp.matches(d))

    def testCompositeDoesNotMatch(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(28))
        d = datetime.date(2004, 9, 29)
        self.failIf(cp.matches(d))

    def testCompositeWithoutYearMatches(self):
        cp = CompositePattern()
        cp.add(MonthPattern(4))
        cp.add(DayPattern(10))
        d = datetime.date(2005, 4, 10)
        self.failUnless(cp.matches(d))

# Refactoring
# Set up a datetime object in the beginning instead of
# repeating every time
class PatternTests(unittest.TestCase):
    def setUp(self):
        self.d = datetime.date(2004, 9, 29)

    def testYearMatches(self):
        yp = YearPattern(2004)
        self.failUnless(yp.matches(self.d))

    def testLastThursdayMatches(self):
        cif __name__ == "__main__":
    unittest.main()p = CompositePattern()
        cp.add(LastWeekdayPattern(THURSDAY))
        self.failUnless(cp.matches(self.d))

    def testYearDoesNotMatch(self):
        yp = YearPattern(2003)
        self.failIf(yp.matches(self.d))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
