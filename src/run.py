# /src/run.py

import os
from src.setup import readInput, getArguments
from src.plotting import createAni


# é preciso diferenciar 1d, 2d e 3d
args = getArguments()   # get arguments from parser
data = readInput(input_filename=args.input, dim=args.dim, xsup=args.xsup, ysup=args.ysup)  # read input file
createAni(data, args)