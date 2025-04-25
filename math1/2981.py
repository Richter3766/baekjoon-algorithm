import sys
from math import gcd

num = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(num)]
result = gcd(*num_list)
print(result)