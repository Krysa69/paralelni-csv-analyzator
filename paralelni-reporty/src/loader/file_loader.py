import os
from config import INPUT_DIR

def load_files_into_queue(file_queue):
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".csv"):
            filepath = os.path.join(INPUT_DIR, filename)
            file_queue.put(filepath)
