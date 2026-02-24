# ASCII-TOOL
This is a small tool to convert images to ascii art. I made it in a very short amount of time as a small side project so its nothing big.

## Installation

### Using pip
Just type `pip install ascii-tool` into the command line.

### Using AUR (arch only)
If you are on Arch Linux you can also use your favourite AUR helper to install it. for example: `yay -S ascii-tool`

## Usage

### GUI
If you simply type `ascii-tool` it will launch the GUI where you can visually select an Image to turn into ascii.

### Command Line
If you want to convert an image directly inside your terminal you can type `ascii-tool` along with the path to your image.
```
ascii-tool /path/to/your/img
```
If you would like to specify the size of the output you can use the `-width` parameter. By default it's 120.
```
ascii-tool /path/to/your/img -width 90
```