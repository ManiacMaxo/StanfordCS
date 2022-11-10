#!/usr/bin/env python3

"""
Stanford CS106A BabyNames Project
Part-A: organizing the bulk data
"""

import sys
from pathlib import Path
from typing import Dict, List

Names = Dict[str, Dict[int, int]]


def add_name(names: Names, year: int, rank: int, name: str):
    """
    Add the given data: int year, int rank, str name
    to the given names dict and return it.
    (1 test provided, more tests TBD)
    >>> add_name({}, 2000, 10, 'Abe')
    {'Abe': {2000: 10}}
    >>> # pass - more tests TBD
    """
    if name not in names:
        names.update({name: {}})

    if names[name].get(year) is None:
        # otherwise it will overwrite the existing value
        names[name].update({year: rank})

    return names


def add_file(names: Names, filename: str):
    """
    Given a names dict and babydata.txt filename, add the file's data
    to the dict and return it.
    (Tests provided, Code TBD)
    >>> add_file({}, 'small-2000.txt')
    {'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}
    >>> add_file({}, 'small-2010.txt')
    {'Yot': {2010: 1}, 'Zena': {2010: 1}, 'Bob': {2010: 2}, 'Alice': {2010: 2}}
    >>> add_file({'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}, 'small-2010.txt')
    {'Bob': {2000: 1, 2010: 2}, 'Alice': {2000: 1, 2010: 2}, 'Cindy': {2000: 2}, 'Yot': {2010: 1}, 'Zena': {2010: 1}}
    """
    year, *lines = Path(filename).read_text().splitlines()

    for line in lines:
        rank, m_name, f_name = line.strip().split(",")
        add_name(names, int(year), int(rank), m_name)
        add_name(names, int(year), int(rank), f_name)

    return names


def read_files(filenames: List[str]) -> Names:
    """
    Given list of filenames, build and return a names dict
    of all their data.
    """

    names: Names = {}

    for filename in filenames:
        add_file(names, filename)

    return names


def search_names(names: Names, target: str) -> List[str]:
    """
    Given names dict and a target string,
    return a sorted list of all the name strings
    that contain that target string anywhere.
    Not case sensitive.
    (Code and tests TBD)
    """
    return sorted(
        [name for name in names.keys() if target.casefold() in name.casefold()]
    )


def print_names(names: Names):
    """
    (provided)
    Given names dict, print out all its data, one name per line.
    The names are printed in increasing alphabetical order,
    with its years data also in increasing order, like:
    Aaden [(2010, 560)]
    Aaliyah [(2000, 211), (2010, 56)]
    ...
    Surprisingly, this can be done with 2 lines of code.
    We'll explore this in lecture.
    """
    for key, value in sorted(names.items()):
        print(key, sorted(value.items()))


def main():
    # (provided)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ""
    if len(args) >= 2 and args[0] == "-search":
        target = args[1]
        filenames = args[2:]  # Change filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == "__main__":
    main()
