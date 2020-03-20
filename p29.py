a=int(input('enter the 10 digits number '))
count=0 
maxdigit=0     
while a!=0:
    r=a%10
    if r>maxdigit:
        maxdigit=r
    count+=1
    a=int(a/10)
if count!=10:
    a=int(input('you did not enter the 10 digits number.please enter the 10 digits number '))
print(maxdigit)
