n=int(input())
li=[1,1]
for i in range(n):
    if i>1:
        s=li[i-1]+li[i-2]
        li.append(s)
print(li[n-1])