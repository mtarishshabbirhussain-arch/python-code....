# password = input("Password ::")
# if password == "1234":
#     print(" COrrect password . user login.")
# else:
#     print("wrong password." )

# #print name five time.NOTE
# for i in range(5):
#     print("my name is ali.")


# #calculator NOTE
# a = int(input("number 1:: "))
# b = int(input("number 2:: "))

# print("add::",a + b)
# print("subtraction::",a-b)
# print("mul::",a*b)
# print("divide::",a/b)

# Age calculator NOTE

# birth_year = int(input("my birth year:: "))
# age = 2026 - birth_year
# print("my age is", age,".")



# Square number NOTE
# num = int(input("enter number;; "))
# print ( "square::", num * num)


# # counting from 1 to 10. NOTE
# for i in range(1,11):
#     print (i)

# Table NOTE
# n = int(input("Enter Number:: "))
# for i in range(1,21):
#     print(n,"x",i," = ", n*i)

#limit of table NOTE
# n = int ( input( " Enter number:: "))
# limit = int(input("table limit:: "))
# for i in range(1, limit + 1):
#     print(f"{n} x {i} = {n*i}")

# Reverse table...10 to 1. NOTE

# n = int (input("Enter number:: "))
# for i in range(10,0,-1):
#     print (f"{n} x {i} = {n*i}")


# table only even or odd lines NOTE

# n = int(input("Enter number:: "))
# for i in range(1,11):
#     # if i % 2 == 0:
#     #     print("Even Table::",f"{n} x  {i} = {n*i}")
#         if i % 2 != 0:
#                 print("Odd Table::",f"{n} x  {i} = {n*i}")
#     # else:
#     #     print ("Odd Table::",f"{n} x {i} = {n*i}")

 #NOTE       
# wrong input se bachna..ager wrong input likha jye to program error na dr blky last wala message print kr de.

# try:
#     n = int(input("enter number::"))
#     for i in range (1,11):
#         print(f"{n} x {i} = {n*i}")
# except ValueError:
#     print("write only numbers::") 



# bigest number NOTE

# a = int(input("A: "))
# b = int(input("B: "))
# if a>b:
#     print("A is big no..")
# else:
#     print("B is bigest no..")

# NOTE Items add in list.

# fruits = [ "apple"," mango","banana"]
# print(fruits)
# fruits.append(["orange","peach"])
# print(fruits)

# NOTE ager zyda fruits add karna ho to...

# fruits = [ "apple"," mango","banana"]
# more_fruits = ["orange","graps","apple"]
# # for fruit in more_fruits:             # remove kr ka run karo code ko.
#     if fruit not in fruits:
#         fruits.append(fruit)
#     print(fruits)


# NOTE simple calculator

# x = int( input( " num 1 ::"))
# y = int ( input( " num 2 ::"))
# print (" add:: ", x+y)
# print ("subtraction:: ", x-y)
# print ( "multiplication:: ", x*y)
# print ("divion:: ", x/y)


# NOTE # user se do number liya or check kiya ka barda kon sa hai
# #  or choota kon sa hai.

# num1 = int(input("first number."))
# num2 =int (input("second number.")) 
# if num1 < num2:
#     print(num1,"choota number hai.")
    
# else:
#     print (num1,"bara number hai.")



#Calculator... NOTE


# a = 10 
# b = 10
# op = "+"

# if op == "+":
#     print(a+b)
# elif op == "-":
#     print (a-b)
# elif op == "*":
#     print(a*b)
# elif op == "/":
#     print(a/b)
# else:
#     print("Both number are equal.")

# NOTE factorial
# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i

#     print("factorial::",fact)

# NOTE table...
# num = 6
# print ("table  of..",num)
# for i in range(1,6):
#     result = num * i
#     print (f"{num} x {i} = {num * i}")

# NOTE palindrome number

# num = 3
# original = num
# ulta = 0
# while num > 0:
#     digit = num % 10
#     ulta = ulta * 10 + digit 
#     num = num // 10 


# if original == ulta:
#         print("Palandrome::")
# else:
#         print("not palandrome")

# TODO  Lecture # 01...........😎😎😁😀 
# NOTE Arithmetic Operators, Relational Operators.......

# a = 10
# b = 2

# # Arithmetic Operators
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Remainder:", a % b)
# print("Power:", a ** b)
#NOTE
# # Relational Operators
# print("Equal:", a == b)
# print("Not Equal:", a != b)
# print("Greater Than:", a > b)
# print("Less Than:", a < b)
# print("Greater Than or Equal:", a >= b)
# print("Less Than or Equal:", a <= b)


# NOTE
# Assignment operator......


# x = 10

# x += 5
# print(x)   # 15

# x -= 3
# print(x)   # 12

# x *= 2
# print(x)   # 24

# x /= 4
# print(x)   # 6.0


# x = 10
# x %= 3
# print(x) # remainder 1

# x = 13
# x //= 4
# print(x) # floore division

# x = 4
# x **= 2
# print (x) #  power 16


# NOTE logical operator....

# x = 10
# y = 5


# print (not(x != y))  # output True ..but not operator change it..False..
# print (not(x == y) ) # output False ..but not operator change it..True..


# NOTE  AND Operator
# val1 = True
# val2 = True
# val3 = False
# val4 = False

# print (" And Answer::", (x > y) and (x == y)) # False

# print (" And Answer::", val1 and val2) # True
# print (" And Answer::", val1 and val3) # False
# print (" And Answer::", val3 and val2) # False
# print (" And Answer::", val3 and val4) # False

# NOTE  OR Operator

# val1 = True
# val2 = True
# val3 = False
# val4 = False

# print (" OR Answer::", (x > y) or (x == y)) # True

# print (" OR Answer::", val1 or val2) # True
# print (" OR Answer::", val1 or val3) # True
# print (" OR Answer::", val3 or val2) # True
# print (" OR Answer::", val3 or val4) # False


# NOTE User se number lo aur check karo even hai ya odd.

# number1 = int(input("Enter 1st number: "))
# number2 = int(input("Enter 2nd number: "))

# if number1 % 2 == 0:

#     if number2 % 2 == 0:
#         print("Both numbers are even.")
#     else:
#         print(number1, "is even and", number2, "is odd.")

# else:

#     if number2 % 2 == 0:
#         print(number1, "is odd and", number2, "is even.")
#     else:
#         print("Both numbers are odd.")



# TODO Type conversoion value ki type ko convert karna la use
# hoti hai.  type1 == conversion(automatically conversion)
# and type2 == casting(manually conversion)  type1 and type2
# dono ka use conversion ka liya hota hai.

# NOTE type1 ...Isko implicit type conversion kehte hain.

# a = 2  # value change automatically in float..(2.0)   #Python automatically 2 ko float mein convert kar deta hai
# b = 4.25    # float superior(>) hota ha int se..
#             #because ya value ki detail ko show krta hai...
# sum = a + b
# print("Sum:", sum)  # Output: 2.0 + 4.25  => 6.25
# print("Type of sum:", type(sum))  # Output: <class 'float'>

# NOTE type2 ...Isko explicit type conversion kehte hain.

# a = 3.14
# print(type(a))  # output :: float...
# print(a)  # output :: 3.14
# a = int(a)      #output :: 3..manually convert float to int..(explicit type conversion)
# print(type(a))  # output : class int...
# print(a) 
# a = float(int(a)) # again convert.
# print(type(a))  # output : class float...
# print(a) # output :: 3.0

#NOTE input two numbers and print their sum....
# val1 = int(input("enter value 1:" ))
# val2 = int(input("enter value 2:" ))
# sum = val1 + val2
# print ("sum two numbers:: ",sum)          
# print(type(sum))

#NOTE print area of square...
# square = float(input("enter square area:: "))
# area = square * square  # or print("square area: " , square ** 2)
# print("square area: " , area)
# print(type(area))

#NOTE 2 floating point numbers (or int number)  and print their average...

# val1 = float(input("enter value 1: " ))
# val2 = float(input("enter value 2: " ))

# print("Average of two number: ", (val1 + val2)/2)

# NOTE input 2 numbers (integer type) a and b...
# print true if a is greater than or equal to b.. if not print false.

# a = int ( input("Enter 1st number:: "))
# b = int (input("Enter 2nd number:: "))

# print(a >= b) # print true other wise print false...


# TODO  👉🤜 Lecture 2 : Strings & Conditional Statements 🤛👈
# ! IMPORTANT  :::
# escape sequence character :: used for tab space in sentence => \t
# and \n used for next line in sentance.....

# NOTE example of escape sequence character:
# val = "Hello\tWorld\nPython"
# print(val)  # Output: Hello    World
#             #         Python

# # ! IMPORTANT  :::
# NOTE strings:: =>
# basic operations in strings:

#NOTE example of string concatenation.

# NOTE first is string concatenation (joining two strings together) using the + operator.
# a = "Hello"
# b = "World"
# c = a + " " + b  # 👉OR 👈c = "a" + "b"🤛...OR...👈 c = a+b
# print(c)  # Output: Hello World  ....OR...print (a+b)  # Output: HelloWorld

# NOTE length of string using len() function.
#! important ::: length of str is used to calculate the number of characters in a string, 
#! including spaces and special characters.

#NOTE example of length of string using len() function.

# str1 = "Hello World"
# len = len(str1) # store str1 in new variable len.
# print(len)  # Output: 11
# print("Length of string is : " , len)  # Output: 11

#NOTE indexing in strings using square brackets []. #! Example of indexing.
# NOTE Indexing kyun use hoti hai?
# Kisi string ka ek specific character nikalne ke liye.
# Kisi list ka ek specific item access karne ke liye.


# a = "muhammad tarish"
# b = a[0]  # first character of string a
# print(b)
# e = a[-1]  # last character of string a
# print(e)
# c = a[8]  # space ko print karega # space ko bhi count kiya jata hai. and special character.
# print(c)

#TODO ......slicing...........😎😎😁😀
# NOTE slicing in strings using square brackets [] and colon :.
# slicing ka use string ke ek part ko extract("Kisi string ka hissa) nikalne ke liye hota hai.

# a = "muhammadtarish"
# print(a[4:len(a)])  # output : mmadtarish
# b = a[0:12]  # slicing from index 0 to 11 (12 is not included)
# b = a[0:12:2]  # slicing from index 0 to 11 with step 2 (every second character)
# print(b)
# print(a[::-1]) # output :hsiratdammahum
# print(a[::-3]) # output : hrdmu
# print(a[-2::-2]) # output : srtamhm
# print(a[-1::-5]) # output : hta
# print(a[11::2]) # output : ih 
# print(a[-7::]) # output : dtarish
# print(a[:-5:]) # output : muhammadt
# print(a[::-2]) # output : hiadmaus
# print(a[-1:5:-1])  # output : hsiratda
# print(a[-1:-13:-2]) # output : hsitdmh
# print(a[5:1:-1]) # output : mmah
# print(a[5:-1:+2]) # output :  mdai
# print(a[5:-1:-1]) # output :  # empty string
# print(a[-5:1:-1]) # output : atdammah
# print(a[-5:1]) # output :  # empty string
# print(a[5:-1]) # output : madtaris
# print(a[-1:-5]) # output:  # empty string
# print(a[0:12:2]) # output: mhmtrh
# print(a[4:]) # output: mmadtarish


# TODO string funcations:
# TODO 1. str.endswith("kisi bhi string ka last character") # ya use hota hai check karne ke liye ka string ka end me kya hai.

# str = "i am a coder."
# print (str.endswith("er")) # output : False
# print (str.endswith("er.")) # output : True

# TODO 2. str.startswith("kisi bhi string ka first character") # ya use hota hai check karne ke liye ka string ka start me kya hai.

str = "i_am a coder."
# print (str.startswith("i")) # output : true
# print (str.startswith("i_")) # output : true 
# print(str.startswith("i_am")) # OUTPUT :TRUE 
# print(str.startswith("am")) # OUTPUT :false 

# TODO 3.  capitalize() Pehla letter capital..
# str = "i_am a coder."
# print(str.capitalize())    # output : I_am a coder. #NOTE es ko comment kr do ager [ str = str.capitalize() ] run krna han to..
# # str = str.capitalize()    # es liya lga ya ka output change na ho ager capitilize funcation use krna ka bad...

# print(str)                  # output : i_am a coder.  # original string is not changed. to es liya.. str = str.capitalize() 


# TODO 4. replace() ka use string me kisi old character ko new character se replace karne.
# str = "i a studing from minhaj college." # orignal string is not changed. to es liya.. str = str.replace("minhaj","minhaj university")
# print(str)  # output : i a studing from minhaj college.
# print(str.replace("minhaj college","minhaj university")) # replace old character with new character.
# str = str.replace("minhaj college","minhaj university") # replace old character with new character.
# print (str)

# TODO 5.  find() ka use string me kisi character ka index find karne ke liye hota hai. 
# TODO #   ka wo word string mein exist karta hai ya nahi. or agar exist karta hai to uska index return karega.
# TODO #   or agar exist nahi karta to -1 return karega.

# str = "my name is tarish. i am a student of minhaj university."
# print(str.find("d")) # output : 29
# print(str.find("tarish")) # output : 11
# print(str.find("minhaj")) # output : 37
# print(str.find("class")) # output : -1  # because class word is not exist in string.
 
#TODO 6.  count() ka use string me kisi character ka count karne ke liye hota hai. ka wo hamari string mein ktni dfa aaya hai.

# str = "my name is tarish. i am a student of minhaj university."
# print(str.count ("t")) # output : 4  # because ..t.. character is exist 4 dfa in string.
# print(str.count("student")) # output : 1  # because ..student.. word is exist 1 dfa in string.

#TODO 7.  isdigit() ka use string me check karne ke liye hota hai ka wo string sirf digits se bana hai ya nahi.
# str = "123456"
# print(str.isdigit()) # output : True  # because ..str.. string is only digits.

# str = "1234a56"
# print(str.isdigit()) # output : False  # because ..str.. string is not only digits. it has a character 'a' in it.

#TODO 8.  isalpha() ka use string me check karne ke liye hota hai ka wo string sirf alphabets se bana hai ya nahi.
# str = "abcdef"
# print(str.isalpha()) # output : True  # because ..str.. string is only alphabets.

# str = "abcd4ef"
# print(str.isalpha()) # output : False  # because ..str.. string is not only alphabets.

#TODO 9.  isalnum() ka use string me check karne ke liye hota hai ka wo string sirf alphabets aur digits se bana hai ya nahi.
# str = "abc123"
# print(str.isalnum()) # output : True  # because ..str.. string is only alphabets and digits.

# str = "abc123!"
# print(str.isalnum()) # output : False  # because ..str.. string is not only alphabets and digits.

#TODO 10.  isspace() ka use string me check karne ke liye hota hai ka wo string sirf spaces se bana hai ya nahi.
# str = "   "
# print(str.isspace()) # output : True  # because ..str.. string is only spaces.

# str = " acd "
# print(str.isspace()) # output : False  # because ..str.. string is not only spaces. it has a character 'a' in it.

#TODO String program for practice:....... 👉👉🤛👉👉👉👉👉👉👉👉👉👉👉🤦‍♂️😉
############ input user first name & prints its length.🤦‍♂️😉
# str = input("Enter name:: ")  # input :: tarish
# print("lenght of the name:: ",len(str))  # output :: 6

############ To find the occurance(Kitni baar koi cheez appear (nazar) aaye.) of a dollar in a string...🤦‍♂️😉
# str = "My salary is $500 and my bonus is $100."
# print(str.count("$"))   # output :: 2

#TODO ####### conditional statements....#######
# NOTE # ....if-elif-else  #indendation. ka matlab print statement likhana se pehla 4 (tab) spaces ko kehta hai..
# marks = int (input ("Enter student marks:: "))

# if (marks >= 90):
#     print("grade:: A+")
# elif(marks >= 80 and marks < 90):
#     print("grade:: B")
# elif(marks >= 70 and marks < 80):
#     print("grade:: C")
# elif(marks >= 60 and marks < 70):
#     print("grade:: D")
# elif(marks >= 50 and marks < 60):
#     print("grade:: E")
# else:
#     print("grade:: F")

#TODO  ####.... nesting program..... ####

# age = int (input("Enter age:: "))
# if (age >= 18):
    
#     if(age >= 80):
#         print("can no driving.")
#     else:
#         print("can driving.")
# else:
#     print("minor")

#! ========================================================>>>>>>>.. Practice programs..==============
# NOTE WAP to check if a number entered  by the user is odd or even.......
# num = int (input("Enter any number:: "))
#                                     # remander = num % 2
# if(num %2 == 0):                    # if(remander == 0)
#     print("This number is even.") 
# else:
#     print("This number is odd.")

#  NOTE WAP to find the greatest of 3 numbers entered by the user .....
# a = int(input("Enter first numbers:: "))
# b = int(input("Enter second numbers:: "))
# c = int(input("Enter third numbers:: "))
# if(a>b and a>c):
#     print("a is greatest number")
# elif (b>c):
#     print("b is greatest number.")
# else:
#     print("c is greatest number.")

# NOTE WAP to find the greatest of 4 numbers entered by the user .....

# a = int(input("Enter 1st numbmer:: "))
# b = int (input("Enter 2nd number:: "))
# c = int (input("Enter 3rd number:: "))
# d = int(input("Enter 4th nunber:: "))

# if(a>b and a>c and a>d):
#     print ("The larget number is:",a)
# elif (b>a and b>c and b>d):
#     print("The largest number is ",b)
# elif(c>a and c>b and c>d):
#     print("The largest number is" ,c)
# else:
#     print("The largest number is ", d)

# NOTE WAP to check if a number is a multiple of 7 or not..

# num = int(input("Enter a number:: "))

# if(num %7 == 0):
#     print(num, "Multiple of 7. ")
# else:
#     print(num, "Not multiple of 7.")

  





















