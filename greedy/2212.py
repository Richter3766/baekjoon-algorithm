import sys

sensors_num = int(sys.stdin.readline())
sites_num = int(sys.stdin.readline())
sites_info = sorted(list(map(int, sys.stdin.readline().split())))

difference_site= []
for idx in range(sensors_num - 1):
    difference_site.append(sites_info[idx + 1] - sites_info[idx])

difference_site.sort()
print(sum(difference_site[:sensors_num - sites_num]))
