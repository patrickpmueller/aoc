#!/bin/env python3

def pairs(l):
    prev = l[0]

    ret = []
    for elem in l[1:]:
        ret.append((prev, elem))
        prev = elem

    return ret


safe_reports = 0

with open("data.txt", "r") as file:
    for report in file.readlines():
        levels = map(lambda x: int(x.strip()), report.split(" "))
        levels = list(levels)

        diffs = []
        safe = True
        for level_pair in pairs(levels):
            diff = level_pair[0] - level_pair[1]
            if diff == 0:
                print("Report not save, difference is 0")
                safe = False
                break
            else:
                diffs.append(diff)

        if not safe:
            continue

        max_val = max(diffs)
        min_val = min(diffs)

        if not (max_val / abs(max_val) == min_val / abs(min_val)):
            print("Report not safe due to direction change")
            safe = False
        elif abs(max_val) > 3:
            print("Report not safe due to step size")
            safe = False
        elif abs(min_val) > 3:
            print("Report not safe due to step size")
            safe = False

        if safe:
            print("Report is safe")
            safe_reports += 1
            continue

print(safe_reports)
