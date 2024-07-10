import os
import json
import glob
import argparse
from collections import Counter

def parse_args():
    parser = argparse.ArgumentParser(description="Count rhetorical devices in JSON files.")

    return parser.parse_args()

def collect_samples():
    def collect_single_device_samples(directory='./data/raw/single_rhetorical_device'):
        json_files = glob.glob(os.path.join(directory, "*.json"))
        samples = []

        for file in json_files:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data:
                    samples.append(data[0])
        
        return samples

    def collect_multiple_device_samples(directory='./data/raw/multiple_rhetorical_devices'):
        json_files = glob.glob(os.path.join(directory, "*.json"))
        json_files.sort()
        samples = []

        with open(json_files[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
            if data:
                samples.append(data[0])
        
        return samples

    samples = collect_single_device_samples()
    samples += collect_multiple_device_samples()

    with open("./data/sample/samples.json", 'w', encoding='utf-8') as f:
        json.dump(samples, f, indent=4, ensure_ascii=False)

def count_rhetorical_devices(directory='./data/raw'):
    rhetorical_device_counter = Counter()

    # Walk through the directory and subdirectories
    for root, _, files in os.walk(directory):
        files.sort()
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        for item in data:
                            if 'rhetorical_device' in item:
                                rhetorical_device_counter.update(item['rhetorical_device'])
                    except (json.JSONDecodeError, TypeError):
                        print(f"Error reading {file_path}, skipping.")

    with open("./metadata/rhetorical_device_counts.csv", 'w', encoding='utf-8') as f:
        for device, count in rhetorical_device_counter.items():
            f.write(f"{device},{count}\n")

    return rhetorical_device_counter

def main():
    args = parse_args()

    # Collect samples
    collect_samples()

    # Count rhetorical devices
    count_rhetorical_devices()

if __name__ == "__main__":
    main()