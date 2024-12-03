#!/bin/env python3
import re

def scan_for_mul(mem):
    total = 0
    mul_instructions = re.findall(mul_instruction, mem)
    for ins in mul_instructions:
        ins = ins[4:-1].split(",")
        total += int(ins[0]) * int(ins[1])
    return total


mul_instruction = r"mul\([0-9]+,[0-9]+\)"
total = 0

memory = ""
with open("data.txt", "r") as file:
    memory = "-".join(file.readlines())

is_do = True
while memory != "":
    if is_do:
        is_do = False
        try:
            end = memory.index("don't()")
            total += scan_for_mul(memory[:end + 1])
            print(f"In do block, and dont is found at index {end}, searching in memory {memory[:end + 1]}")
            memory = memory[end + 2:]
        except:
            print(f"In do block, and dont isn't found, searching in memory {memory}")
            total += scan_for_mul(memory)
            memory = ""
    else:
        try:
            start = memory.index("do()")
            print(f"In dont block, and do is found at index {start}")
            memory = memory[start + 2:]
            is_do = True
        except:
            print("There is no further do")
            memory = ""
print(total)
