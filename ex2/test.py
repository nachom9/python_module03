#!/usr/bin/env python3

import math


def coordinates(coord: str) -> tuple[int]:
    """
    Parse a coordinate string and compute its distance from the origin.

    Parameters
    ----------
    coord : str
        Coordinate values separated by commas, e.g., "3,4,0".
        The function expects exactly three numeric values.

    Behavior
    --------
    - Splits the input string by commas.
    - Attempts to convert each part into an integer.
    - If successful:
        * Prints the coordinate as a tuple of integers.
        * Computes the Euclidean distance from (0,0,0).
        * Prints the computed distance.
    - If conversion fails:
        * Prints an error message mimicking Python's ValueError format.
        * Stops execution for this coordinate.

    Errors
    ------
    - ValueError
        Triggered when one or more coordinate values cannot be converted
        to integers (e.g., "abc,20,5").

    Notes
    -----
    - The function assumes the coordinate string contains exactly three values.
    - Distance formula used:
          d = sqrt(x² + y² + z²)
    """
    coord = coord.split(",")
    try:
        num = tuple(int(i) for i in coord)
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error}")
        return

    print(f"Position created: {num}")
    d = float(math.sqrt(num[0]**2 + num[1]**2 + num[2]**2))
    print(f"Distance between (0, 0, 0) and {num}: {d}")
    return num


def unpack_coordinates(coords: tuple[int]) -> None:
    print(f"Player at x={coords[0]}, y={coords[1]}, z={coords[2]}")
    print(f"Coordinates: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")


def main() -> None:
    """
    Demonstrate the coordinate parser with multiple test cases.

    Behavior
    --------
    - Prints formatted section headers.
    - Tests the coordinates() function with:
        * Valid coordinate input
        * Another valid input
        * Fully invalid input
    - Ensures the program continues running even when errors occur.
    """
    print("=== Game Coordinate System ===\n")
    coordinates("10,20,5")
    print("\nParsing coordinates: \"3,4,0\"")
    coordinates("3,4,0")
    print("\nParsing coordinates: \"abc,def,ghi\"")
    coordinates("abc,def,ghi")
    print("\nUnpacking demonstration:")
    coords = coordinates("3,4,0")
    unpack_coordinates(coords)


if __name__ == "__main__":
    main()


