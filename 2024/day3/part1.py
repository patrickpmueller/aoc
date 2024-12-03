#!/bin/env python3
import re

mul_instruction = r"mul\([0-9]+,[0-9]+\)"
total = 0

with open("data.txt", "r") as file:
    memory = "-".join(file.readlines())
    print(memory)
    mul_instructions = re.findall(mul_instruction, memory)
    for ins in mul_instructions:
        ins = ins[4:-1].split(",")
        total += int(ins[0]) * int(ins[1])


print(total)
