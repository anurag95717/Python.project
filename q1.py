#for i in range(1,11):
#    if i%2==0:
#        print(i)
#sum=0
#for i in range(1,111):
#    sum +=i
#    print(sum)
#name='navinvidyarthi'
#for i in range(len(name) - 1,-1, -1):
#    print(name[i])
#vowels='aeiou'
#n='navin vidyarthi'
#count=0
#for i in n:
#    if i in vowels:
#        count +=1
#print(f'Total vowels in {n} is {count}')
#a=0
#b=1
#print(a,b, end=" ")
#for i in range(10):
#    next=a+b
#    print(next,end=" ")
#    a,b=b,next
#n=5
#sum=1
#for i in range(1,n+1):
#    sum*=i
#    print(sum)
#num=7
#is_prime=True
#for i in range(2,int(25**0.5)+1):
#    if num%i==0:
#        is_prime=False
#        break
#if is_prime and num > 1:
#    print(num,"is a prime number")
#else:
#    print(num,"is not a prime number")
name='programming'
char_count={}
for chr in name:
    if chr in char_count:
        char_count[chr]+=1
    else:
        char_count[chr]=1
for chr,count in char_count.items():
    print(chr + ':', count)