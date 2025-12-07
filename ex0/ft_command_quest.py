#!/usr/bin/env python3

import sys


def show_args() -> None:
    """
    Display the program name, each argument provided in the command line,
    and the total number of arguments.

    This function uses sys.argv, where:
      - sys.argv[0] is always the program's name/path
      - sys.argv[1:] are the arguments passed by the user
    """

    arg_nb = 1  # Counter to iterate through command‑line arguments
    print("=== Command Quest ===")

    # If only the program name is present, no arguments were passed
    if len(sys.argv) == 1:
        print("No arguments provided!")

    # Always print the program's name
    print(f"Program name: {sys.argv[0]}")

    # Loop through all arguments passed (if any)
    while arg_nb < len(sys.argv):
        print(f"Argument {arg_nb}: {sys.argv[arg_nb]}")
        arg_nb += 1

    # Display total number of arguments including the program name
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    # Entry point of the script
    show_args()
