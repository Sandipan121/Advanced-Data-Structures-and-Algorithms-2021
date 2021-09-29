def factorialLargeNumber(n=int(input('Enter the number:'))):
    result=[None]*10000000
    output=[]
    result[0]=1
    digit_length=1
    x,q,carry=0,2,0
    if n<0:
        return None
    while(q<=n):
        x=0
        while x<digit_length:
            result[x]=result[x]*q
            result[x]=result[x]+carry
            carry=result[x]//10
            result[x]=result[x]%10
            #increase the value of x to exit the loop
            x+=1
        q+=1
        while(carry!=0):
            result[digit_length]=carry%10
            carry=carry//10
            digit_length+=1
    for x in result:
        if x!=None:
            output.insert(0,x)
        else:
            break
    return output
if __name__=='__main__':
    print('Factorial is:',end='')
    ans=factorialLargeNumber()
    if ans==None:
        print('Enter a valid number')
    else:
        for x in ans:
            print(x,end='')
        print()