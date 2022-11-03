from copy import deepcopy
import sys
input = sys.stdin.readline

n= int(input())
city_map = []
city_high = []

for _ in range(n):
    city = list(map(int, input().split()))
    city_map.append(city)
    city_high += set(city)

def check(arr,h):
    save_cnt = 0
    save_arr = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h:
                arr[i][j] = 0
                save_cnt += 1
                save_arr.append([i,j])
            while save_arr:
                x,y = save_arr.pop()
                for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
                    if 0 <= a < n and 0 <= b < n and arr[a][b] > h:
                        arr[a][b] = 0
                        save_arr.append([a,b])
    return save_cnt

max_save = 1
for i in set(city_high):
    cp_map = deepcopy(city_map)
    max_save = max(max_save, check(cp_map,i))
print(max_save)