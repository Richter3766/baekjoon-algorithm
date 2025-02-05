import sys

def find_good(num_list):
    if len(num_list) == length:
        return int(''.join(num_list))

    for number in range(1, 4):
        num_list.append(str(number))
        if is_good(num_list):
            result = find_good(num_list)
            if result:
                return result
        num_list.pop()


def is_good(num_list):
    for i in range(len(num_list) // 2):
        if num_list[2 * (- i - 1) : - i - 1] == num_list[-i - 1:]:
            return False
    return True

length = int(sys.stdin.readline())

# 1, 2, 3 을 반드시 한 번은 쓰면서 좋은 수열 만들기
# 좋은 수열은 임의의 길이의 인접한 두 개의 부분 수열이 반복되지 않는 수열이다.
num_list = []

result = find_good(num_list)

print(result)