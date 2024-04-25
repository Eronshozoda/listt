my_list=input().split()
n=int(input())
s=[]
for i in range(1,n+1):
    for j in my_list:
        s.append(f"{j}{i}")
print(s)
        
            
   
