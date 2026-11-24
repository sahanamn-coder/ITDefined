#sum of numbers 
numbers = [1,2,3,4,6,7]
print(sum(numbers)) # function we can use 

sum=0
for num in numbers:
    sum+=num
print(f"The total sum of numers is {sum}") ## for loop approach

print("--"*20)
print(len(numbers))