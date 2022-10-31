import sys
input = sys.stdin.readline


n = int(input())
nums = [int(input()) for _ in range(n)]

# 그냥 sort()함수 쓰면됨...
nums.sort()
print(*nums, sep='\n')

# 퀵 정렬(실패 메모리 초과)
# def quick(arr):
#     if len(arr) < 2:
#         return arr

#     mid = arr[0]
#     mid_left = []
#     mid_right = []

#     for i in arr[1:]:
#         if i < mid:
#             mid_left.append(i)
#         else:
#             mid_right.append(i)
#     new_arr = quick(mid_left) + [mid] + quick(mid_right)

#     return new_arr

# print(*quick(nums), sep='\n')




# 버블 정렬(실패함 시간 초과)
# for i in range(n):
#     for j in range(n-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]

# for i in nums:
#     print(i)
