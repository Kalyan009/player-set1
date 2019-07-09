a=int(input())
sum=0
while a>0:
  rem=a%10
  sum=sum+(rem**2)
  a //= 10
print(sum)
