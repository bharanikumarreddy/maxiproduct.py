num=int(input())
l=[]
l = list(map(int,input().strip().split()))[:num]
l.sort(reverse=True)
ans=l[0]*l[1]
print(ans)
