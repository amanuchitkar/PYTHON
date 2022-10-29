import json

data = '{"var1":"aman","var2":56}'
print(data)

parsed = json.loads(data)
print(parsed)
print(parsed["var2"])

Data = {
    "class": 12,
    "Channal": "Aman uchitkar",
    "isbad": False,
    "car": ["lamborgini", "farray", "bugati"],
    "frigh": ("roti", 89)
}
l = json.dumps(Data)
print(l)
