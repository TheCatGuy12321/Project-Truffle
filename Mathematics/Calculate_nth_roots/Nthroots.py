from math import sin,cos,radians
from argparse import ArgumentParser
from decimal import *
from gmpy2 import root
import csv
import time

d = lambda x : Decimal(x)

answers = []

getcontext().prec=10
parser = ArgumentParser("Nthroots.py", 
description="Calculate Nth roots of a")
parser.add_argument("a",help="The number",type=Decimal)
parser.add_argument("n",help="Nth root",type=int)
parser.add_argument("-o", "--output-csv", help="Output a csv file containing answers?", action="store_true")
args = parser.parse_args()
a = d(args.a)
n = int(args.n)
output_csv = args.output_csv

answers.append(d(float(root(float(a), n))).normalize())

angle = d(360/n)

for i in range(1, n):
    real = d(d(cos(radians(angle*i)))*answers[0]).normalize()
    imag = d(d(sin(radians(angle*i)))*answers[0]).normalize()
    if str(imag)[0] == "-":
        answers.append(f"{real:.10f}"+"   -   "+f"{(imag*-1):.10f}"+"*i")
    else:
        answers.append(f"{real:.10f}"+"   +   "+f"{imag:.10f}"+"*i")

if not(output_csv):
    for i in answers:
        print(i, end="\n\n")
else:
    with open(f"Output_{time.time()}.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\n', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(answers)
        f.close()