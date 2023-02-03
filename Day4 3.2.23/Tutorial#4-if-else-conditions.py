#we use conditional operators in if else most of the...
        #here this is an example of blueprint of if-else statements writing style

# a = 10
# b = 9

# if(a<b):
#     print("Its Valid That 20 is greater than 10")\

# else:
#     print("No Its not valid 20 is not greator than 10")

# a = 10
# b = 20
# c = 30

# if(a<b) & (b<c):
#     print("A is less than B & B is the less than c")
# elif(a>b):
#     print("B is greater")
# else:
#     print("all values are equal")


#---------------------if with tuples---------------#

tup1 = ('a','b','c')

if 'z' in tup1:
    print("Value A is [present in Tuple1")
    
else:
    print("Value Z is not present in Tuple1")

#---------------------if with tuples---------------#

#---------------------if with lists---------------#

lis1 = ['a','b','c']

# print(type(lis1))
opt = str(input("Enter The Alpahbet "))
print("Your alphabet is ",opt)

if opt in lis1:
    print("Your given alphabet",opt," is present in list ")
    # opt1 = str(input("Give the alphabet which u want to add"))#append funciton
else:
    print("Your given alphabet",opt," is not present in list")

print("Did not you get your alphabet, You can add it")
opt1 = str(input("Give the alphabet which u want to add"))#append funciton

lis1.append(opt1)
if lis1:
    print("Your Value",opt1,"Has Been Added")
    print("Thanks For Adding A New Value here is the New updated List")
    print(lis1)
else:
    print("Unfortunatly our server is down right now || Try Again Later")


# if opt1.append():
#     print("Your Value has been entered")
# opt1 = str(input("Give the alphabet which u want to add"))#append funciton