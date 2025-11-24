import unittest
from core.worker_pool import WorkerPool
from aggregation.aggregator import Aggregator
from parser.csv_parser import CsvParser
import tempfile
import os

class TestWorkerPool(unittest.TestCase):

    def test_worker_processes_file(self):
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv") as f:
            f.write("x,y\n1,2\n3,4\n")
            path = f.name

        agg = Aggregator()
        parser = CsvParser()
        pool = WorkerPool(2, agg, parser)

        pool.start()
        pool.file_queue.put(path)
        pool.stop()

        os.remove(path)

        self.assertEqual(agg.total_files, 1)
        self.assertEqual(agg.total_rows, 3)
