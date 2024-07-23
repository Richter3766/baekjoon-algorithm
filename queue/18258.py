import sys
from collections import deque
def push(x):
    queue.append(x)

def pop():
    if len(queue) == 0:
        return -1
    return queue.popleft()

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return 1
    return 0

def front():
    if len(queue) == 0:
        return -1
    return queue[0]


def back():
    if len(queue) == 0:
        return -1
    return queue[-1]

N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(int(command[1]))
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'back':
        print(back())