#!/usr/bin/env python3

"""
Stanford CS106A Waterfall warmup
"""

import random
import sys
import tkinter
from typing import Callable, Literal, Union

import drawcanvas
from grid import Grid

SIDE = 15  # pixels across of one square
WATER_FACTOR = 20  # 1 out of this factor is water in top edge
ROCK_FACTOR = 10  # 1 out of this factor is rock at the start


def is_move_ok(grid: Grid, x_to: int, y_to: int) -> bool:
    """
    Given a grid and possibly out-of-bounds x_to, y_to
    return True if that destination is ok, False otherwise.
    (tests provided, code TBD)
    >>> grid = Grid.build([['w', 'w', 'w'], ['r', None, 'w']])
    >>> is_move_ok(grid, 1, 1)   # down ok
    True
    >>> is_move_ok(grid, -1, 1)  # out-of-bounds left
    False
    >>> is_move_ok(grid, 0, 1)   # down blocked
    False
    >>> is_move_ok(grid, 2, 1)   # down blocked
    False
    >>> is_move_ok(grid, 2, 2)   # out-of-bounds down
    False
    """
    # out of bounds
    try:
        if not grid.get(x_to, y_to):
            return False
    except:
        return False

    return True


def safe_get(
    grid: Grid, x: int, y: int
) -> Union[Literal[False], None, Literal["w"], Literal["r"]]:
    """Get a value from the grid, or False if out of bounds."""
    try:
        return grid.get(x, y)
    except:
        return False


def move_water(grid: Grid, x: int, y: int):
    """
    There is water at the given x,y.
    Move the water to one of the 3 squares below,
    or erase it, as described in the handout.
    Return the grid when done.
    (tests provided, code TBD)
    >>> grid = Grid.build([['w', 'w', 'w'], ['r', None, 'w']])
    >>> move_water(grid, 1, 0)  # down ok
    [['w', None, 'w'], ['r', 'w', 'w']]
    >>> grid = Grid.build([['w', 'w', 'w'], ['r', None, 'w']])
    >>> move_water(grid, 0, 0)  # down right
    [[None, 'w', 'w'], ['r', 'w', 'w']]
    >>> grid = Grid.build([['w', 'w', 'w'], ['r', None, 'w']])
    >>> move_water(grid, 2, 0)  # down left
    [['w', 'w', None], ['r', 'w', 'w']]
    >>> grid = Grid.build([['w', 'w', 'w'], ['r', None, 'w']])
    >>> move_water(grid, 2, 1)  # nowhere to go - disappears
    [['w', 'w', 'w'], ['r', None, None]]
    """

    if safe_get(grid, x, y + 1) is None:
        grid.set(x, y + 1, "w")

    if safe_get(grid, x - 1, y + 1) is None:
        grid.set(x - 1, y + 1, "w")

    if safe_get(grid, x + 1, y + 1) is None:
        grid.set(x + 1, y + 1, "w")

    grid.set(x, y, None)

    return grid


def move_all_water(grid: Grid):
    """
    Move every water 'w' in the world
    once by calling move_water() for each.
    (provided)
    """
    # tricky: do y in reverse direction so each
    # water moves only once.
    for y in reversed(range(grid.height)):
        for x in range(grid.width):
            if grid.get(x, y) == "w":
                move_water(grid, x, y)
    return grid


def set_top(grid: Grid):
    """
    Set random squares at the top row, y=0, to
    have water in them.
    (provided)
    """
    for x in range(grid.width):
        if random.randrange(WATER_FACTOR) == 0:
            grid.set(x, 0, "w")
    return grid


def init_rocks(grid: Grid):
    """
    Set a random selection of squares to be rock 'r'
    to initialize the grid.
    (provided)
    """
    for y in range(grid.height):
        for x in range(grid.width):
            if random.randrange(ROCK_FACTOR) == 0:
                grid.set(x, y, "r")
    return grid


# ************* Utility Functions Below here


def draw_grid_canvas(grid: Grid, canvas: tkinter.Canvas):
    """
    Draw the grid to the canvas.
    """
    canvas.delete("all")
    canvas.create_rectangle(0, 0, grid.width * SIDE, grid.height * SIDE, fill="black")

    for y in range(grid.height):
        for x in range(grid.width):
            val = grid.get(x, y)
            if val:
                pixel_x = SIDE * x
                pixel_y = SIDE * y
                canvas.create_text(
                    pixel_x,
                    pixel_y,
                    text=val,
                    anchor=tkinter.NW,
                    fill="white",
                    font=("Courier", 20),
                )

    canvas.update()


def do_one_round(grid: Grid, canvas: tkinter.Canvas):
    """Do one round of the move, call in timer."""
    set_top(grid)
    draw_grid_canvas(grid, canvas)
    move_all_water(grid)


# TK Timer fns:


def start_timer(top: tkinter.Canvas, delay_ms: int, fn: Callable):
    """Start the my_timer system, calls given fn"""
    top.after(delay_ms, lambda: my_timer(top, delay_ms, fn))


def my_timer(top: tkinter.Canvas, delay_ms: int, fn: Callable):
    """my_timer callback, re-posts itself."""
    fn()
    top.after(delay_ms, lambda: my_timer(top, delay_ms, fn))


def main():
    args = sys.argv[1:]

    width = 50
    height = 30

    # Optional command line setting of -width- -height-
    if len(args) == 2:
        width = int(args[0])
        height = int(args[1])
    grid = Grid(width, height)
    init_rocks(grid)

    canvas = drawcanvas.make_canvas(width * SIDE, height * SIDE, "Waterfall")
    draw_grid_canvas(grid, canvas)

    start_timer(canvas, 30, lambda: do_one_round(grid, canvas))

    drawcanvas.DrawCanvas.mainloop()


if __name__ == "__main__":
    main()
