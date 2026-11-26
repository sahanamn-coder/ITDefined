
#Calculator
a=10
b=20

print((a+b))
print((a-b))
print((a*b))
print((a/b))



#Print 1-10 numbers 
for i in range(1,10):
        print(i)

print("--"*20)

#Print a Table for 2 
num=2
for i in range(1,11):
    print(num*i)
    print(f"{num} * {i} = {i*num}")

print("--"*20)

# Reverse a String using for loop 
Str1="Mysore"
rev=""
for ch in Str1:
    rev=ch+rev
print(f"using for loop {rev}")

# reverse a String using while
str1="Mysore"
rev=""
ch=len(str1)-1
while ch>=0:
    rev=rev+str1[ch]
    ch=ch-1
print(f"using while loop {rev}")


#Reverse a number 
num=12345
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(f"using while loop {rev}")

#Reverse a number using for loop
numbers=12345
rev=int(str(numbers)[::-1])
print(f"using slice {rev}")

reversed_num=""
for i in str(numbers):
     reversed_num=i+reversed_num
reversed_num=int(reversed_num)
print(f"using for loop {reversed_num}")

