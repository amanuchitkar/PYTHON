# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {
    "Mrudul": "chicken",
    "aman": "burger",
    "ashutosh": "RotiSabji",
    "shubham": {"brackfast": "chaii", "lunch": "roti", "diner": "egg"},
}
# print(d2["shubham"]["brackfast"])
# print(d2["shubham"])
# d2["ankit"] = "pizza"
# d2["pranav"] = "pubg"
# del d2["aman"]
# d3 = d2.copy()
# del d3["aman"]
# d2.update({"Kushi": "mobile"})
# print(d2.keys())
print(d2.items())
print(d2)
