a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
r,c=len(a),len(a[0])

t,l,b,rg=0,0,r-1,c-1
while t<=b and l<=rg:
    for i in range(l,rg+1):
        print(a[t][i],end=' ')
    t+=1
    for i in range(t,b+1):
        print(a[i][rg],end=' ')
    rg-=1

    if t<=b:
        for i in range(rg,l-1,-1):
            print(a[b][i],end=' ')
        b-=1
    if(l<=rg):
        for i in range(b,t-1,-1):
            print(a[i][l],end=' ')
        l+=1