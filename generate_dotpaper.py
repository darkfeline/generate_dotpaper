#!/usr/bin/env python3

"""Simple dot paper generator.

    $ python generate_dotpaper.py output.png

Edit the constants in this script to configure.

Requires Python 3 and Pillow.

"""

import sys

from PIL import Image, ImageDraw

def inch2mm(inch):
    return inch * 25.4

def mm2inch(mm):
    return mm / 25.4

def mm2px(dpi, mm):
    dots_per_mm = mm2inch(dpi)  # dots/inch * inch/mm
    return mm * dots_per_mm

def enumerate_points(rect, grad):
    for x in range(grad, rect[0], grad):
        for y in range(grad, rect[1], grad):
            yield (x, y)

def centered_box(pos, rad):
    return (tuple(i - rad for i in pos),
            tuple(i + rad for i in pos))

DPI = 300

A4_MM = (210, 297)
A4_PX = tuple(int(mm2px(DPI, unit)) for unit in A4_MM)

GRAD_MM = 5

RAD_MM = 0.5
RAD_PX = mm2px(DPI, RAD_MM)

COLOR = (150, 150, 150)

# Make image
output = sys.argv[1]
image = Image.new('RGB', A4_PX, (255, 255, 255))
draw = ImageDraw.Draw(image)

# We iterate using mm to avoid loss of precision when converted to pixels
for pos in enumerate_points(A4_MM, GRAD_MM):
    pos = tuple(int(mm2px(DPI, i)) for i in pos)
    draw.ellipse(centered_box(pos, RAD_PX), COLOR)

image.save(output, dpi=(DPI, DPI)) 
