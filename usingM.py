import random

# die Throw ex..
randon_num = random.randint(1, 6)
randon_num0 = random.randint(1, 6)
print(randon_num0, randon_num, randon_num0 + randon_num)

randon_num1 = random.random()
randon_num2 = random.random() * 100
randon_num3 = random.randint(1, 100)
# print(randon_num1)
# print(randon_num2)
# print(randon_num3)

channel = ["Arun pawar", "ExproleTheEnseen2.o", "Dinesh sir", "Khan Sir", "Abhiandniyu", "Ashish chanchlani"]
choice = random.choice(channel)
print(choice)
# die = ["1", "2", "3", "4", "5", "6"]
# throw = random.choice(die)
# print(throw)
