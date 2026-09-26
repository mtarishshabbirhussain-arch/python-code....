# TODO ........Dictionary&Set
# es ka under hn list,tuple,bollean vlue,float vlue bhi store kr skta hai.

# student = {
#     "name" : "tarish",
#     "subject" : ["python","java","cpp"], # list...
#     "marks" : (40,50,27,45), # tuple
#     "is_adult" : True, # bolean value
#     "cgpa" : 3.5,  # float value

# }

# print(student)  # print whole dictionary


# print(student["name"])  # print single value
# print(student["subject"])   # print single value
# print(student["marks"])   # print single value
# print(student["is_adult"])   # print single value
# print(student["cgpa"])     # print single value


# student["name"] = "Ali"
# print("change key value of name: ",student) # change value in dictionary..


# student["city"] = "Lahore"
# print(student)   # add new value..in dictionary...


'''____________________________________________________________________________________________________'''

# TODO :: ________________________ create null dictionary & add value in empty dictionary ____________________________________

# null_dict = {}
# print(null_dict)  # empty dictionary  {}
# null_dict["name"] = "zubair"
# print(null_dict)  # {'name': 'zubair'}
'''___________________________________End code____________________________________'''
# TODO '''_____________________________________________ nested dictionary  ____________________________________________'''
#!  __________________________________________ Program nested dict.. _________________________________________
# student = {
#         "name1" : "ali",
#         "std1" : {
#             "age" : 21,
#             "marks" : 85,
#         },
#         "name2" : "zain",
#                 "std2" : {
#                     "age" : 19,
#                     "marks" : 95,
#                     "address" : "lahore"
#         }
# }
       
# print(student)  # whole dict print.....
'''___________________________________________________________________________________________'''
# print(student["name1"]) # output :: ali
# print(student["std1"])  # output :: {'age': 21, 'marks': 85}
# print(student["std1"]["age"])  # output :: 'age': 21
# print(student["std1"]["marks"])  # output :: 'marks': 85
'''____________________________________________________________________________________________'''
# print(student["name1"],["std1"]) # output :: ali ['std1'] but not valid....
# print(student["name1"]["std1"]) # Error
# print(student,["name1"]["std1"]) # Error
# print(student,["std1"]["age"]["marks"]) # Error
'''________________________________________________________________________________________________'''
# print(student["name2"]) # output :: zain
# print(student["std2"])  # output :: {'age': 19, 'marks': 95, 'address': 'lahore'}
# print(student["std2"]["age"])  # output :: 'age': 19
# print(student["std2"]["marks"])  # output :: 'marks': 95
# print(student["std2"]["address"])  # output :: 'address' : lahore

'''___________________________________________________ End program dict _____________________________________ '''

#TODO _________________________________ Dictionary method ________________________________________________

#!_____________________ dict.keys() _________________

# student = {
#         "name1" : "ali",
#         "std1" : {
#             "age" : 21,
#             "marks" : 85,
#         }
# }

# print(student.keys()) # use ho ga ka kitni keys hai hamari dict mein or un ka output :: dict_keys(['name1', 'std1'])
# print(len(student.keys())) #output :: 2 .....  us ki length btaye ga dict ki...
# print(list(student.keys())) # type casting ki han..ab output list (ager tuple lagaye to tuple mein aye ga.) mein aaye ga... output : ['name1', 'std1']
'''________________________________________________ END CODE ________________________________________'''
# ! ________________________________ dict.value() _________________________________________

# student = {
#         "name1" : "ali",
#         "std1" : {
#             "age" : 21,
#             "marks" : 85,
#         }
# }

# print(student.values()) # return all values (both dictionary).... # output :: dict_values(['ali', {'age': 21, 'marks': 85}])
# print(list(student.values())) # type casting (convert into list) ..output..:['ali', {'age': 21, 'marks': 85}]
'''__________________________________________________ End code ___________________________'''
# ! ________________________________ dict.items() _________________________________________


# student = {
#         "name1" : "ali",
#         "std1" : {
#             "age" : 21,
#             "marks" : 85,
#         }
# }


# dictionary = (student.items())
# print("student_dict :  ",dictionary) # output : student_dict :   dict_items([('name1', 'ali'), ('std1', {'age': 21, 'marks': 85})])
# # print(type(list(student.items())))
# pairs = list(student.items())
# print(pairs[0]) # output :: ('name1', 'ali')
# print(pairs[0][0])  # output :: name1
# print(pairs[0][1]) # output :: ali
# print(pairs[1])  # output :: ('std1', {'age': 21, 'marks': 85})
# print(pairs[1][0]) # output :::  std1
# print(pairs[1][1]) # output::: {'age': 21, 'marks': 85}
# print(pairs[1][1]["marks"]) # output :: 85

# print(student.items()) # all pairs ko print kr de ga...output :: dict_items([('name1', 'ali'), ('std1', {'age': 21, 'marks': 85})])
# print(len(student.items()))  # output :: 2
# print(list(student.items())) # output ko list mein kr de ga../[('name1', 'ali'), ('std1', {'age': 21, 'marks': 85})]
# print(student["std1"]["marks"] + student["std1"]["age"]) # output :: 106
'''_______________________________________________________________  End code ______________________________'''
#! __________________________________ dic.get("key") _________________________
# student = {
#         "name1" : "ali",
#         "std1" : {
#             "age" : 21,
#             "marks" : 85,
#         }
# }

# print(student.get("name2")) # both take same value..if key is wrong he print "None" ......
# print(student["name2"]) # both take same value..if key is wrong he get error ......
'''____________________________ End code ___________________________________'''

#! __________________________________ dic.update({"key" : "value"}) _________________________

# student = {
#     "name" :"ahmed",
#     "std" : {
#             "age" : 21,
#         "roll_no" : 23
#     }
#     }
# new_dict=({"name":"zain","address" : "lahore", "birth" : "12-12-2005"})
# (student.update(new_dict))
# print(student)

# print(student["std"]["age"])
# print(student["std"])
# print(student)
'''______________________________ End code _________________________________'''

# TODO _______________ Data type (sets in python) ____________________________************
# sets mutable hota hai..or es ka elements immutable hota hai..

# a = set()   # empty set syntax
# print(type(a)) #  <class 'set'>

# sets = {1,2,3,4,4,3,5,"hello","world","hello","world"}
# print(sets) # NOTE ignore doublicate value...set koi order follow nahi karta..koi bhi value kahi bhi print ho jati han...
# print(len(sets)) # 7
# print(type(sets)) # output :: <class 'set'>
'''___________________________________________________________________'''

# TODO ____________________ method of sets ___________________________________
#! _______________________________________ set.add() _______________________________

#ham sets mein tuple hi add kr skta hai,,or list or dict add nahi kr skta...

# marks = set()
# marks.add(23)
# marks.add(54)
# marks.add(52)
# marks.add(52)
# marks.add("tarish") 
# marks.add((1,2,3))
# print(marks)
# print(marks.pop())
# print(marks.pop())
# print(marks.pop())
# marks.clear()
# print(len(marks))
# marks.remove(54)
# marks.remove(52)
# print(marks)

# marks.add([2,4,5,6]) # list ha es liya ""error""" aaye ga...
# print(marks)
'''________________________________________ End code _______________________'''

#! _______________________________________ set.union() and intersection() _______________________________

# set1 = {1,2,3,4}
# set2 = {5,6,7,8,1,2,3,4,5,6}

# print(set1.union(set2)) # output :: {1, 2, 3, 4, 5, 6, 7, 8}
# print(set1.intersection(set2)) # output :: {1, 2, 3, 4}

'''______________________________________ End code _____________________________________'''

# todo ___________________________ practical question ___________________

#! __________________________ practical Question _____________________________ 
# NOTE  Store following word meanings in a python dictionary:
# table : "a piece of furniture", "list of facts & figures"cat : "a small animal"
'''________________________________________________________________________________'''

# word = {
#     "table" : ["a pice of furniture", "list of fact and figures"],
#     "cat" : "a small animal",
    
# }

# print(word) # output : {'table': ['a pice of furniture', 'list of fact and figures'], 'cat': 'a small animal'}

'''________________________________ End code _______________________________'''
 #! ______________________ Question 2 _____________________________________
# NOTE You are given a list of subjects for students. Assume one classroom is required for 1 subject.
#  How many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript","java", "python", "java", "C++", "C"
# set = {"java","c++","c","python","javascript","javascript","python","c","c","c++","python",}
'''___________________________________________________________________________'''

# print(set)
# print(len(set)) # output ;; 5
# print(type(set)) # output ;; <class 'set'>
'''________________________________ End code _______________________________'''

 #! ______________________ Question 3 _____________________________________

# NOTE :: Question 1WAP to enter marks of 3 subjects from the user and store 
# them in a dictionary. Start with an empty dictionary & add one by one. 
# Use subject name as key & marks as value.
'''_________________________________________________________'''

# subject = {}

# a = int(input("Enter first subject marks:; "))
# subject.update({"phy" : a})
# b = int(input("Enter second subject marks :: "))
# subject.update({"comp" : b})
# c = int(input("Enter third subject marks :: "))
# subject.update({"eng" : c})

# print(subject)

'''________________________________ End code _______________________________'''

#! ______________________ Question 3 _____________________________________
#NOTE Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types).

# value = {
#     ("float" , 9.0), # tuple  create..
#     ("int" , 9)    
# }
# print(type(value))
# print(value)

'''________________________________ End code _______________________________'''

# data = {
#     "name" : "tarish",
#     "age" : 23,
#     "city" : "lahore"
#     }
# (data.update({"course":"python"})) # add new (key and value)..
# print (data)
# (data.update({"age" : "21"})) # update value of age....
# print(data)
# print(data["name"],"_ ",data["age"])
# print(data)
'''________________________________ End code _______________________________'''

# std = {
#     "name" : "tarish",
#     "age" : "23",
#     "marks" : "95"
# }

# print(std["marks"])
# (std.update({"city" : "sialkot"}))
# print(std)
# (std.pop("age")) # delete age (key and value)
# del std["age"] # delete age (key and value)
# print(std)
'''________________________________ End code _______________________________'''

# student = {
#     "std" : {
#         "name":"tarish",
#         "age":"21",
#         "marks":"98"
#     }
# }
# print(student["std"]["name"])
# (student["std"].update({"marks":"95"}))
# print(student)
# student["std"].update({"address":"lahore"})
# print(student)
'''________________________________ End code _______________________________'''
# students = {
#     "student1":{
#         "name" : "tarish",
#         "age":"21",
#         "marks":"55"
#     },
#     "student2":{
#         "name":"zain",
#         "age":"33",
#         "marks":"89"
#     }
# }
# print("Name : ",students["student1"]["name"],"    ","Marks : ",students["student1"]["marks"])
# print("Name : ",students["student2"]["name"],"    ","Marks : ",students["student2"]["marks"])

'''________________________________ End code _______________________________'''

# set = {10,20,30,40,"tarish",2.5}
# set.add(50)
# set.remove(20)
# print(set)
'''________________________________ End code _______________________________'''

# set1 = {1,2,3,4}
# set2 = {4,5,6,7}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1 - set2) # output : {1, 2, 3}
# print(set2 - set1) # output :{5, 6, 7}
# print(set2 ^ set1) # output : {1, 2, 3, 5, 6, 7} 


'''________________________________ End code _______________________________'''

# colors = {"red", "blue", "green", "blue", "red"}
# print(colors)
# colors.add("yellow")
# print(colors)
# colors.remove("green")
# print(colors)
'''________________________________ End code _______________________________'''

# emp = {
#     "emp":{
          
        
#             "name": "ali",
#             "salary":"5000",
#             "city":"lahore"

#     },
#     "emp2":{
#         "name": "zain",
#         "salary":"6000",
#         "city":"sialkot"
#     }
# }
  
# for key , value in emp.items():
#     print ("name: ",value["name"],"  ","Salary : ",value["salary"],"  ","City : ",value["city"])
'''________________________________ End code _______________________________'''































































































#! _________________________________ Nested Dictionary + loop ________________________________________

# students = {
#     "student1": {
#         "name": "Ali",
#         "marks": 85
#     },
#     "student2": {
#         "name": "Zain",
#         "marks": 95
#     }
# }


# for key,value in students.items():
#     print(key)
#     print(value)
'''_______________________________________ END CODE __________________________________________'''
#!_____________________________________  Nested Dictionary + loop ________________________
# employees = {
#     "emp1": {
#         "name": "Ahmed",
#         "salary": 50000
#     },
#     "emp2": {
#         "name": "Sara",
#         "salary": 60000
#     },
#     "emp3": {
#         "name": "Usman",
#         "salary": 55000
#     }
# }

# for key, value in employees.items():
#     print("Name:", value["name"], "Salary:", value["salary"])
 
# Name: Ahmed Salary: 50000
# Name: Sara Salary: 60000
# Name: Usman Salary: 55000
'''________________________________________ END CODE _________________________________________'''
#!_____________________________________  Nested Dictionary + loop ________________________
# student = {
#         "name1" : "ali",
#         "std1" : {
#             "age" : 21,
#             "marks" : 85,
#         }
# }
# for key, value in student.items():
#     print(key, "=", value) # output : name1 = ali ....std1 = {'age': 21, 'marks': 85}
'''________________________________________ END CODE _________________________________________'''

































































































































































