# TechnoArt

R.I.P [TechnoBlade](https://www.youtube.com/c/TechnoBlade)

This is pixel art renderer for the terminal. This program reads in a given pixel art file and prints it out to the terminal.
By default this program uses Technoblade pixelart. But you can either add own art to the img folder or specify a specific file with the `-i` flag. Since every pixel gets converted to a character, the maximum size of the art is limited to the terminal size. In my tests, the maximum size of the art was around 64x64. I've only tested png files so far.
## Installation

### Linux
```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
python3 -m pip install --upgrade argparse
```
You should consider creating a simbolic link to the `technoart.py` file in your `bin` folder with `ln -s technoart.py /usr/local/bin/technoart`.

## Contributing

Any type of code contribution is of course welcome. But right now this program needs more pixel art.