import sys
import heapq

def find_max_num(num_people, info_people):
    max_num = 1

    info_people.sort()
    i_rank_heap = [info_people[0][1]]
    for i in range(1, num_people):
        if info_people[i][1] < i_rank_heap[0]:
            max_num += 1
        heapq.heappush(i_rank_heap, info_people[i][1])

    return max_num

testcase_num = int(sys.stdin.readline())
result_list = []

for i in range(testcase_num):
    num_people = int(sys.stdin.readline())
    info_people = [list(map(int, sys.stdin.readline().split())) for _ in range(num_people)]

    max_num = find_max_num(num_people, info_people)
    result_list.append(max_num)

for result in result_list:
    print(result)