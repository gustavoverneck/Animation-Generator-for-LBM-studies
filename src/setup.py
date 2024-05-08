# /src/setup.py


import os
import argparse

def readInput(input_filename, x_sup, y_sup):
    # Read the output file
    data = []
    input_filename
    with open("input/{}".format(input_filename), 'r') as f:
        output = f.readlines()
        l = 0
        data.append([[],[],[]])
        for line in output:
            data[l][0].append(float(line.split()[0]))
            data[l][1].append(float(line.split()[1]))
            data[l][2].append(float(line.split()[2]))
            data.append([[],[],[]])
            if float(line.split()[0])==x_sup and float(line.split()[1])==y_sup:   # x, y, T
                l += 1
    return data


def getArguments():
    # Parase arguments
    parser = argparse.ArgumentParser()
    # Add Arguments
    #parser.add_argument("--model", type=str, help="Plot type (1D or 2D)")
    parser.add_argument("--input", type=str, help="Input file path/name")
    parser.add_argument("--output", type=str, help="Output MP4 file path/name")
    parser.add_argument("--nt", type=int, help="Number of time steps")
    #parser.add_argument("--x_inf", type=int, help="x lower bound")
    parser.add_argument("--x_sup", type=int, help="x upper bound")
    #parser.add_argument("--y_inf", type=int, help="y lower bound")
    parser.add_argument("--y_sup", type=int, help="y upper bound")
    #parser.add_argument("-nx", type=int, help="Number of x steps")
    #parser.add_argument("-ny", type=int, help="Number of y steps")

    # Read Arguments
    args = parser.parse_args()
    return args