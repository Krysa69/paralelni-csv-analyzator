import csv

class CsvParser:
    def parse(self, filepath):
        count = 0

        with open(filepath, encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                count += 1

        return count
