import unittest

from mp_main import main


class TestDataValidation(unittest.TestCase):
    """Test data validation. The Input data should be an integer in the range 1-100"""
    def test_data_validation_input_is_string(self):
        self.assertEqual(main('test string'), 'Input data should be an integer in the range 1-100')

    def test_data_validation_input_is_out_of_range(self):
        self.assertEqual(main(101), 'Input data should be an integer in the range 1-100')
        self.assertEqual(main(0), 'Input data should be an integer in the range 1-100')

    def test_data_validation_input_is_negative(self):
        self.assertEqual(main(-1), 'Input data should be an integer in the range 1-100')


class TestDataFromTable(unittest.TestCase):
    """Tests the data from the source table (pdf)"""
    def test_data_is_1_expect_1s(self):
        self.assertEqual(main(1), {'small': 1, 'medium': 0, 'large': 0, 'bulk': 0})

    def test_data_is_2_expect_1s(self):
        self.assertEqual(main(2), {'small': 1, 'medium': 0, 'large': 0, 'bulk': 0})

    def test_data_is_3_expect_1s(self):
        self.assertEqual(main(3), {'small': 1, 'medium': 0, 'large': 0, 'bulk': 0})

    def test_data_is_4_expect_1m(self):
        self.assertEqual(main(4), {'small': 0, 'medium': 1, 'large': 0, 'bulk': 0})

    def test_data_is_5_expect_1m(self):
        self.assertEqual(main(5), {'small': 0, 'medium': 1, 'large': 0, 'bulk': 0})

    def test_data_is_6_expect_1m(self):
        self.assertEqual(main(6), {'small': 0, 'medium': 1, 'large': 0, 'bulk': 0})

    def test_data_is_7_expect_1l(self):
        self.assertEqual(main(7), {'small': 0, 'medium': 0, 'large': 1, 'bulk': 0})

    def test_data_is_8_expect_1l(self):
        self.assertEqual(main(8), {'small': 0, 'medium': 0, 'large': 1, 'bulk': 0})

    def test_data_is_9_expect_1l(self):
        self.assertEqual(main(9), {'small': 0, 'medium': 0, 'large': 1, 'bulk': 0})

    def test_data_is_10_expect_2m_1b(self):
        self.assertEqual(main(10), {'small': 0, 'medium': 2, 'large': 0, 'bulk': 1})

    def test_data_is_11_expect_2m_1b(self):
        self.assertEqual(main(11), {'small': 0, 'medium': 2, 'large': 0, 'bulk': 1})

    def test_data_is_12_expect_2m_1b(self):
        self.assertEqual(main(10), {'small': 0, 'medium': 2, 'large': 0, 'bulk': 1})

    def test_data_is_13_expect_2l_1b(self):
        self.assertEqual(main(13), {'small': 0, 'medium': 0, 'large': 2, 'bulk': 1})

    def test_data_is_14_expect_2l_1b(self):
        self.assertEqual(main(14), {'small': 0, 'medium': 0, 'large': 2, 'bulk': 1})

    def test_data_is_15_expect_2l_1b(self):
        self.assertEqual(main(15), {'small': 0, 'medium': 0, 'large': 2, 'bulk': 1})

    def test_data_is_16_expect_2l_1b(self):
        self.assertEqual(main(16), {'small': 0, 'medium': 0, 'large': 2, 'bulk': 1})

    def test_data_is_17_expect_2l_1b(self):
        self.assertEqual(main(17), {'small': 0, 'medium': 0, 'large': 2, 'bulk': 1})

    def test_data_is_19_expect_1s_2l_1b(self):
        self.assertEqual(main(19), {'small': 1, 'medium': 0, 'large': 2, 'bulk': 1})

    def test_data_is_21_expect_1s_2l_1b(self):
        self.assertEqual(main(21), {'small': 1, 'medium': 0, 'large': 2, 'bulk': 1})

    def test_data_is_22_expect_1m_2l_1b(self):
        self.assertEqual(main(22), {'small': 0, 'medium': 1, 'large': 2, 'bulk': 1})

    def test_data_is_24_expect_1m_2l_1b(self):
        self.assertEqual(main(24), {'small': 0, 'medium': 1, 'large': 2, 'bulk': 1})

    def test_data_is_25_expect_3l_1b(self):
        self.assertEqual(main(25), {'small': 0, 'medium': 0, 'large': 3, 'bulk': 1})

    def test_data_is_26_expect_3l_1b(self):
        self.assertEqual(main(26), {'small': 0, 'medium': 0, 'large': 3, 'bulk': 1})

    def test_data_is_27_expect_1m_2l_1b(self):
        self.assertEqual(main(27), {'small': 0, 'medium': 0, 'large': 3, 'bulk': 1})

    def test_data_is_28_expect_1s_3l_2b(self):
        self.assertEqual(main(28), {'small': 1, 'medium': 0, 'large': 3, 'bulk': 2})

    def test_data_is_30_expect_1s_3l_2b(self):
        self.assertEqual(main(30), {'small': 1, 'medium': 0, 'large': 3, 'bulk': 2})

    def test_data_is_31_expect_1m_3l_2b(self):
        self.assertEqual(main(31), {'small': 0, 'medium': 1, 'large': 3, 'bulk': 2})

    def test_data_is_33_expect_1m_3l_2b(self):
        self.assertEqual(main(33), {'small': 0, 'medium': 1, 'large': 3, 'bulk': 2})

    def test_data_is_34_expect_4l_2b(self):
        self.assertEqual(main(34), {'small': 0, 'medium': 0, 'large': 4, 'bulk': 2})

    def test_data_is_36_expect_4l_2b(self):
        self.assertEqual(main(36), {'small': 0, 'medium': 0, 'large': 4, 'bulk': 2})

    def test_data_is_99_expect_11l_4b(self):
        self.assertEqual(main(99), {'small': 0, 'medium': 0, 'large': 11, 'bulk': 4})

    def test_data_is_100_expect_1s_11l_4b(self):
        self.assertEqual(main(100), {'small': 1, 'medium': 0, 'large': 11, 'bulk': 4})


class TestItemsCover(unittest.TestCase):
    """Tests if all items are in the box"""
    def test_items_cover(self):
        for qty in range(1, 101):
            boxes = main(qty)
            self.assertLessEqual(qty, (boxes['small']*3 + boxes['medium']*6 + boxes['large']*9))


if __name__ == '__main__':
    unittest.main()