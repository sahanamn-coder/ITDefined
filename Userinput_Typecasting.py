birth_year=int(input("enter your birth year: "))
age= 2026-birth_year    
print("your age is: ",age)
if(age>=18):
    print("you are eligible to vote")
elif(age<18):
    print("you are not eligible to vote")