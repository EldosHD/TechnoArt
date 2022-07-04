# TechnoArt

R.I.P [TechnoBlade](https://www.youtube.com/c/TechnoBlade)

This is pixel art renderer for the terminal. This program reads in a given pixel art file and prints it out to the terminal.
By default this program uses Technoblade pixelart. But you can either add own art to the img folder or specify a specific file with the `-i` flag. Since every pixel gets converted to a character, the maximum size of the art is limited to the terminal size. In my tests, the maximum size of the art was around 64x64. I've only tested png files so far.

![](screenshot.png)
## Installation

You need python 3 installed to use this program.
### Linux
Clone the repo to a folder of your choice. Then install the dependencies with the following command:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
python3 -m pip install --upgrade argparse
```
You should consider creating a simbolic link to the `technoart.py` file in your `bin` folder with `sudo ln -s LOCATION/technoart.py /usr/local/bin/technoart`. Just replace the LOCATION with the location of the `technoart.py` file.

### Windows
Clone the repo to a folder of your choice. Then install the dependencies with pip like in the linux section.

### MacOS
Clone the repo to a folder of your choice. Then install the dependencies with pip like in the linux section.

## Contributing

Any type of code contribution is of course welcome. But right now this program needs more pixel art.