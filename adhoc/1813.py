import sys
from collections import Counter

N = int(sys.stdin.readline())
statements = sys.stdin.readline().split()
counter = Counter(statements)

result = 0
for key in counter.keys():
    nkey = int(key)
    if counter.get(key) == nkey and nkey > result:
        result = nkey
if result == 0 and '0' in counter.keys():
    result = -1

print(result)