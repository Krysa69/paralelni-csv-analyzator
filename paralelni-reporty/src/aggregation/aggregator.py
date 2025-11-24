import threading

class Aggregator:
    def __init__(self):
        self.lock = threading.Lock()
        self.total_files = 0
        self.total_rows = 0
        self.errors = []
        self.file_stats = []

    def add_file(self, filename, row_count, duration):
        """Uloží statistiky o jednom zpracovaném souboru."""
        with self.lock:
            self.total_files += 1
            self.total_rows += row_count
            self.file_stats.append({
                "name": filename,
                "rows": row_count,
                "time": duration
            })

    def add_error(self, message):
        """Uloží text chyby."""
        with self.lock:
            self.errors.append(message)
