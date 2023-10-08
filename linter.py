#!/usr/bin/python
import os

if __name__ == "__main__":
    for file in os.listdir("."):
        if os.path.splitext(file)[1] == ".py":
            os.system(f"isort {file}")
            os.system(f"black {file}")
            os.system(f"pylint {file}")
