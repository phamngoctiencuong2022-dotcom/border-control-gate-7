# Câu 4a: Đọc JSON và in tên người có tuổi lớn nhất
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
json_file = os.path.join(script_dir, "data.json")

# Create test JSON if not exists
if not os.path.exists(json_file):
    data = [
        {"ten": "Alice", "tuoi": 30},
        {"ten": "Bob", "tuoi": 25},
        {"ten": "Charlie", "tuoi": 40}
    ]
    with open(json_file, 'w') as f:
        json.dump(data, f)

with open(json_file, 'r') as f:
    people = json.load(f)
    oldest = max(people, key=lambda x: x["tuoi"])
    print(oldest["ten"])
