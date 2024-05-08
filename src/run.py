# /src/run.py

import os
from src.setup import readInput, getArguments
from src.plotting import createAni


# é preciso diferenciar 1d, 2d e 3d
args = getArguments()
data = readInput(input_filename=args.input, x_sup=args.x_sup, y_sup=args.y_sup)  
createAni(data, args)