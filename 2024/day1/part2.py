#!/bin/env python3

left_list = []
right_list = []

with open("data.txt", "r") as file:
    for line in file.readlines():
        data = map(lambda x: int(x), line.split("   "))
        data = list(data)
        left_list.append(data[0])
        right_list.append(data[1])

similarity_score = 0

for left_elem in left_list:
    similarity_score += right_list.count(left_elem) * left_elem

print(similarity_score)
