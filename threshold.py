import numpy as np
import matplotlib.pyplot as plt

from load_file import load_file

def count_wins(n,counts,wins):
    data = load_file(n)
    for game in data:
        turns = game["a"] + game["b"]
        for player in [["a","A"],["b","B"]]:
            ratio = game[player[0]] / turns
            rate = int(round(ratio * 100.0))
            if game["W"] == player[1]:
                counts[rate] += 1
                wins[rate] += 1
            else:
                counts[rate] += 1

def threshold():
    counts = [0] * 101
    wins = [0] * 101
    for n in range(1000):
        count_wins(n,counts,wins)
    x_data = []
    y_data = []
    for i in range(101):
        if counts[i] == 0:
            continue
        else:
            x_data.append(i)
            y_data.append(wins[i]/counts[i])
    plt.plot(x_data,y_data)
    plt.show()

threshold()