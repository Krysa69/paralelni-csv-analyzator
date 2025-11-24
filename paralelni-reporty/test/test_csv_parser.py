import unittest
import tempfile
import os
from parser.csv_parser import CsvParser

class TestCsvParser(unittest.TestCase):

    def test_parse_counts_rows(self):
        parser = CsvParser()

        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv") as f:
            f.write("a,b,c\n1,2,3\n4,5,6\n")
            path = f.name

        count = parser.parse(path)
        os.remove(path)

        self.assertEqual(count, 3)  # 3 řádky
