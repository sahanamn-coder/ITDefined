# given number is devisible or not 
num=7
if num%3==0 and num%5==0:
    print("given number is devisible")

#sum of digits in a number
number=1223
sum=0
for i in str(number):
    sum=sum+int(i)
print(sum)

num=12345
rev=0
while num>0:
    rem=num%10 
    rev=rev*10+rem 
    num=num//10
print(f"using while loop {rev}")
