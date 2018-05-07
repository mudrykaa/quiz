#!/usr/bin/python3.6

def next_step(pointer, current, data):
    x = getattr(current[0], current[1])(1), current[1], current[2]
    data[pointer] = x
    return x

def balance(str_in):
    left, right = "", ""
    data = {
        "left" : (0, "__add__", ("(", ")")), 
        "right": (len(str_in) - 1, "__sub__", (")", "("))
    }
    pointer = "left"
    current = data[pointer]
    balance = False
    while data["left"][0] <= data["right"][0]:
        if str_in[current[0]] == current[2][1]:
            current = next_step(pointer, current, data)
        elif str_in[current[0]] == current[2][0]:
            current = next_step(pointer, current, data)
            if pointer == "left":
                balance = True
                pointer = "right"
                current = data[pointer]
            else:
                pointer = "left"
                current = data[pointer]
                if balance:
                    next_step(pointer, current, data)
                    balance = False
                    left += "("
                    right = ")" + right
        else:
            if pointer == "left":
                left += str_in[current[0]]
            else:
                right = str_in[current[0]] + right
            current = next_step(pointer, current, data)
    return left, right

test = "a)b(((cd)efg)h"
left, right = balance(test)
print("Input:    {}\nBalanced: {}".format(test, (left + right)))
