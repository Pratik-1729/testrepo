# #1. Taking inputs
# num1 = int(input("enter ur number: "))
# print(num1)
# print("The data type is: ",type(num1))
# ## Taking string as input
# str_1 = input("Enter the Name: ")
# print("the name is: ",str_1)
# print("\n")
# print("The data type of name is: ",type(str_1))

# ## Float as input
# float_1 = float(input("enter the decimal: "))
# print(float_1)
# print("\n")
# print("The data type of decimal is: ",type(float_1))

'''
# arithmetic operations 

num1 = 20
num2  = 4
print("sum is:", num1+num2)
print("sub is:", num1-num2)
print("mul is:", num1*num2)
print("div is:", num1/num2)
print("floor div is:", num1//num2)
print("reminder is:", num1%num2)
'''


'''
#assignment operations
a = 2
b = 3
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
'''

'''
#bitwise operation
a = 16
b = 64
print(a>>1)
print(a<<1)
print(~a)
'''

'''
#if-else conditionals

a = 23
b = 14
if(a==b):
    print("Both are equal")
elif(a>=b):
    print(a,"is greater than",b)
else:
    print(b,"is greater than ",a)
'''


'''
#loops
for i in "Pratik":
    print(i,end=" ")
i = 10
while (i>0):
    print(i)
    i-=1
'''
#arrays, sets , list, tuple , dictionary
'''arr1=[]
arr2 = (34,546,87)
for i in range(1,11):
    arr1.append(i)
print(arr1)
arr1.insert(0,30)
print(arr1)

arr1.sort()
arr1.reverse()
arr1.extend(arr2)
print(arr1)
arr1.remove(30)
print(arr1.count(30))
arr3 = arr1.copy()'''

##Tuples
'''tup1 = (1,2,4,56,78)
print(tup1[2])
print(tup1.count(4))'''

##sets
'''set1 = {11,23,43,33,45,33,43,23,11,1}
set2 = {11,45,8,434,6788}
print(set1)
set1.update({87})
set1.remove(11)
set1.add(34)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1)'''

##dictionary
'''dict1 = {1 : "hello", 2 : "How", 3 : "are", 4 : "you?"}
print(dict1)
print(dict1.get(1))
print(dict1.values())
print(dict1.items())
print(dict1.keys())
print(dict1.fromkeys("how"))'''

##2d lists
'''arr2d = [[1,2,3],[4,5,6],[7,8,9]]
print(arr2d)
arr2d.reverse()
arr2d.sort()
arr2d.sort()
arr2d.append([[19,[245]]])
print(type(arr2d))
#'''

##Functions in Python
def factorial(n):
    if (n == 0):
        fact = 1
    else:
        fact = n * factorial(n-1)
    return fact
print(factorial(9))

