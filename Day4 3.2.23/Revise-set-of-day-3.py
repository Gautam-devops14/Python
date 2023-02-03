    # This revise set of Day 3rd is conducting on Day 4
dic1 = {'Apple':30,'Banana':50,'Rohit Sharma':99,'Gill':95} #Common Var

#Question 1 Create A Function and make a Dictionary Var and show the data Type as a “Dict”

dic1 = {'Apple':30,'Banana':50,'Rohit Sharma':99,'Gill':95}
# print(type(dic1),dic1)

#----------------------------------------------------------------------

#Question 2 Create a function(a.Extract the Keys (b.Extract the values))

# a. Extract the keys
# b. Extract the values

# print(dic1)
# print(dic1.keys())
# print(dic1,"This is Seoncd Onee")
# print(dic1.values())

#----------------------------------------------------------------------


#Question 3 Create a function ((a. Add a new element(Pineapple - 80)(b.Changing A existing Element (Pineapple- 52)4.)))

# print(dic1)
# dic1['Pineapple'] = 80
# print(dic1)
# dic1['Pineapple'] = 52
# print(dic1)

#----------------------------------------------------------------------

#Question 4 Create a function and concatenating ((a.Join Two Var Name Shop1 & Shop2 (updating) {Shop-1 Given & Shop-2 Any})(b. Remove a specify element from Shop-1 (“Apple”)))

#(a.Join Two Var Name Shop1 & Shop2 (updating) {Shop-1 Given & Shop-2 Any})

# shop1 = {'Apple':30,'Banana':50,'Rohit Sharma':99,'Gill':95}
# shop2 = {'Mango':45,'Kiwi':65,'Virat':114,'Pant':105}

# print(shop1,"This is Shop1 List",shop2,'''THis is shop2 list''')
# shop1.update(shop2)
# print(shop1)

#----------------------------------------------------------------------

# shop1.pop('Apple')
# print(shop1)

#-------------------------------------------------------------------

#Question 5  Create a function and make a variable and show Data type as a Sets

# set1 = {9,1.45,'Mang'}

# print(type(set1),set1)

#-------------------------------------------------------------------

#Question 6 Create a Function and ((a.Add a value (‘Bata’) in sets)(b. Update existing Sets and update – 90,50,True value)(c. Remove a Specific Name from Sets))

#(a. Add a value (‘Bata’) in sets)

set1 = {9,1.45,'Mang'}

print(set1.add('Bata'))
print(set1)

#(b. Update existing Sets and update – 90,50,True value)

print(set1.update([90,50,True]),set1)
# print(set1)

#(c.Remove a Specific Name from Sets)

print(set1.remove('Bata'),set1)
# print(set1)
