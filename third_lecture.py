# TODO list in python...

# marks = [45,36,78,34,89,45,76,45]
# print(marks) #output:: [45,36,78,34,89,45,76,45]
# print(type(marks))  #output :: <class 'list'>
# print(marks[6])  # output :: 76 "6 index number."
# print(len(marks)) # output :: 8
# TODO =============== mix list ==========
# student = ["Ali",24,85.0,"Lahore"]
# print("Student information:: " ,student)

#  # ager ham list mein kuch change krna chaha to kr skta hai....jis ko change krna hai us ka index likhna hai..
 
# student [0] = "Tarish"
# student [3] = "Sialkot"
# print("update student information::  ",student)#output : ["Tarish",24,85.0,"Sialkot"]

# # TODO  ==== lists slicing =====

from pickle import FALSE, TRUE
from re import A


marks = [45,36,78,34,89,45,76,45]
# print(marks[0:len(marks)]) #output : [45, 36, 78, 34, 89, 45, 76, 45]
# print(marks[:len(marks)]) # output : [45, 36, 78, 34, 89, 45, 76, 45] 
# print(marks[5:len(marks)])  # output : [45, 76, 45]
# print(marks[0:5])  # output : [45, 36, 78, 34, 89]
# print(marks[0:-4]) # output : [45, 36, 78, 34]
# print(marks[-1:-4:-1]) # output : [45, 76, 45]
# print(marks[-1:4:-1])
# print(marks[1:8:2])  # [36, 34, 45, 45]

# TODO =====  list method ======
# NOTE : list.append() # adds one elements at the end...

# list = ["ali", "ahmed", "umer", "bilal", "hassan"]
# print(list) # output : ["ali", "ahmed", "umer", "bilal", "hassan"]
# list.append("tarish") # adds one elements at the end...
# print(list) # output : ["ali", "ahmed", "umer", "bilal", "hassan", "tarish"] # mutation in list.

# TODO : list.sort() # sort the list in ascending order...
# list = [5,4,7,3,8,3,1,2,9]
# list.sort() # sort the list in ascending order...
# list.sort(reverse=True) # sort the list in descending order...
# print(list) # output : [9, 8, 7, 5, 4, 3, 3, 2, 1] # mutation in list.
# list.sort(reverse=False) # sort the list in ascending order...
# print(list) # output : [1, 2, 3, 3, 4, 5, 7, 8, 9] # mutation in list.

#TODO : list.reverse() # reverse the list...
# list = [1,2,3,4,5,6]
# list.reverse() # reverse the list...  
# print(list) # output : 6,5,4,3,2,1

# TODO : list.insert() # insert the element at specific index...
# list = [1,2,3,4,5,6]
# list.insert(2, 10) # insert 10 at index 2...
# print(list) # output : [1, 2, 10, 3, 4, 5, 6]

# TODO : list.remove() # remove the element from the list...
# list = [1,2,3,4,5,6]
# list.remove(4) # remove the element 4 from the list...
# print(list) # output : [1, 2, 3, 5, 6]

# TODO : list.pop() # remove the index element from the list...
# list = [1,2,3,4,5,6]
# list.pop(4) # remove the element at index 4...
# print(list) # output : [1, 2, 3, 4, 6]

#! TODO : ===========>....Tuples in python.....<===========(Built in data type)

# tuple = (1,2,3,4)
# tuple1 = (1,),1  
# tuple2 = () # empty tuple...
# print(tuple2) #output : ()
# print(type(tuple2)) # output : <class 'tuple'>
# print(tuple1) # output : ((1,), 1)
# print(type(tuple1)) # output :: <class 'tuple'>
# print(tuple)   # output : (1, 2, 3, 4)
# print(type(tuple)) # output :: <class 'tuple'>
# print(tuple [2]) # output : 3 bcz index 2..

# TODO : ====>..... slicing in tuple .......<=====
# #        0,1,2,3,4,5   # positive index
# tuple = (1,2,3,4,5,6)
#    #  -6,-5,-4,-3,-2,-1          # negative index

# print(tuple[1:3]) # output : (2, 3)
# print(tuple[1:len(tuple)]) # output :(2, 3, 4, 5, 6)
# print(tuple[1:]) # output :(2, 3, 4, 5, 6)
# print(tuple[:3]) # output :(1, 2, 3)
# print(tuple[-1:3:-1]) # output : (6, 5)
# print(tuple[3:-1:1]) # output : (4, 5)

# TODO :: tuple method
#! first method :: tuple.index(element) # element ka index btana ka liya..
#        0,1,2,3,4,5   # positive index
# tuple = (1,2,3,4,4,4,5,6)
# print(tuple.index(4)) # es ka under hm koi bhi element likha ga to uska index bta de ga...
# print(tuple.count(4)) # ya element kitni dfa aaya hai..wo btaye ga..

# TODO :: practical code....
# NOTE user enter three movies name and store it in list..

# movies = []
# name = (input("Enter movies name: "))
# name1 = (input("Enter movies name: "))
# name2 = (input("Enter movies name: "))
# (movies.append(name))
# (movies.append(name1))
# (movies.append(name2))
# print(movies)

# NOTE check if a list contains a palindrome of element .(hint: use copy() method )

# list  = [1,2,3]


# copy_list    = list.copy()
# copy_list.reverse()

# if (copy_list == list):
#     print("palandrom")
# else:
#     print("not palandrom")

# NOTE WAP to count the number of students with the a grade in the following tuple...
 
# grade = ("c","A","D","E","A","C","B","A")
# print(grade.count("A"))  # output :: 3
# print(type(grade)) # class :: tuple

#NOTE store the above values in a list and sort them from "A" to "Z"..

# list = ["F","A","D","E","A","C","B","A"]
# (list.sort())
# print(list)

# TODO PRACTICE QUESTION>>>>>>>>

#Ek khali list banao. User se 5 favourite fruits
#  ke naam lo aur list mein store karo. Aakhir mein poori list print karo.

fruits = []

# name1 = input("Enter fruits name:: ")
# name2 = input("Enter fruits name:: ")
# name3 = input("Enter fruits name:: ")
# (fruits.append(name1))
# (fruits.append(name2))
# (fruits.append(name3))

# print(fruits)
# ! ====================>>>..... dono way se same result aye ga.....👆👇.....

'''
# name = input("Enter fruits name:: ")
# (fruits.append(name))
# name = input("Enter fruits name:: ")
# (fruits.append(name))
# name = input("Enter fruits name:: ")
# (fruits.append(name))

print(fruits)
                            '''

# TODO ====== == ========  2nd question ========

# [10, 20, 30, 40, 50]
#😀 Last element print karo.
#😎Pehle 3 elements print karo.
#😊Last 2 elements print karo


marks = [10, 20, 30, 40, 50]
# print(marks[4])  #😀 Last element print karo.
# print(marks[:3])  #😎Pehle 3 elements print karo.
# print(marks[3:len(marks)])     #😊Last 2 elements print karo

#! ========     pop , insert  , remove......
# print(marks.pop(2))  # output : 30..
# (marks.insert(2,70)) #output::[10, 20, 70, 30, 40, 50]
# print(marks)  # remove index 3 element ..and insert 70...
# (marks.remove(30)) 
# print(marks)  # output :: [10, 20, 40, 50]


# TODO =========>>>>  ....3rd question.....  <=========

# Ek tuple banao jisme 7 weekdays ke naam hon.

# Pehla din print karo.
# Aakhri din print karo.
# Beech ke 3 din slicing se print karo.

# days = ("mon","tue","wed","thur","fri","sat","sun",)

# print(days[0])
# print(days[6])
# print(days[2:5])

# TODO =========>>>>  ....4th question.....  <=========

# List ko ascending order mein sort karo.
# Phir descending order mein sort karo.
# Number 45 kitni baar aaya hai, pata kar

# num = [12, 45, 23, 89, 11, 45,45, 67]
# num.sort()
# print(num) # output :: [11, 12, 23, 45, 45, 67, 89]
# num.sort(reverse=True) #output :: [89, 67, 45, 45, 23, 12, 11]..in decending order...
# print(num)
# num.sort(reverse=False) #output :: [11, 12, 23, 45, 45, 67, 89]..in ascending  order...
# print(num)
# print(num.count(45))  #output :: 3

# TODO =========>>>>  ....5th question.....  <=========

# User se 4 student names lo aur list mein store karo.

# Uske baad:

# Pehla student print karo.
# Aakhri student print karo.
# Sirf beech ke students print karo.

# std_name = []
# name = input("Enter student name::  ")
# std_name.append(name)
# name1 = input("Enter student name::  ")
# std_name.append(name1)
# name2 = input("Enter student name::  ")
# std_name.append(name2)
# name3 = input("Enter student name::  ")
# std_name.append(name3)
# print(std_name)   # output :: user enter 4 student name...and print on screen....

# print(std_name[-4:-3]) # print 1st name
# print(std_name[3:])    # print last name
# print(std_name[1:3])   # print between two name.

# TODO =========>>>>  ....6th question.....  <=========

# (Tuple)

# (5, 10, 15, 20, 25, 30)

# Sirf slicing use karke:

# (15, 20, 25) nikalo.
# Reverse order mein poora tuple print karo.

# mar = (5, 10, 15, 20, 25, 30)
# print(mar[2:5]) # output : 15,20,25
# print(mar[-1::-1]) # output : (30, 25, 20, 15, 10, 5)

# TODO =========>>>>  ....7th question.....  <=========

# Ek list mein movies hain.

# User se ek movie ka naam lo.

# Agar woh movie list mein ho to:

# "Movie Found"

# warna:

# "Movie Not Found"
'''--------------------------------------------WAY ONE---------------------------------------------------'''
# movies = []
# mov1 = input("Enter 1st movie name :  ")
# (movies.append(mov1))
# mov2 = input("Enter 2nd movie name :  ")
# (movies.append(mov2))
# mov3 = input("Enter 3rd movie name :  ")
# (movies.append(mov3))
# mov4 = input("Enter 4th movie name :  ")
# (movies.append(mov4))
# print(movies)

# new_movie = input("Enter name of movie.:==>  ")

# if (new_movie in movies):
#     print("movie found.")
# else:
#     print("not found.")
'''---------------------------------------------------------------------------------------------------'''
# movie = movies
# print(movie)
# print(movie.copy()) # copy list ...
# (movie.reverse())  # reverse list....
# print(movie)

# if (movies == movie):
#     print("movie found.")
# else:
#     print("not found.")
'''--------------------------------------------WAY TWO---------------------------------------------------------'''

# movie = ["veer","hero","villian","race"]

# movie.insert(0,"race2") # ['race2', 'veer', 'hero', 'villian', 'race']
# print(movie)
# movie.remove("veer") # ['race2', 'hero', 'villian', 'race']
# print(movie)
# movie.pop(2) # ['race2', 'hero', 'race']
# print(movie)
'''------------------------------------------------------------------------------------'''
# search_movie = input("Enter movie name:: ")
# if search_movie  in movie:
#     print("found movie.")
# else:
#     print("Not found.")
'''-----------------------------------------------------------------------------------------'''
# TODO =========>>>>  ....8th question.....  <=========

# tuple 

# Bina tuple ko badle:

# Pehle 4 elements print karo.
# Aakhri 3 elements print karo.
# Har doosra (alternate) element print karo

# num = (10, 20, 30, 40, 50, 60)

# print(num[0:4]) # (10, 20, 30, 40)
# print(num[-3:]) # (40, 50, 60)
# print(num[0::2]) # (10, 30, 50)

'''______________________________________________________________________________________________'''
# TODO =========>>>>  ....9th question.....  <=========
# User se 5 numbers lo aur list mein store karo.

# Uske baad:
# print("Sabse bada number:", max(num))
# print("Sabse chhota number:", min(num))

# num.sort()
# print("Ascending order:", num)

# num.sort(reverse=True)
# print("Descending order:", num)
# List ko ascending order mein print karo.
# List ko descending order mein print karo.
'''____________________________________________________________________'''
num = []

num1 = int(input("Enter 1st num:  "))
num.append(num1)
print(num)

num2 = int(input("Enter 2nd num:  "))
num.append(num2)
print(num)

num3 = int(input("Enter 3rd num:  "))
num.append(num3)
print(num)

num4 = int(input("Enter 4th num:  "))
num.append(num4)
print(num)

num5 = int(input("Enter 5th num:  "))
num.append(num5)
print(num)

print("Sabse bada number:", max(num))
print("Sabse chhota number:", min(num))

num.sort()
print("Ascending order:", num)

num.sort(reverse=True)
print("Descending order:", num)
'''__________________________________________________________________'''












































































































































