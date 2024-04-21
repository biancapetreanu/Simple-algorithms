 m = input()
10
v = []
for i in range(1,m):
     for j in range(m,m-i,-1):
             v.append(i)
     print(v)