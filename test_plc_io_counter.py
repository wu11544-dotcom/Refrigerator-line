"""使用虚构地址验证 PLC I/O 统计。"""

import unittest

from plc_io_counter import count_io_addresses


class TestPlcIoCounter(unittest.TestCase):
    def test_normal_counts(self):
        self.assertEqual(
            count_io_addresses(["X0", "X1", "Y0", "Y1"]),
            {"X": 2, "Y": 2, "duplicates": []},
        )

    def test_duplicate_addresses(self):
        self.assertEqual(
            count_io_addresses(["X0", "X1", "Y0", "Y1", "X1"]),
            {"X": 2, "Y": 2, "duplicates": ["X1"]},
        )
        self.assertEqual(
            count_io_addresses(["Y1", "X0", "Y1", "X0", "Y1"]),
            {"X": 1, "Y": 1, "duplicates": ["Y1", "X0"]},
        )

    def test_empty_list(self):
        self.assertEqual(
            count_io_addresses([]),
            {"X": 0, "Y": 0, "duplicates": []},
        )


if __name__ == "__main__":
    unittest.main()
