# list1 = [["aman", 1], ["mrudul", 2], ["ashutosh", 3], ["pranav", 4],
#          ["nayan", 5], ["abhishek", 6]]
# dict1 = dict(list1)
# for item in dict1:
#     print(item)
# for item, rank in dict1.items():
#     print(item, "rank is", rank)
# ---------------------------------------------

items = [int, float, 2, "hi", 8, 5, 9, 7, 56, 80, 70, "yes"]

for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)
