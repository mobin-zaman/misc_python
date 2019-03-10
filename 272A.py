n=int(input())
arr=raw_input()
l=list(map(int,arr.split(' ')))

sum=sum(l)

count=0
n+=1

for i in range(5):
    sum+=1
    if (sum%n!=1):
        count+=1

print (count)    