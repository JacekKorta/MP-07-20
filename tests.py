import unittest

from main import fix_the_boxes


class TestMainTask(unittest.TestCase):

    def test_data_validation_input_is_string(self):
        self.assertEqual(fix_the_boxes('test string'), 'Input data should be an integer in the range 1-100')

    def test_data_validation_input_is_out_of_range(self):
        self.assertEqual(fix_the_boxes(101), 'Input data should be an integer in the range 1-100')
        self.assertEqual(fix_the_boxes(0), 'Input data should be an integer in the range 1-100')

    def test_data_validation_input_is_negative(self):
        self.assertEqual(fix_the_boxes(-1), 'Input data should be an integer in the range 1-100')


if __name__ == '__main__':
    unittest.main()