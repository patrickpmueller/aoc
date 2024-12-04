#!/bin/env python3
import re

def main():
    word_search = []
    xmases = 0

    with open("data.txt", "r") as file:
        word_search = list(map(lambda x: x.strip(), file.readlines()))

    # Rows
    for row in word_search:
        xmases += check_xmas(row)
    print(xmases)

    # Columns
    word_search_columns = row_to_columns(word_search)
    for column in word_search_columns:
        xmases += check_xmas(column)
    print(xmases)

    # Diag
    word_search_diag = grid_to_diag(word_search)
    for diag in word_search_diag:
        xmases += check_xmas(diag)

    print(xmases)


def grid_to_diag(grid):
    diag = []

    # Get bottom left element at index 0,0
    grid = list(reversed(grid))
    len_x = len(grid[0])
    len_y = len(grid)

    # (0;0) and its diagonal
    diag_00 = ""
    for i in range(min(len_x, len_y)):
        diag_00 += grid[i][i]
    diag.append(diag_00)
    print(diag)

    # (x;0) and its diagonals
    for i in range(1, len_x - 3):
        this_diag = ""
        for y in range(0, min(len_x - i, len_y)):
            x = i + y
            this_diag += grid[y][x]
            print(f"i: {i}, x: {x}, y: {y}, this_diag: {this_diag}")
        diag.append(this_diag)
    print(diag)

    # (0;y) and its diagonals
    for i in range(1, len_y - 3):
        this_diag = ""
        for x in range(0, min(len_x, len_y - i)):
            y = x + i
            this_diag += grid[y][x]
            print(f"i: {i}, x: {x}, y: {y}, this_diag: {this_diag}")
        diag.append(this_diag)
    print(diag)

    # (x;-y) diagonals that cross x axis
    for i in range(3, len_x):
        this_diag = ""
        for y in range(0, min(i + 1, len_y)):
            x = i - y
            this_diag += grid[y][x]
            print(f"i: {i}, x: {x}, y: {y}, this_diag: {this_diag}")
        diag.append(this_diag)
    print(diag)

    for i in range(1, len_y - 3):
        this_diag = ""
        for y in range(i, min(len_x, len_y)):
            x = len_x - y + i - 1
            this_diag += grid[y][x]
            print(f"i: {i}, x: {x}, y: {y}, this_diag: {this_diag}")
        diag.append(this_diag)

    print(diag)
    return diag


def row_to_columns(rows):
    columns = ["" for _ in range(len(rows[0]))]
    for row in rows:
        for columni, column in enumerate(row):
            columns[columni] += column

    return columns



def check_xmas(row):
    xmases = 0
    xmases += len(re.findall(r"XMAS", row))
    xmases += len(re.findall(r"SAMX", row))
    return xmases


if __name__ == "__main__":
    main()
