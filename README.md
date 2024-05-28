# Surface-Heat-Map-Animation-Generator
Surface Heat Map Animation Generator using python

The data format is:
x[0]_0 y[0]_0 t[0,0]_0
x[0]_0 y[0]_0 T[0,0]_0
...
x[nx]_0 y[ny]_0 t[0,0]_0
x[nx]_0 y[ny]_0 T[0,0]_0
...
x[0]_1 y[0]_1 t[0,0]_1
x[0]_1 y[0]_1 T[0,0]_1
...
...
x[nx]_nt y[ny]_nt t[nx, ny]_nt'

and it must be located in 'input' directory.

Usage:

Run "python3 app.py [-h] [--input INPUT] [--output OUTPUT] [--nt NT] [--xsup XSUP]
              [--ysup YSUP] [--xlabel XLABEL] [--ylabel YLABEL]
              [--title TITLE] [--dim DIM]"

options:
  -h, --help       show this help message and exit
  --input INPUT    Input file path/name.
  --output OUTPUT  Output MP4 file path/name.
  --nt NT          Number of time steps.
  --xsup XSUP      x upper bound.
  --ysup YSUP      y upper bound.
  --xlabel XLABEL  x label.
  --ylabel YLABEL  y label.
  --title TITLE    Title.
  --dim DIM        Dimension of the problem (1 or 2).
