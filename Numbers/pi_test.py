import unittest
import pi
from decimal import Decimal


class TestPi(unittest.TestCase):
    def test_pi_with_valid_input(self):
        with self.assertRaises(SystemExit) as se:
            pi.main(lambda: '12', lambda: 'q')
        self.assertEqual(se.exception.code, 0)
        self.assertEqual(pi.pi(2), Decimal('3.14'))

    def test_pi_nan_input(self):
        with self.assertRaises(SystemExit) as se:
            pi.main(lambda: 'foo', lambda: 'q')
        self.assertEqual(se.exception.code, 0)
        self.assertIn('Please try again', pi.pi('foo'))

    def test_pi_input_too_large(self):
        with self.assertRaises(SystemExit) as se:
            pi.main(lambda: '50', lambda: 'q')
        self.assertEqual(se.exception.code, 0)
        self.assertIn('Please try again', pi.pi(50))

    def test_pi_input_negative(self):
        with self.assertRaises(SystemExit) as se:
            pi.main(lambda: '-2', lambda: 'q')
        self.assertIn('Please try again', pi.pi(-2))
        self.assertEqual(se.exception.code, 0)

    def test_pi_with_no_input(self):
        with self.assertRaises(SystemExit) as se:
            pi.main(lambda: '', lambda: 'q')
        self.assertEqual(se.exception.code, 0)

    def test_pi_with_q_first(self):
        with self.assertRaises(SystemExit) as se:
            pi.main(lambda: 'q', lambda: 'q')
        self.assertEqual(se.exception.code, 0)


if __name__ == '__main__':
    unittest.main(buffer=True)
