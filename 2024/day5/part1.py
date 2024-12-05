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
        if is_valid(update_parsed, ruleset):
            num = update_parsed[len(update_parsed)//2]
            total += num

    print(total)


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
