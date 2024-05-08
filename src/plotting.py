# /src/plotting


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animate(i, data, args):
    nt = args.nt
    print(f"{i/nt*100:.2f} %")
    plt.clf()
    x = np.array(data[i][0])
    y = np.array(data[i][1])
    T = np.array(data[i][2])
    plt.scatter(x, y, c=T, cmap='jet')
    plt.colorbar()
    return

def init(data, args):
    plt.scatter([], [], c=[], cmap='jet')
    x = np.array(data[0][0])
    y = np.array(data[0][1])
    T = np.array(data[0][2])
    plt.scatter(x, y, c=T, cmap='jet')
    plt.colorbar()
    return args

def saveAni(anim, args):
    output = args.output
    anim.save(f"output/{output}",  
          writer = 'ffmpeg', fps = 30)
    print(f"Animation saved in /output/{output}!")
    return

def createAni(data, args):
    fig = plt.figure()
    init(data, args)
    anim = FuncAnimation(fig, animate, fargs=(data, args), frames=args.nt, interval=20)
    saveAni(anim, args)
    return

    