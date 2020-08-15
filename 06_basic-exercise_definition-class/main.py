# coding: utf-8

import random
import rhinoscriptsyntax as rs
from box import Box

# variable
num_x = 10
num_y = 10
box_spacing_distance = 1000

rs.EnableRedraw(False)

for x in range(num_x):
    for y in range(num_y):
        origin = [x * box_spacing_distance, y * box_spacing_distance, 0]
        width = random.randint(100, box_spacing_distance - 100)
        depth = random.randint(100, box_spacing_distance - 100)
        height = random.randint(100, box_spacing_distance - 100)

        box = Box(origin, width, depth, height)
        box.draw_box()
        box.draw_box_info()

rs.EnableRedraw(True)
