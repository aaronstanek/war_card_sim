# output format
# each file has an array of 1000 games of war
# Each game has the following information
# A's initial cards array starting at 2
# B's initial cards
# The winner of the game
# How many times A placed a better card than B (a)
# How many times B placed a better card then A (b)
# How many times they tied (t)

import os
import json
import random

def get_file_total():
    try:
        f = os.listdir("data")
    except:
        raise Exception("data directory not present")
    f = len(f)
    return f

def save_to_file(data,file_count):
    s = json.dumps(data,separators=(',', ':'))
    with open("data/"+str(file_count)+".json","w") as file:
        file.write(s)

def gen_start():
    output = []
    for i in range(2,15):
        # J = 11, Q = 12, K = 13, A = 14
        for j in range(4):
            output.append(i)
    return output

def count_cards(arr):
    output = [0] * 13
    for i in range(len(arr)):
        n = arr[i] - 2
        output[n] += 1
    return output

def mini_turn(data,output,place):
    if len(data["A_hand"]) == 0:
        if len(data["A_pool"]) == 0:
            output["W"] = "B"
            return
        else:
            data["A_hand"] = data["A_pool"]
            data["A_pool"] = []
            random.shuffle(data["A_hand"])
    if len(data["B_hand"]) == 0:
        if len(data["B_pool"]) == 0:
            output["W"] = "A"
            return
        else:
            data["B_hand"] = data["B_pool"]
            data["B_pool"] = []
            random.shuffle(data["B_hand"])
    data["hold"].append(data["A_hand"].pop())
    data["hold"].append(data["B_hand"].pop())
    if place:
        if data["hold"][-2] == data["hold"][-1]:
            output["t"] += 1
            for i in range(3):
                mini_turn(data,output,False)
            mini_turn(data,output,True)
        else:
            if data["hold"][-2] > data["hold"][-1]:
                data["A_pool"] += data["hold"]
                output["a"] += 1
            else:
                data["B_pool"] += data["hold"]
                output["b"] += 1
            data["hold"] = []

def play_game():
    output = dict()
    deck = gen_start()
    random.shuffle(deck)
    data = dict()
    data["A_hand"] = deck[0::2]
    data["B_hand"] = deck[1::2]
    data["A_pool"] = []
    data["B_pool"] = []
    data["hold"] = []
    output["A"] = count_cards(data["A_hand"])
    output["B"] = count_cards(data["B_hand"])
    output["W"] = "D"
    output["a"] = 0
    output["b"] = 0
    output["t"] = 0
    for turns in range(1000000):
        mini_turn(data,output,True)
        if output["W"] != "D":
            return output
    return output

def main():
    file_count = get_file_total()
    print(file_count,"files")
    while file_count < 1000:
        k = []
        while len(k) < 1000:
            k.append(play_game())
        save_to_file(k,file_count)
        del(k)
        file_count += 1

main()
