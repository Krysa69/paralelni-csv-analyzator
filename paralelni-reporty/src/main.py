import time
from core.logging_setup import setup_logging
from core.worker_pool import WorkerPool
from parser.csv_parser import CsvParser
from aggregation.aggregator import Aggregator
from loader.file_loader import load_files_into_queue
from export.exporter import export_report
from config import NUM_WORKERS

logger = setup_logging()

def main():
    logger.info("Spouštím aplikaci...")

    start = time.time()

    aggregator = Aggregator()
    parser = CsvParser()
    pool = WorkerPool(NUM_WORKERS, aggregator, parser)

    pool.start()
    load_files_into_queue(pool.file_queue)
    pool.stop()

    total_duration = time.time() - start

    export_path = export_report(aggregator, total_duration)
    logger.info(f"Hotovo. Report vygenerován: {export_path}")

if __name__ == "__main__":
    main()
