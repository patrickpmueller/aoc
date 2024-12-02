#!/bin/env python3

def main():
    safe_reports = 0
    to_dampen = []
    data = []

    with open("data.txt", "r") as file:
        for report in file.readlines():
            levels = map(lambda x: int(x.strip()), report.split(" "))
            levels = list(levels)
            data.append(levels)

    for levels in data:
        if is_safe(levels):
            print("Report is safe\n")
            safe_reports += 1
            continue
        else:
            print("Report not safe, adding to dampening list\n")
            to_dampen.append(levels)
            continue

    for report in to_dampen:
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1:]
            print(f"Removing level {i + 1} from report {report}, it is now {new_report}")
            if is_safe(new_report):
                print("Report is safe after dampening\n")
                safe_reports += 1
                break
            else:
                print("Dampening unsuccessful, trying again\n")


    print(safe_reports)


def pairs(l):
    prev = l[0]

    ret = []
    for elem in l[1:]:
        ret.append((prev, elem))
        prev = elem

    return ret


def is_safe(levels):
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
            return safe

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

        return safe

if __name__ == "__main__":
    main()
