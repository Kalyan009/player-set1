a=int(input())
temp=0
while i>0:
  rem=a%10
  temp=temp*10+rem
  i=i//10
print(temp)
