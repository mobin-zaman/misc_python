
def fc(x,n,*ara):
    print ara
    ara=f(x,n,*ara)
    print ara

def f(x,n,*ara):
    print 'in f'
    # if(x==n):
    #     print 'came into ultimate if'
    #     print 'if ',x
    #     return None

    y=x+1
    print y
     
    if(x<(n-1)): 
        print 'came into nested if'
        ara[y],ara[x]=ara[x],ara[y]
        f(x+1,n,*ara)
    else:
        return ara

n=int(input())
ara=list()
for i in range(1,n+1):
    ara.append(i) 

fc(1,n,ara)
