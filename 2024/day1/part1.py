#!/bin/env python3

left_list = []
right_list = []

with open("data.txt", "r") as file:
    for line in file.readlines():
        data = map(lambda x: int(x), line.split("   "))
        data = list(data)
        left_list.append(data[0])
        right_list.append(data[1])

left_list = sorted(left_list)
right_list = sorted(right_list)
total_distance = 0

for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print(total_distance)
