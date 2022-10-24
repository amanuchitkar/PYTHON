# tut #77

def searcher():
    import time
    time.sleep(3)
    # booklist = ['To Kill a Mockingbird by Harper Lee',
    #             'The Great Gatsby by F Scott Fitzgerald',
    #             'Things Fall Apart by Chinua Achebe',
    #             'Moby-Dick by Herman Melville',
    #             'The Color Purple by Alice Walker',
    #             'Catch-22 by Joseph Heller',
    #             'Atlas Shrugged by Ayn Rand',
    #             'The Lord of the Rings by J.R.R. Tolkien',
    #             'Harry Potter and the Philosopher Stone by J.K. Rowling',
    #             'Diary of a Wimpy Kid: Old School by Jeff Kinney',
    #             'The BFG by Roald Dahl',
    #             'Harry Potter and the Chamber of Secrets by J.K. Rowling',
    #             'Harry Potter and the prisoner of Azkaban by J.K. Rowling',
    #             'Diary of a Wimpy Kid: Double Down by Jeff Kinney',
    #             'Awful Auntie by David Walliams',
    #             'Diary of a Wimpy Kid: by Hard Luck Jeff Kinney',
    #             'Wonder by R.J. Palacio',
    #             'James and the Giant Peach by Roald Dahl',
    #             'Ratburger by David Walliams',
    #             'Matilda by Roald Dahl']
    with open("aman.txt", "r") as f:
        booklist = f.read()
    while True:
        text = (yield)
        if text in booklist:
            print("Your text found in book list")
        else:
            print("Not found youer text")


# search = searcher()
# next(search)
# search.send("The")
# input(":")
# search.send("The BFG by Roald Dahl")
# search.send("Philosopher")
# search.send("aman")
# search.send("Moby-Dick by Herman Melville")
# search.send("Harry Potter and the Chamber of Secrets by J.K. Rowling")
# search.close()

s=searcher()
next(s)
i=input("search any thing: ")
s.send(i)