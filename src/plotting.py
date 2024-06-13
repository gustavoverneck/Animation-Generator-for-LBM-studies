# /src/plotting


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm import tqdm
import numpy as np
import os
import subprocess
import sys

def open_directory_in_file_explorer(path):
    if not os.path.isdir(path):
        raise ValueError(f"The path '{path}' is not a valid directory.")
    
    if os.name == 'nt':  # Windows
        os.startfile(path)
    elif os.name == 'posix':
        if sys.platform == 'darwin':  # macOS
            subprocess.run(['open', path])
        else:  # Linux
            subprocess.run(['xdg-open', path])
    else:
        raise OSError(f"It was not possible to open output directory in {os.name}.")

def animate_2D(i, data, args, progress_bar):
    nt = args.nt
#    print(f"{i/nt*100:.2f} %")
    plt.clf()
    x = np.array(data[i][0])
    y = np.array(data[i][1])
    T = np.array(data[i][2])
    plt.scatter(x, y, c=T, cmap='jet')
    plt.title(args.title)
    plt.colorbar()
    progress_bar.update(1)
    return

def animate_1D(i, data, args, progress_bar):
    nt = args.nt
    #print(f"{i/nt*100:.2f} %")
    plt.clf()
    x = np.array(data[i][0])
    T = np.array(data[i][1])
    #extent = [x[0]-2*0.05, x[-1]+2*0.05,0,1]
    plt.plot(x, T, c="black")
    #plt.imshow(T[np.newaxis, :],  cmap="winter", aspect="auto")#, extent=extent)
    plt.title(args.title)
    #plt.xlim(extent[0], extent[1])
    plt.yticks([])
    progress_bar.update(1)
    #plt.colorbar()
    return

def animate_vector2D(i, data, args, progress_bar):
    nt = args.nt
    plt.clf()
    x = np.array(data[i][0])
    y = np.array(data[i][1])
    T = np.array(data[i][2])
    vx = np.array(data[i][3])
    vy = np.array(data[i][4])
    plt.scatter(x, y, c=T, cmap='rainbow')
    plt.colorbar()
    plt.quiver(x, y, vx, vy, angles='xy', scale_units='xy', scale=0.1)
    plt.title(args.title)
    plt.gca().set_aspect('equal')
    progress_bar.update(1)
    return

def init_2D(data, args):
    plt.scatter([], [], c=[], cmap='jet')
    x = np.array(data[0][0])
    y = np.array(data[0][1])
    T = np.array(data[0][2])
    plt.scatter(x, y, c=T, cmap='jet')
    plt.title(args.title)
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
    # Create progress bar
    return args

def init_vector2D(data, args):
    x = np.array(data[0][0])
    y = np.array(data[0][1])
    vx = np.array(data[0][2])
    vy = np.array(data[0][3])
    T = np.array(data[0][4])
    plt.scatter(x, y, c=T, cmap='rainbow')
    plt.colorbar()
    plt.quiver(x, y, vx, vy, angles='xy', scale_units='xy', scale=0.1)
    plt.title(args.title)
    return args

def saveAni(anim, args):
    output = args.output
    anim.save(f"output/{output}",  
          writer = 'ffmpeg', fps = 30)
    print(f"Animation saved in /output/{output}!")
    # Open folder
    open_directory_in_file_explorer(f"output")
    
    
    return

def createAni(data, args):
    fig = plt.figure()
    n_frames = args.nt
    progress_bar = tqdm(total=n_frames, desc='Animating')
    if args.type == 'heatmap':
        # For dimension=2
        if args.dim == 2:
            init_2D(data, args)
            anim = FuncAnimation(fig, animate_2D, fargs=(data, args, progress_bar), frames=args.nt, interval=20)
            saveAni(anim, args)
        # For dimension=1
        else:
            init_1D(data, args)
            anim = FuncAnimation(fig, animate_1D, fargs=(data, args, progress_bar), frames=args.nt, interval=20)
            saveAni(anim, args)
        progress_bar.close()
    elif args.type == 'vectorfield':
        # For dimension=2
        if args.dim == 2:
            init_vector2D(data, args)
            anim = FuncAnimation(fig, animate_vector2D, fargs=(data, args, progress_bar), frames=args.nt, interval=0.01)
            saveAni(anim, args)
        progress_bar.close()
    return
