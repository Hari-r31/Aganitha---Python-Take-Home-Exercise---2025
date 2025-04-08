# get_papers_list/utils.py

import csv
from typing import List, Dict

def write_to_csv(data: List[Dict], filename: str):
    if not data:
        print("No data to write.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
