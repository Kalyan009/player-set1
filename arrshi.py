k,b=map(int,input().split())
d=map(int,input().split())
d=list(d)
res=d[-b:]+d[:-b]
for i in res:
  print(i,end=' ')
