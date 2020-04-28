import unittest

from calender_available_slots import calc


class TestCalenderAvailability(unittest.TestCase):
    def test_calc(self):
        c1 = [[900, 1030], [1200, 1300], [1600, 1800]]
        c2 = [[1000, 1130], [1230, 1430], [1430, 1500], [1600, 1700]]
        t1 = [900, 2000]
        t2 = [1000, 1830]
        d = 30

        self.assertEqual(calc(c1, c2, t1, t2, d),
                         [[1130, 1200], [1500, 1600], [1800, 1830]])

    def test_c1_empty(self):
        c1 = []
        c2 = [[1000, 1130], [1230, 1430], [1430, 1500], [1600, 1700]]
        t1 = [900, 2000]
        t2 = [1000, 1830]
        d = 30

        self.assertEqual(calc(c1, c2, t1, t2, d),
                         [[1130, 1230], [1500, 1600], [1700, 1830]])

    def test_c2_empty(self):
        c1 = [[900, 1030], [1200, 1300], [1600, 1800]]
        c2 = []
        t1 = [900, 2000]
        t2 = [1000, 1830]
        d = 30

        self.assertEqual(calc(c1, c2, t1, t2, d),
                         [[1030, 1200], [1300, 1600], [1800, 1830]])


if __name__ == '__main__':
    unittest.main()
