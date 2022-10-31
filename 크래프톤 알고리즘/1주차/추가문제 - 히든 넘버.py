n = int(input())
word = list(input())

check = [str(i) for i in range(10)]

check_num = ''

for i in word:
    if i not in set(check):
        check_num += ' '
    else:
        check_num += i

hidden_nums = list(map(int, check_num.split()))
nums = [i for i in hidden_nums if len(str(i)) < 7]
print(sum(nums))

#
# for i in range(n):
#     if word[i] in check:
#         check_num += word[i]
#         if word[i+1] not in check:
#             hidden_num.append(int(check_num))
#             check_num = ''

# nums = [i for i in hidden_num if len(str(i)) < 7]
# print(sum(nums))

