#!/bin/env python3

def main():
    rules = []
    with open("rules.txt", "r") as file:
        rules = file.readlines()

    updates = []
    with open("updates.txt", "r") as file:
        updates = file.readlines()

    ruleset = parse_rules(rules)

    total = 0
    for update in updates:
        update_parsed = list(map(int, update.split(",")))
        if not is_valid(update_parsed, ruleset):
            update_sorted = bubbleSort(update_parsed, ruleset)
            num = update_parsed[len(update_sorted)//2]
            total += num

    print(total)


def bubbleSort(arr, ruleset):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if cmp(arr[j], arr[j+1], ruleset):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

    return arr


def cmp(a, b, ruleset):
    try:
        return a in ruleset[b]
    except:
        return False


def is_valid(update, ruleset):
    for i, page in enumerate(update):
        #print(f"update: {update}, page: {page}, i: {i}")
        for past in update[:i]:
            try:
                #print(f"update: {update}, past: {past}, page: {page}, update[:i]: {update[:i]}")
                if past in ruleset[page]:
                    return False
            except:
                print("No rules for this number")

    return True


def parse_rules(raw_set):
    in_set = map(lambda x: x.split("|") , raw_set)
    in_set = [list(map(int, elem)) for elem in in_set]

    ruleset = {}
    for raw in in_set:
        ruleset[raw[0]] = []

    for raw in in_set:
        ruleset[raw[0]].append(raw[1])

    return ruleset


if __name__ == "__main__":
    main()
