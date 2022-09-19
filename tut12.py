s = set()
# print(type(s))
# l = [2, 5, 6, 7, 3]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))
s.add(1)
s.add(2)

# s.union({1, 2, 3})
s1 = s.union({1, 2, 3})
s2 = s.intersection({1, 2, 3})
print(s, s1, s2)
