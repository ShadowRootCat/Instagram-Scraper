import re
import os
import json
from datetime import datetime

DATA_DIR = '../data_files'

PATTERNS = {
    "Emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "Phone Numbers": r"\+?[0-9\s\-]{10,15}",
}

def extract_pii(file_content):
    results = {}
    for category, pattern in PATTERNS.items():
        matches = re.findall(pattern, file_content)
        if matches:
            results[category] = matches
    return results

def main():
    data = {}
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.txt'):
            with open(os.path.join(DATA_DIR, filename), 'r') as file:
                data[filename] = extract_pii(file.read())
    with open(f"pii_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()
