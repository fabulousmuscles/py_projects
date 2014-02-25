import unittest
import pi


class TestPi(unittest.TestCase):
    def test_pi_with_valid_input(self):
        with self.assertRaises(SystemExit) as se:
            pi.main(lambda: '12', lambda: 'q')
        self.assertEqual(se.exception.code, 0)

    def test_pi_nan_input(self):
        with self.assertRaises(SystemExit) as se:
            pi.main(lambda: 'foo', lambda: 'q')
        self.assertEqual(se.exception.code, 0)

    def test_pi_input_too_large(self):
        with self.assertRaises(SystemExit) as se:
            pi.main(lambda: '400', lambda: 'q')
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
    unittest.main()
