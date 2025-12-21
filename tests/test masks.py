import unittest
from src.masks import get_mask_card_number, get_mask_account


class TestMasks(unittest.TestCase):

    def test_get_mask_card_number(self):
        self.assertEqual(get_mask_card_number(7000792289606361), "7000 79** **** 6361")
        self.assertEqual(get_mask_card_number("7000792289606361"), "7000 79** **** 6361")
        self.assertEqual(get_mask_card_number("7000 79 22 89 6063 61"), "7000 79** **** 6361")

        with self.assertRaises(ValueError):
            get_mask_card_number("123456789012345")  # менее 16 цифр

        with self.assertRaises(ValueError):
            get_mask_card_number("12345678901234567")  # более 16 цифр

        with self.assertRaises(ValueError):
            get_mask_card_number("abcdefghijklmnoq")  # нецифровой ввод

    def test_get_mask_account(self):
        self.assertEqual(get_mask_account(73654108430135874305), "**4305")
        self.assertEqual(get_mask_account("73654108430135874305"), "**4305")
        self.assertEqual(get_mask_account("12345678"), "**5678")

        with self.assertRaises(ValueError):
            get_mask_account("123")  # менее 4 цифр

        with self.assertRaises(ValueError):
            get_mask_account("abcde")  # нецифровой ввод


if __name__ == "__main__":
    unittest.main()