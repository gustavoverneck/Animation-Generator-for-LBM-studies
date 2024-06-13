# /src/run.py

import os
from src.setup import readInput, getArguments
from src.plotting import createAni

args = getArguments()   # get arguments from parser
data = readInput(input_filename=args.input, dim=args.dim, type=args.type, xsup=args.xsup, ysup=args.ysup)  # read input file

createAni(data, args)
