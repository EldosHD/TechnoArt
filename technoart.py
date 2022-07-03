#!/usr/bin/python3
# converts a random img to pixelart
block = "▀"


def printForground(r, g, b):
    """Prints out the escape code for the given forground color. That will color the upper pixel."""
    print(f"\x1b[38;2;{r};{g};{b}mm", end="")


def printBackground(r, g, b):
    """Prints out the escape code for the given background color. That will color the lower pixel."""
    print(f"\x1b[48;2;{r};{g};{b}m", end="")


def printReset():
    """Prints out the escape code for resetting the color."""
    print("\x1b[0m", end="")

printForground(173, 148, 111)
print("hey")
printReset()


