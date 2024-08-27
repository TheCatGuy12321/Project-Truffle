from math import sin,cos,radians
from argparse import ArgumentParser
from decimal import *

d = lambda x : Decimal(x)

getcontext().prec=15


parser = ArgumentParser("PfPDA.py", 
description="Gets the Coordinate of point B given the coordinates of point A, distance from A to B, and the angle(in degrees, not radians) of the line relative to the x-axis in the cartesian plane.")
parser.add_argument("posx",help="X coordinate of point A",type=int)
parser.add_argument("posy",help="Y coordinate of point A",type=int)
parser.add_argument("len",help="Length of line AB",type=int)
parser.add_argument("ang",help="Angle of BAC",type=int)
args = parser.parse_args()
posx=d(args.posx)
posy=d(args.posy)
_len=d(args.len)
ang=d(args.ang)

# Point B's X = cos(angle)*len+posx
# Point B's Y = sin(angle)*len+posy
outx = d(cos(radians(ang)))*_len+posx
outy = d(sin(radians(ang)))*_len+posy
print("Point B = ({1:.15f}, {1:.15f})".format(outx, outy))