n=int(input())
num=list(map(int,input().split()))
s=0
for i in num:
    s=s+i
n1=s/n
print(f"{n1:.2f}")