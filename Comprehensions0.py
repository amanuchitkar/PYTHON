# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)
# ______________OR------------------------
ls = [i for i in range(100) if i % 3 == 0]
# print(ls)

book = ['To Kill a Mockingbird by Harper Lee',
        'The Great Gatsby by F Scott Fitzgerald',
        'Things Fall Apart by Chinua Achebe',
        'Moby-Dick by Herman Melville',
        'The Color Purple by Alice Walker',
        'Catch-22 by Joseph Heller',
        'Atlas Shrugged by Ayn Rand',
        'The Lord of the Rings by J.R.R. Tolkien',
        'Harry Potter and the Philosopher Stone by J.K. Rowling',
        'Diary of a Wimpy Kid: Old School by Jeff Kinney',
        'The BFG by Roald Dahl',
        'Harry Potter and the Chamber of Secrets by J.K. Rowling',
        'Harry Potter and the prisoner of Azkaban by J.K. Rowling',
        'Diary of a Wimpy Kid: Double Down by Jeff Kinney',
        'Awful Auntie by David Walliams',
        'Diary of a Wimpy Kid: by Hard Luck Jeff Kinney',
        'Wonder by R.J. Palacio',
        'James and the Giant Peach by Roald Dahl',
        'Ratburger by David Walliams',
        'Matilda by Roald Dahl']
# lis = [f"item{i}:{i}" for i in range(10)]
# lis = [f"{book[i]}:{i}" for i in range(20)]
# lis = [f"{book[i]}:{20-i}" for i in range(20)]
# lis = {f"{book[i]} : {book[19 - i]}" for i in range(20)}
lis = {i: f"item{i}" for i in range(10)}
lis = {value: key for key, value in lis.items()}

# print(lis)
dresses = {Dress for Dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
# dresses=[Dress for Dress in ["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2"]]
print(dresses)
print(type(dresses))
event = (i for i in range(10))
print(event.__next__())
print(event.__next__())
print(event.__next__())
print(event.__next__())
print(event.__next__())
for i in event:
        print(i)
