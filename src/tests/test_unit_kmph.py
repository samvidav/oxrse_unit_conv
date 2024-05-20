import unittest
from oxrse_unit_conv.units import mps, kmph


class TestKilometerPerHour(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(kmph.si_unit.matches(mps))

    def test_basic_conversion(self):
        self.assertEqual(kmph.to_si(36), 10)
        self.assertEqual(kmph.to_unit(10, kmph), 10)


if __name__ == '__main__':
    unittest.main()
