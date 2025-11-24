import unittest
from aggregation.aggregator import Aggregator

class TestAggregator(unittest.TestCase):

    def test_add_file(self):
        agg = Aggregator()

        agg.add_file(10)
        agg.add_file(5)

        self.assertEqual(agg.total_files, 2)
        self.assertEqual(agg.total_rows, 15)

    def test_add_error(self):
        agg = Aggregator()
        agg.add_error("chyba")
        self.assertIn("chyba", agg.errors)
