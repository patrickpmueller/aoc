#!/bin/env python3

floor = 0
with open("data.txt", "r") as file:
    string = file.readline()
    for i, char in enumerate(string):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor < 0:
            print(i + 1)
            break
