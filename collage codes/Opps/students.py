class Student:
    # def __init__(self,nameis,PNRis,yearis):
    name="aman"
    PRN=2079
    year=1
    def info(self):
        print(f"PNR is {self.PRN},Name is {self.name},in year {self.year}")

std1=Student()
std1.info()
print(std1.__dict__)

pol=Student()
pol.PRN=113
pol.name="Shubham Pol"
pol.year=9
pol.info()

print(pol.__dict__)
# sharma=Student("aman",953,1)
# sharma.info()