#!/usr/bin/env bash
import subprocess, PIL.Image, sys, os
tmp = subprocess.check_output(["mktemp", "-d", "/tmp/wide.XXXXXX"]).decode("utf-8").strip()
res = []
for line in subprocess.check_output(["xrandr","-q"]).decode("utf-8").split("\n"):
    if " connected" in line:
        l = line.split()
        if l[2] == "primary":
            res.append(l[3])
        else:
            res.append(l[2])
# Debug
# res = ["1440x900+0+0", "1366x768+1400+376", "1440x900+2806+0"]
res = [x.replace("+","x").split("x") for x in res]
res = [[int(x) for x in f] for f in res]
res.sort(key = lambda x: x[2]) # order monitors from left to right by sorting them by left offset
image = PIL.Image.open(sys.argv[1])
total_screen_width = max(x[0] + x[2] for x in res)
total_screen_height = max(x[1] + x[3] for x in res)
ires = []
for r in res:
    height_percentage = float(r[1])/total_screen_height
    height = round(height_percentage * image.size[1])
    width = round(height * (float(r[0])/r[1]))
    top_offset_percent = float(r[3]) / total_screen_height
    top_offset = round(top_offset_percent * image.size[1])
    left_offset = sum(x[0] for x in ires)
    ires.append([width, height, left_offset, top_offset])
x = 0
left_offset = 0
if len(sys.argv) > 2:
    try:
        left_offset = int(sys.argv[2])
    except:
        left_offset = round(0.5 * (image.size[0] - (ires[-1][0] + ires[-1][2])))
for h in ires:
    print(h)
    #left upper right lower
    subimage = image.crop((h[2] + left_offset, h[3], h[2]+h[0] + left_offset, h[3]+h[1]))
    subimage.save(tmp + "/" + str(x) + ".png")
    print(subimage.size)
    x += 1
for x in range(len(ires)):
    subprocess.call(["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor"+str(x)+"/workspace0/last-image", "-s", tmp + "/" + str(x) + ".png"])
