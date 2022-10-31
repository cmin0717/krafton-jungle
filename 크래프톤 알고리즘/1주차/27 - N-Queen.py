n = int(input())

pan = [0]*n

count = 0

def queen(x):
    global count
    if x == n:
        count += 1
        return
    else:
        for i in range(n):
            pan[x] = i # x행,i열에 퀸
            if x == 0:
                queen(x+1)
            else:
                for j in range(x): # 앞서 놓은 퀸만 보면 되므로 퀸의 개수만큼만 for문을 돌려준다.
                    if pan[x] == pan[j] or abs(pan[x]-pan[j]) == abs(x-j): # 앞서 있던 퀸들에 걸리나 안걸리나 체크!
                        break
                else:
                    queen(x+1) # 안걸리면 다음 퀸
queen(0)
print(count)

# n = int(input())

# pan = [0]*n

# def check(x):
#     for i in range(x):
#         if pan[x] == pan[i] or abs(pan[x]-pan[i]) == abs(x-i):
#             return False
#     else:
#         return True
# count = 0
# def queen(m):
#     global count
#     if m == n:
#         count += 1
#         return
#     else:
#         for i in range(n):
#             pan[m] = i
#             if check(m):
#                 queen(m+1)
#         return

# queen(0)
# print(count)