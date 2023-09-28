T=int(input())
G=[]
C=[]
for i in range(0,T):
    g,c=input().split()
    G.append(int(g))
    C.append(int(c))
for i in range(0,T):
    H=(C[i])**2/(2*G[i])
    print(int(H))
