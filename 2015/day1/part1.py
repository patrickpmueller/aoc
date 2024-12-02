#!/bin/env python3

floor = 0
with open("data.txt", "r") as file:
    string = file.readline()
    for char in string:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

print(floor)
