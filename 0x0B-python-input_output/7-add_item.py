#!/usr/bin/python3
"""Module for a script to execute arguments"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


name = "add_item.json"
lis = []

for count in range(1, len(sys.argv)):
    lis.append(sys.argv[count])

try:
    file = load_from_json_file(name)
    file.extend(lis)
    save_to_json_file(file, name)
except Exception:
    with open(name, 'w') as file_0:
        pass
    save_to_json_file(lis, name)
