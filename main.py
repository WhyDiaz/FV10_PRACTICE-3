from pyscript import document, display

#Unique Keys: Values can have duplicates

#set1= {'sample1', "sample2"} 
#my_sample_data = {"Math": 95,
#"Science": 90,
#"Filipino": 90}
#"Math":91  #If added it only displays this because it updates and uses the most recent data added

#display(type(set1), target="output1") #Displays <class 'set'>
#display(type(my_sample_data), target="output1") #Displays <class 'dict'>
#display(my_sample_data['Math'], target="output1") #Displays 95 WOW!!!!!!
#display(my_sample_data, target="output1") 


#Conversions

#set1= {'sample1', "sample2"} 
#my_sample_data = {"Math": 95,
#"Science": 90,
#"Filipino": 90}

#Displays {'a':'x','b','y'}
#a = ('ax', "by")
#display(dict(a), target= "output1")

#a = {"b", "c"} #Displays syntax error cuz it REQUIRES 2 Values 
#display(dict(a), target= "output1")


#Combination

#Displays {'First Name':'Peter', 'Last Name': 'Parker', 'Category': 'Hero'}
#info1 = ['First Name', "Last Name", "Category"]
#info2 = ["Peter", "Parker", "Hero"]
#details = dict(zip(info1, info2))
#display(details, target= "output1")

#How to add a value and delete a value

#Displays {'Math':95, 'Science':90, 'Filipino':90, 'Social Studies':100,}
grades = {"Math": 95,
"Science": 90,
"Filipino": 90}

#grades['Social Studies'] = 100 
#display(grades, target="output1")

#Replaces the SS grade to the Math grade 
#grades['Math'] = 100 
#display(grades, target="output1")

del grades['Math']  
display(grades, target="output1")

#Merging dictionaries

#Method 1: Using the x | y 

#Method 2: Using the unpacking operator 
#You can merge two or more dictionaries udsing the operator 
#If both dictionaries contain the same key the latter dictionary overwrites gthe value.
#How it looks **Blank**

#Method 3: Using the update Method ()
#The update() method adds or replaces key value paris in the place (it modifies the original dictionary).
#You can also merge by updating one dictionary with another 
#How it looks like blank_x.update(Blank_y)

#Identifying information in dictionairies

#We can also find information in dictionareis 
#Use len() func to get the number of elements 
#Enter the key to get the value associated to a key.
#To check if the key exists, you can us the in keyword.
#We can also get the value of a key using the get() method 
#We can get the keys from the dictionary using the key() method.
#If you can get keys you can also get values using the values() method.
#Similarly we can retrieve a value associated with a specific key just like how we access in offsetting.

#Comparing Dictionaries

#Dictionaries are equal if they have the same keys and corresponding values, regardless of order. 
# == checkers for equality ; !=checks for inequality. 
#Looks like : display (Blank_1 == blank_2)