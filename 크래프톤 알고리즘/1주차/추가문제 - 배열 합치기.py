import sys
input = sys.stdin.readline

n,m = map(int, input().split())
n_li = list(map(int, input().split()))
m_li = list(map(int, input().split()))
# all_li = n_li + m_li

# print(*sorted(all_li))

# sort함수를 안쓴 풀이법. n_li, m_li 각각 배열로 주어져서 각 리스트는 정렬이 되어있다.
all_li = []
a,b = 0,0
while a < n  and b < m:
    if n_li[a] > m_li[b]:
        all_li.append(m_li[b])
        b += 1
    else:
        all_li.append(n_li[a])
        a += 1
while a < n:
    all_li.append(n_li[a])
    a += 1
while b < m:
    all_li.append(m_li[b])
    b += 1

print(*all_li)
