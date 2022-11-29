#!/usr/bin/env python3

"""
Stanford CS106A TipTop Project
"""

import sys
from pathlib import Path
from typing import DefaultDict, List

# define functions here


def get_tags(lines: List[str], separator: str = "^"):
    all_tags = DefaultDict(set)

    for line in lines:
        user, *tags = line.split(separator)
        for tag in tags:
            all_tags[tag.lower()].add(user.lower())

    return all_tags


def dump_tags(tags: dict[str, set[str]]):
    for tag in sorted(tags.keys()):
        users = "\n ".join(sorted(tags[tag]))
        print(f"{tag}:\n {users}")


def read_files(files: List[Path]):
    lines: List[str] = []
    for file in files:
        lines.extend(file.read_text().splitlines())

    return lines


def main():
    args = sys.argv[1:]

    files = []
    for arg in args:
        file = Path(arg)
        if not file.exists() or not file.is_file():
            continue

        files.append(file)

    content = read_files(files)
    tags = get_tags(content)
    dump_tags(tags)


if __name__ == "__main__":
    main()
