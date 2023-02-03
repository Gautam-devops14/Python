# The Syntax of Dictionary Data Type

# fruit = {'Apple':30,'Mango':40}
# print(type(fruit),fruit)

#Extracting Keys & Value

fruit = {'Apple':30,'Mango':40,'Guvava':90}
# print(fruit.keys())
# print(fruit.values())

# Mutable Changing or Adding a Element

#Changing The Element
# fruit['Apple']=50
# print(fruit)


#Adding An Element
# fruit = {'Apple':30,'Mango':40,'Guvava':90}
# fruit['Banana']=60
# print(fruit)


# Updating a dictionary two elements into One Elements

f1 = {'Apple':30,'Mango':40,'Guvava':90}
f2 = {'Pineapple':55,'Watermelon':88,'Banana':460}

f1.update(f2)
print(f1)

#Popping Out an Eelement

f1.pop('Apple')
print(f1)
