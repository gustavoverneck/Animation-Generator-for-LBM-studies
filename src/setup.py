# /src/setup.py


import os
import argparse

def readInput(input_filename, dim, **kwargs):
    # Reads 2D lattice
    if kwargs['type'] == 'heatmap':
        if dim == 2:
            # Read the output file
            xsup = kwargs['xsup']
            ysup = kwargs['ysup']
            data = []
            with open("input/{}".format(input_filename), 'r') as f:
                output = f.readlines()
                l = 0
                data.append([[],[],[]])
                for line in output:
                    data[l][0].append(float(line.split()[0]))
                    data[l][1].append(float(line.split()[1]))
                    data[l][2].append(float(line.split()[2]))
                    data.append([[],[],[]])
                    if float(line.split()[0])==xsup and float(line.split()[1])==ysup:   # x, y, T
                        l += 1
            return data
        
        # Reads 1D lattice
        elif dim == 1:
            # Read the output file
            xsup = kwargs['xsup']
            data = []
            with open("input/{}".format(input_filename), 'r') as f:
                output = f.readlines()
                l = 0
                data.append([[], []])
                for line in output:
                    data[l][0].append(float(line.split()[0]))
                    data[l][1].append(float(line.split()[1]))
                    data.append([[], []])
                    if float(line.split()[0])==xsup:
                        l += 1
            return data
        # If the dimension is invalid, break!
        else:
            raise ValueError("Invalid dimension. Please choose 1 or 2.")
    
    elif kwargs['type'] == 'vectorfield':
        if dim == 2:
            # Read the output file
            xsup = kwargs['xsup']
            ysup = kwargs['ysup']
            data = []
            with open("input/{}".format(input_filename), 'r') as f:
                output = f.readlines()
                l = 0
                data.append([[],[],[],[],[]])   # x y T vx vy
                for line in output:
                    data[l][0].append(float(line.split()[0]))   # x
                    data[l][1].append(float(line.split()[1]))   # y
                    data[l][2].append(float(line.split()[3]))   # T
                    data[l][3].append(float(line.split()[4]))   # vx
                    data[l][4].append(float(line.split()[5]))   # vy
                    data.append([[],[],[],[],[]])
                    if float(line.split()[0])==xsup and float(line.split()[1])==ysup:
                        l += 1
            return data
        elif dim==1:
            raise ValueError("Invalid dimension for vector field. Please choose 2.")
    else:
        raise ValueError("Invalid plot type. Please choose 'heatmap' or 'vectorfield'.")

def getArguments():
    # Parase arguments
    parser = argparse.ArgumentParser()
    # Add Arguments
    parser.add_argument("--input", type=str, help="Input file path/name.", default="input.dat")
    parser.add_argument("--output", type=str, help="Output MP4 file path/name.", default="output.mp4")
    parser.add_argument("--nt", type=int, help="Number of time steps.")
    parser.add_argument("--xsup", type=float, help="x upper bound.")
    parser.add_argument("--ysup", type=float, help="y upper bound.")
    parser.add_argument("--xlabel", type=str, help="x label.", default=" ")
    parser.add_argument("--ylabel", type=str, help="y label.", default=' ')
    parser.add_argument("--title", type=str, help="Title.", default=" ")
    parser.add_argument("--dim", type=int, help="Dimension of the problem (1 or 2).")
    parser.add_argument("--type", type=str, help="Plot type.", default="heatmap")
    # Read Arguments
    args = parser.parse_args()
    return args