age1=60
age2=76
age3=12

youngest=oldest=age1
if age2<youngest:
    youngest=age2
if age2>oldest:
    oldest=age2
if age3<youngest:
    youngest=age3
if age3>oldest:
    oldest=age3

# youngest=min(age1,age2,age3)
# oldest=max(age1,age2,age3)

print(youngest,oldest)