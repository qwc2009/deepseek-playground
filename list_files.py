#!/usr/bin/env python3
import os
import sys

def list_files(path="."):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        indent = " " * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 2 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    list_files(target)
