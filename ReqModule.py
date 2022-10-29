# tut 81
import requests

r = requests.get("http://cyber.uchitkargroups.in.net/")
print(r.text)
print(r.status_code)

# url = "http://audio.uchitkargroups.in.net/"
# data = {
#     "p1": 2,
#     "p2": 9
# }
# r2 = requests.post(url=url, data=data)
# print(r2.text)
# print(r2.status_code)
