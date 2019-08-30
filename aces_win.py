import numpy as np
import matplotlib.pyplot as plt

from load_file import load_file

def count_face_cards(n,output_w,output_a):
    data = load_file(n)
    for game in data:
        if game["W"] == "A":
            g = game["A"]
        else:
            g = game["B"]
        g = g[-1]
        output_w.append(g)
        g = game["A"][-1]
        output_a.append(g)

def plot_face_cards():
    arr_w = []
    arr_a = []
    for n in range(1000):
        count_face_cards(n,arr_w,arr_a)
    for arr in [arr_w,arr_a]:
        print("mean",np.mean(arr))
        std = np.std(arr)
        print("std",std)
        se = std / (999999*0.5)
        print("se",se)
        x_data = []
        y_data = []
        for i in range(0,5):
            x_data.append(i)
            t = 0
            for a in arr:
                if a == i:
                    t += 1
            y_data.append(t)
        plt.plot(x_data,y_data)
    plt.show()

plot_face_cards()