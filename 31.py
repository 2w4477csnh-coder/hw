x,y=map(int,input().split())
r1=x%y
r2=y%x
print(int(r1==0 or r2==0))