#!/usr/bin/python3
# converts a random img to pixelart
from PIL import Image
from os import listdir
import argparse
import random

block = "▀"

defaultImg = "./img/technoFaceSmall.png"
version = 1.0
epilog = f"""
Written by: EldosHD
Version: {version}
This program is licensed under the GNU General Public License v3.0
\x1b[5m\x1b[38;5;213mIn memory of Technoblade\x1b[0m
https://www.youtube.com/c/Technoblade"""


def printForground(r, g, b):
    """Prints out the escape code for the given forground color. That will color the upper pixel."""
    print(f"\x1b[38;2;{r};{g};{b}m", end="")


def printBackground(r, g, b):
    """Prints out the escape code for the given background color. That will color the lower pixel."""
    print(f"\x1b[48;2;{r};{g};{b}m", end="")


def printReset():
    """Prints out the escape code for resetting the color."""
    print("\x1b[0m", end="")


def spacePrint(width, height, img):
    """Prints the given pic using spaces as pixels. Should be used for small pictures."""
    for y in range(height):
        for x in range(width):
            # load pixeldata from image
            pixel_data = img.getpixel((x, y))
            if len(pixel_data) == 3:
                r, g, b = pixel_data
            elif len(pixel_data) == 4:
                r, g, b, a = pixel_data
            else:
                print("Error: Pixel data has wrong length.")
                exit(1)

            # print pixel
            printBackground(r, g, b)
            print("  ", end="")
            printReset()
        print()


def blockPrint(width, height, img):
    """Prints the given pic using blocks as pixels. Should be used for large pictures."""
    for y in range(height):
        if (y % 2 == 0):
            for x in range(width):
                # load pixeldata from image
                pixel_data = img.getpixel((x, y))
                if len(pixel_data) == 3:
                    r, g, b = pixel_data
                elif len(pixel_data) == 4:
                    r, g, b, a = pixel_data
                else:
                    print("Error: Pixel data has wrong length.")
                    exit(1)

                if y + 1 in range(height):
                    # load pixeldata from image
                    pixel_data = img.getpixel((x, y + 1))
                    if len(pixel_data) == 3:
                        r2, g2, b2 = pixel_data
                    elif len(pixel_data) == 4:
                        r2, g2, b2, a2 = pixel_data
                    else:
                        print("Error: Pixel data has wrong length.")
                        exit(1)
                else:
                    r2, g2, b2, a2 = 0, 0, 0, 0
                printForground(r, g, b)
                printBackground(r2, g2, b2)
                print(block, end="")
                printReset()
            print()
        else:
            pass


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="This program prints \x1b[38;5;213mTechnoblade\x1b[0m fanart to the terminal. It comes with a few arts by default, but you can specify your own image with the -i flag.",
        epilog=epilog
    )

    mode = parser.add_mutually_exclusive_group()
    imgPickMode = parser.add_mutually_exclusive_group()
    mode.add_argument("-b", "--block-mode", action="store_true", default=True,
                      help="uses a unicode block and background colors to render each pixel. This way each pixel from the source will end up at 8x8 pixels in the terminal. Use this if the img is big. This is the default mode. Only one mode can be used at once")
    mode.add_argument("-s", "--space-mode", action="store_true", default=False,
                      help="uses spaces as pixels. This way each pixel from the source will end up at 16x16 pixels in the terminal. Use this if the img is small")

    imgPickMode.add_argument("-r", "--random", action="store_true",
                             help="picks a random image from the image folder. This option can't be used with the -i flag")
    imgPickMode.add_argument(
        "-i", "--image", help="specifies the image to use. If not specified, a 8x8 pixel technoface will be used. This option can't be used with the -r flag",
        default=defaultImg)
    parser.add_argument("--version", action="version",
                        version="%(prog)s " + str(version))

    args = parser.parse_args()

    if args.random:
        imgList = listdir("./img")
        randImg = imgList[random.randint(0, len(imgList) - 1)]
        args.image = f"./img/{randImg}"

    img = Image.open(args.image)
    width, height = img.size

    if args.space_mode:
        spacePrint(width, height, img)
    elif args.block_mode:
        blockPrint(width, height, img)
    else:
        print("Error: No mode selected")
        exit(1)


if __name__ == "__main__":
    main()
    exit(0)
