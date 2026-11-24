price=float(input("enter your order filter amount"))
if price>199:
    print("free delivery and final price is: ",price)
else:
    final_price=price+40
    print("delivery charges applicable and final price is: ",final_price)
    
print("--"*20)

# 24rth QA question
a=10
b=20
c=30
if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")

print("--"*20)


#Ticket booking for movie
age = int (input("Enter your age: "))
if(age>5):
    print("you are eligible to book the ticket")
    if(age>=12 and age<=60):
        print("your ticket price is 200")
    elif(age<12):
        print("your ticket price is 100")
else:
    print("Ticket is not required")        


