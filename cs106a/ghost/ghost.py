#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""

import math
import os
import sys
from pathlib import Path
from time import time
from typing import List, Optional, Tuple, Union

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage

Pix = Tuple[Union[float, int], Union[float, int], Union[float, int]]

CHANNELS = 3


def pix_dist2(pix1: Pix, pix2: Pix):
    return sum((pix1[i] - pix2[i]) ** 2 for i in range(CHANNELS))


def average_pix(pixs: List[Pix]) -> Pix:
    return tuple(sum([pix[i] for pix in pixs]) / len(pixs) for i in range(CHANNELS))


def best_pix(pixs: List[Pix]) -> Pix:
    """
    Given a list of 1 or more pix, returns the best pix.
    """
    avg_pix = average_pix(pixs)
    return min(pixs, key=lambda pix: pix_dist2(pix, avg_pix))


def good_apple_pix(pixs: List[Pix]) -> Pix:
    """
    Given a list of 2 or more pix, return the best pix
    according to the good-apple strategy.
    >>> good_apple_pix([(18, 18, 18), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 2, 0), (1, 0, 1)])
    (20, 20, 20)
    """
    avg_pix = average_pix(pixs)
    good_half = sorted(pixs, key=lambda pix: pix_dist2(pix, avg_pix))[: len(pixs) // 2]
    return best_pix(good_half)


def solve(images: List[SimpleImage], mode: Optional[str]):
    """
    Given a list of image objects and mode,
    compute and show a Ghost solution image based on these images.
    Mode will be None or '-good'.
    There will be at least 3 images and they will all be
    the same size.
    """

    start_time = time()

    width = images[0].width
    height = images[0].height
    solution = SimpleImage.blank(width, height)

    for x in range(width):
        for y in range(height):
            pixs = [image.get_pix(x, y) for image in images]
            pix: Pix = (0, 0, 0)

            if mode == "-good":
                pix = good_apple_pix(pixs)
            elif mode is None:
                pix = best_pix(pixs)

            solution.set_pix(x, y, pix)

    solution.show()
    print(f"Time: {(time() - start_time):.2f}s")


def jpgs_in_dir(dir: str) -> List[Path]:
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for file in Path(dir).iterdir():
        if file.suffix == ".jpg":
            filenames.append(file)
    return filenames


def load_images(dir: str) -> List[SimpleImage]:
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage.file(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # Command line args
    # 1 arg:  dir-of-images
    # 2 args: -good dir-of-images
    if len(args) == 1:
        images = load_images(args[0])
        solve(images, None)

    if len(args) == 2 and args[0] == "-good":
        images = load_images(args[1])
        solve(images, "-good")


if __name__ == "__main__":
    main()
