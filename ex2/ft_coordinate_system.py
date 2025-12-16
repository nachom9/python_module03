#!/usr/bin/env python3

import math


def parse_coord(coord: str) -> tuple[int]:

    s_coord = coord.split(",")
    try:
        tup = tuple(int(i) for i in s_coord)
    except ValueError as error:
        print("Error parsing coordinates:", error)
        print(f'Error details - Type: ValueError, Args: ("{error}")')
        return
    diff = float(math.sqrt((tup[0]) ** 2 + (tup[1]) ** 2 + (tup[2]) ** 2))

    print("Position created:", tup)
    print(f"Distance between (0, 0, 0) and {tup}: {diff}")

    return tup


def unpack_coord(coord: tuple[int]) -> None:

    print(f"Player at x={coord[0]}, y={coord[1]}, z={coord[2]}")
    print(f"Coordinates: X={coord[0]}, Y={coord[1]}, Z={coord[2]}")


if __name__ == "__main__":

    print("=== Game Coordinate System ===\n")
    parse_coord("10,20,5")
    print('\nParsing coordinates: "3,4,0"')
    tup_coord = parse_coord("3,4,0")
    print('\nParsing invalid coordinates: "abc,def,ghi"')
    parse_coord("abc,def,ghi")
    print("\nUnpacking demonstration:")
    unpack_coord(tup_coord)
