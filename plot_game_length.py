import numpy as np
import matplotlib.pyplot as plt

from load_file import load_file

def get_game_lengths(n):
    output = []
    data = load_file(n)
    for game in data:
        turns = game["a"] + game["b"] + game["t"]
        output.append(turns)
    return output

def plot_game_length():
    arr = []
    for n in range(1000):
        arr += get_game_lengths(n)
    plt.hist(arr,bins=300)
    print("mean",np.mean(arr))
    std = np.std(arr)
    print("std",std)
    se = std / (999999*0.5)
    print("se",se)
    plt.show()

plot_game_length()