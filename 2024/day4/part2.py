#!/bin/env python3
import re

def main():
    word_search = []
    xmases = 0

    with open("data.txt", "r") as file:
        word_search = list(map(lambda x: x.strip(), file.readlines()))

    len_x = len(word_search[0])
    len_y = len(word_search)

    list_of_as = []

    for y, row in enumerate(word_search):
        for x, char in enumerate(row):
            if char == "A" and min(x, y) != 0 and max(x, y) != max(len_x, len_y) - 1:
                top_left = word_search[y - 1][x - 1]
                bottom_right = word_search[y + 1][x + 1]
                top_right = word_search[y - 1][x + 1]
                bottom_left = word_search[y + 1][x - 1]
                print(f"{top_left}A{bottom_right}, {top_right}A{bottom_left}")

                diag1 = top_left + "A" + bottom_right
                diag2 = top_right + "A" + bottom_left
                print(check_mas(diag1) and check_mas(diag2))
                xmases += 1 if check_mas(diag1) and check_mas(diag2) else 0

    print(xmases)


def check_mas(row):
    return re.match(r"MAS", row) != None or re.match(r"SAM", row) != None

if __name__ == "__main__":
    main()
