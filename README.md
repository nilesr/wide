# Tool for splitting a multi monitor wallpaper into individual images

## Dependancies
- [Pillow](https://pypi.python.org/pypi/Pillow)
- xrandr

## Usage

`python3 wide.py wide_base.png`

If you are using xfce4, this will automatically set the wallpaper for each screen to the newly generated image. If you aren't, it will at least generate the images. Each monitor's image is listed as its monitor index from left to right. It scrapes the output of `xrandr -q` to get the current display configuration.

### Offset

By default `wide.py` starts at the left of the image. To start from the middle, specify an additional argument `middle`. Otherwise, specify a number of pixels from the left to offset

`python3 wide.py wide_base.png middle`

`python3 wide.py wide_base.png 250`

## Example

My xrandr setup at home looks like this
![](http://i.imgur.com/jyr1vtr.png)

The base image I used was this
![](http://i.imgur.com/Q5NjyQc.jpg)

After running `python3 wide.py wide_base.png` it created three images:
![](http://i.imgur.com/Xydzqpw.jpg)
![](http://i.imgur.com/Mlnog8c.jpg)
![](http://i.imgur.com/tUGvU8v.jpg)

It then set my wallpaper for each monitor to the appropriate image. A screenshot looked like this
![](http://i.imgur.com/J8LB4Pt.jpg)


## Known problems

Currently the code is written assuming that the aspect ratio of your image is greater than the aspect ratio of your monitor setup, i.e. there will be some amount of unused image on the right. If there is not it will probably fail. Just crop the image then run the script.
