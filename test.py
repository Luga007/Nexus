nums = [2,1,3,5,6]
multiple = 2
k = 5


# while k > 0:
#     min_num = nums[0]
#     for i in nums:
#         if min_num > i:
#             min_num = i
#     indexs = nums.index(min_num)
#     nums.remove(min_num)
#     res = min_num * multiple
#     nums.insert(indexs, res)
#     k -= 1
# print(nums)
# res = 5
# lisy = []
# while res > 0:
#     num_min = nums[0]
#     for i in nums:
#         if num_min > i:
#             num_min = i
#     nums.remove(num_min)
#     lisy.append(num_min)
#     res -= 1
#
# print(lisy)


######
# words = ["ааа","аа","ааа"]
# words.sort()
# print(words)
# first, last = words[0], words[-1]
# prefix = ''
# for i in range(min(len(first), len(last))):
#     if first[i] == last[i]:
#         prefix += first[i]
#     else:
#         break
# print(prefix)


# a = 'add'
# e = 'egg'
# a1 = set(a)
# e1 = set(e)
# if len(a1) == len(e1):
#     print(True)

# def length_of_longest_substring(s):
#     char_set = set()  # Храним уникальные символы текущей подстроки
#     left = 0  # Левый указатель окна
#     max_length = 0  # Максимальная длина найденной подстроки
#
#     for right in range(len(s)):  # Двигаем правый указатель
#         while s[right] in char_set:  # Если символ повторяется, сдвигаем левый указатель
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])  # Добавляем новый символ
#         max_length = max(max_length, right - left + 1)  # Обновляем макс. длину
#
#     return max_length
#
# print(length_of_longest_substring("pwwkew"))  # Выведет: 3



