a=input().split()
b=input().split()
for i in range(len(a)):
    for j in range(len(b)):
        if int(a[i])==int(b[j]):
             print(a[i])