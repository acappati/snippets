#! /usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def do_plot(df: pd.DataFrame, coord: str) -> None:
    """
    Function that takes the dataframe and the coordinate
    and produces scatter plot with the coordinate, 
    the energy and the intensity (xsec)
    """
    
    # check if coordinate chosen is correct
    if ((coord != "h") and (coord != "k") and (coord != "l")):
        print("ERROR: wrong coordinate chosen!")
        print(coord)
       
    x = df[coord]
    y = df["Energy"]
    z = df["Intensity"]


    # do plot
    plt.rcParams.update({'font.size': 18})

    fig, ax = plt.subplots(1, 1, figsize=(14, 9), dpi=300, tight_layout=True)
    
    plot = ax.scatter(x, y, c=z, cmap="turbo")
    ax.set_xlabel(coord+" 0 0")
    ax.set_ylabel("Energy (MeV)")
    plt.colorbar(plot, label = "Intensity", 
                 orientation = "vertical")
    plt.savefig("test.png")
    plt.close(fig)
