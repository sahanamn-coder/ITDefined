#Step 1
def addnum():
    print("numbmers were added")

#addnum()

#Step2
def Addnum():
    print("numbmers were added")
    Pen=10
    Book=15
    return Pen+Book

output=Addnum()
print(output)

#Step3
def square(num):
    return num*num

data=square(3) 
print(data)


#Step4
def some_fun(inp_data):
    double_data=inp_data
    #print(id(double_data))

    for index,value in enumerate(double_data):
        double_data[index]=value*2
    return double_data

data=[10,20,30,40]
#print(id(data))
output=some_fun(data.copy())
print(output)