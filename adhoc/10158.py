import sys

width, height = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
nx, ny = 0, 0
checkX = (x + t) // width
checkY = (y + t ) // height

if checkX % 2 == 0:
    nx = (x + t) % width
else:
    nx = width - (x + t) % width
if checkY % 2 == 0:
    ny = (y + t) % height
else:
    ny = height - (y + t) % height

print(nx, ny)

# 오른쪽 벽에 부딪히면?
# 1, 1 -> -1, 1
# 1, -1 -> -1, -1

# 아랫쪽 벽에 부딪히면?
# 1, 1 -> 1, -1
# -1, 1 -> -1, -1

# 윗 벽에 부딪히면?
# 1, -1 -> 1, 1
# -1, -1 -> -1, 1

# 왼쪽 벽에 부딪히면?
# -1, 1 -> 1, 1
# -1 , -1 -> 1, -1

# 왼/오 벽은 x에 -1 곱
# 윗/아래 벽은 y에 -1 곱
# 모서리에 부딪히면 x, y 둘다 -1곱