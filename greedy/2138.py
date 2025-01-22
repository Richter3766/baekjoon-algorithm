import sys
import copy

def click_switch(bulbs, idx):
    if idx == 0:
        bulbs[idx], bulbs[idx + 1] = abs(bulbs[idx] - 1), abs(bulbs[idx + 1] - 1)
    elif idx == number - 1:
        bulbs[idx], bulbs[idx - 1] = abs(bulbs[idx] - 1), abs(bulbs[idx - 1] - 1)
    else:
        bulbs[idx - 1], bulbs[idx], bulbs[idx + 1] = abs(bulbs[idx - 1] - 1), abs(bulbs[idx] - 1), abs(bulbs[idx + 1] - 1)
    return bulbs


def find_count(bulbs):
    count = 0
    for idx in range(1, number):
        if bulbs[idx - 1] != target_bulbs[idx - 1]:
            count += 1
            bulbs = click_switch(bulbs, idx)

    if target_bulbs != bulbs:
        return -1
    return count


number = int(sys.stdin.readline())
bulbs = list(map(int, list(sys.stdin.readline().strip())))
target_bulbs = list(map(int, list(sys.stdin.readline().strip())))

if bulbs == target_bulbs:
    print(0)
else:
    count = find_count(copy.deepcopy(bulbs))
    if count != -1:
        print(count)
    else:
        bulbs = click_switch(bulbs, 0)
        count = find_count(copy.deepcopy(bulbs))
        print(count + 1 if count != -1 else -1)