def collatz(number):

    if(number%2==0):
        return_value=number/2
        print (return_value)
        return return_value
    
    else:
        return_value=3*number+1
        print (return_value)
        return return_value

number=int(input())

return_value=collatz(number)

while(return_value!=1):
    return_value=collatz(return_value)