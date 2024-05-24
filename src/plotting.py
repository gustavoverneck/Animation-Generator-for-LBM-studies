# /src/plotting


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animate_2D(i, data, args):
    nt = args.nt
    print(f"{i/nt*100:.2f} %")
    plt.clf()
    x = np.array(data[i][0])
    y = np.array(data[i][1])
    T = np.array(data[i][2])
    plt.scatter(x, y, c=T, cmap='jet')
    plt.colorbar()
    return

def animate_1D(i, data, args):
    nt = args.nt
    print(f"{i/nt*100:.2f} %")
    plt.clf()
    x = np.array(data[0][0])
    T = np.array(data[0][1])
    #extent = [x[0]-2*0.05, x[-1]+2*0.05,0,1]
    plt.plot(x, T, c="black")
    #plt.imshow(T[np.newaxis, :],  cmap="winter", aspect="auto")#, extent=extent)
    plt.title(args.title)
    #plt.xlim(extent[0], extent[1])
    plt.yticks([])
    #plt.colorbar()
    return

def init_2D(data, args):
    plt.scatter([], [], c=[], cmap='jet')
    x = np.array(data[0][0])
    y = np.array(data[0][1])
    T = np.array(data[0][2])
    plt.scatter(x, y, c=T, cmap='jet')
    plt.colorbar()
    return args

def init_1D(data, args):
    x = np.array(data[0][0])
    T = np.array(data[0][1])
    #extent = [x[0]-2*0.05, x[-1]+2*0.05,0,1]
    plt.plot(x, T, c="black")
    #plt.imshow(T[np.newaxis, :],  cmap="winter", aspect="auto")#, extent=extent)
    plt.title(args.title)
    #plt.xlim(extent[0], extent[1])
    plt.yticks([])
    #plt.colorbar()
    return args

def saveAni(anim, args):
    output = args.output
    anim.save(f"output/{output}",  
          writer = 'ffmpeg', fps = 30)
    print(f"Animation saved in /output/{output}!")
    return

def createAni(data, args):
    fig = plt.figure()
    # For dimension=2
    if args.dim == 2:
        init_2D(data, args)
        anim = FuncAnimation(fig, animate_2D, fargs=(data, args), frames=args.nt, interval=20)
        saveAni(anim, args)
    # For dimension=1
    else:
        init_1D(data, args)
        anim = FuncAnimation(fig, animate_1D, fargs=(data, args), frames=args.nt, interval=20)
        saveAni(anim, args)
    
    return

    