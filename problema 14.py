X=[]
n=int(input('introdu numarul de linii:'))
if ((n>=2)and(n<=10)):
    print('introdu elementele matricei:')
    for a in range(0,n):
        a=[]
    for b in range(0,n):
        b=int(input())
        a.append(b)
        X.append(a)
    print(X)
    d_principala=[]
    d_secundara=[]
    sus_principala=[]
    jos_principala=[]
    sus_secundara=[]
    jos_secundara=[]
    for i in range(len(X)):
        for j in range(len(X[0])):
            if i==j:
                d_principala.append(X[i][j])
            if(i+j)==(len(X)-1):
                d_secundara.append(X[i][j])
            if i<j:
                sus_principala.append(X[i][j])
            if i>j:
                jos_principala.append(X[i][j])
            if(i+j)<(len(X)-1):
                sus_secundara.append(X[i][j])
            if(i+j)>(len(X)-1):
                jos_secundara.append(X[i][j])
    print('suma elementelor diagonalei principale=',sum(d_principala))
    print('suma elementelor diagonalei secundare=',sum(d_secundara))
    print('suma elementelor mai sus de diagonala principala=',sum(sus_principala))
    print('suma elementelor mai jos de diagonala principala=',sum(jos_principala))
    print('suma elementelor mai sus de diagonala secundara=',sum(sus_secundara))
    print('suma elementelor mai jos de diagonala secundara=',sum(jos_secundara))

    