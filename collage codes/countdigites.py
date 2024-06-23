input=98765
i1=0
for i in str(input):
    i1+=int(i)
print(i1)

f=input//10000
j=(input//1000)%10
k=(input//100)%10
l=(input//10)%10
e=(input%10)

print(f+j+k+l+e)

input500,input200,input100,input50,input20,input10,input5,input2,input1=0,0,0,0,0,0,0,0,0

if input>=input500:
    note500=input//500
    input%=500
if input>=input200:
    note200=input//200
    input%=200
if input>=input100:
    note100=input//100
    input%=100
if input>=input50:
    note50=input//50
    input%=50
if input>=input20:
    note20=input//20
    input%=20
if input>=input10:
    note10=input//10
    input%=10
if input>=input5:
    note5=input//5
    input%=5
if input>=input2:
    note2=input//2
    input%=2
if input>=input1:
    note1=input//1
    input%=1

notecount={
    500:note500, 200:note200, 100:note100, 50:note50, 20:note20, 10:note10, 5:note5, 2:note2, 1:note1}

for keys,values in notecount.items():
    
    if values>0:
        print(f"For note {keys}:{values}")
# print(notecount)



input=2879
notes=[500,200,100,50,20,10,5,2,1]
countNote={}
for note in notes:
    if input>=note:
        countNote[note]=input//note
        input%=note

print(countNote)
for keys,values in countNote.items():
    
    if values>0:
        # values=sum(int(digite) for digite in str(values))
        print(f"For note {keys}:{values}")