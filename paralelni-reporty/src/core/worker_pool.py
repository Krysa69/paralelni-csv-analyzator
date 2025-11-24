import threading
import queue
import time

class WorkerPool:
    def __init__(self, num_workers, aggregator, parser):
        self.num_workers = num_workers
        self.aggregator = aggregator
        self.parser = parser

        # fronta souborů k práci
        self.file_queue = queue.Queue()

        # stop signál pro ukončení workerů
        self.stop_signal = object()

        # seznam běžících vláken
        self.workers = []

    def start(self):
        """Spustí worker vlákna."""
        for _ in range(self.num_workers):
            t = threading.Thread(target=self.worker_loop)
            t.start()
            self.workers.append(t)

    def worker_loop(self):
        """Hlavní smyčka každého workeru."""
        while True:
            filepath = self.file_queue.get()

            # ukončení při signálu
            if filepath is self.stop_signal:
                break

            start = time.time()

            try:
                # zpracování CSV
                row_count = self.parser.parse(filepath)
                duration = round(time.time() - start, 4)
                self.aggregator.add_file(filepath, row_count, duration)

            except Exception as e:
                self.aggregator.add_error(f"{filepath}: {e}")

    def stop(self):
        """Bezpečné ukončení workerů."""
        # pošle stop signály
        for _ in range(self.num_workers):
            self.file_queue.put(self.stop_signal)

        # počká, než všechna vlákna skončí
        for t in self.workers:
            t.join()
