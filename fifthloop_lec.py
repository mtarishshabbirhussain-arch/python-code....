# TODO ________Lecture 5 : Loops in Python | While & For Loops | __________________

# count = 1
# while count <= 5:
#     print("tarISH")
#     count += 1

# print(count)

#!_____________________________________________________________________________________________

# i = 1
# while i <= 3:
#     print("tarish")
#     i += 1
# print(i)
#!__________________________________________________________________________

# i = 0
# while i <= 5:
#     print(i)
#     i += 1
'''____________________________________________________________''' 

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
'''__________________________________________________________'''

# print number from 1 to 100.
# i = 1 
# while i <= 100:
#     print(i)
#     i += 1
'''___________________________________________'''

# print number from 100 to 1.
# i = 100
# while i >=1:
#     print(i)
#     i -= 1
'''_________________________________________________'''

# print table of "n" number...

# n = int(input("Enter number:: "))
# i = 1
# while i <= 10:
#     print(n,"x",i,"=",n*i)
#     i += 1
'''______________________________________________________''' 
# print the number of following list using a loop.

# n = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx <= len(n) - 1:
#     print(n[idx])
#     idx += 1   
'''_______________________________________________________'''
# search for a number x in this tuple using loop.:

# nums = (1,4,9,16,25,36,49,64,36,81,100,36)

# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("index is  ",i)
#     else:
#         print("finding...")

    # i += 1
'''____(___________________________________________________________'''

#! ________________________ break and continue keyword __________________________

# i = 1
# while i <= 5:
#     print(i)
#     if(i==3):   
#         break
#     i += 1
'''_______________________________________________________________'''
# i = 1
# while i <= 5:
#     if(i==3): 
#         i += 1  
#         continue
#     print(i)
#     i += 1
'''_____________________________________________________________'''

#! print odd number.
  
# i = 1
# while i <=  10:
#     if (i %2 ==0):
#         i += 1
#         continue
#     print(i)
#     i += 1
'''___________________________________________________'''
#! print even number..

# i = 1
# while i <=  10:
#     if (i %2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1
'''___________________________________________________________'''

#! Ek program banao jo 1 se 10 tak numbers print kare.
#! Agar number 5 aaye → break use karke loop ko stop kar do.
#! Agar number 3 aaye → continue use karke 3 ko skip kar do.
#! Baqi numbers print hon.

# i = 1 
# while i <= 10:
#         if(i == 3):
#              i += 1
#              continue
#         if(i == 5):
#                print(i)
#                break   
#         print(i)
#         i += 1
'''________________________________________________________'''

#! 1 se 20 tak numbers check karo.

#! Agar number odd ho → continue se skip karo.
#!  Sirf even numbers print karo.
#! Agar number 16 aaye → break se loop stop karo.

# i = 1
# while i <= 20:
#     if (i == 16):
#         print(i) # print number 1 to 16..
#         break

#     if(i %2 != 0):
#          # print even number...
#         i += 1
#         continue

#     print(i) # print number 1 to 20...
#     i += 1
'''________________________________________________________'''

#! 1 se 15 tak numbers print karo.

#! 5 ko continue se skip karo.
#! 9 par break karo.
#! Baqi numbers print karo.

# i = 1
# while i <= 15:
#     if(i == 9):
#         print(i)
#         break
#     if(i == 5):
#         i += 1        
#         continue
#     print(i)
#     i += 1
'''_________________________________________________________'''

# while True:
#     num = int(input("Enter number: "))

#     if num == 0:
#         break
#     if num < 0:
#         continue
#     print(num)
'''__________________________________________________________'''
#! ________________ For Loop _____________________


# foods = ["apple","banana","grapes","orange","cucumber"]

# for val in foods:
#     print(val)
'''_________________________________________________'''


# nums = (1,5,3,6,7,9,2,5,0,7)

# for val in nums:
#     print(val)

'''__________________________________________'''
# str = "muhammadtarish"
# for char in str:
#     if(char == "f"):
#         print("d is found.")
#         break
#     print(char)
# else:
#     print("not found.")
"""________________________________________________________"""
# nums = [1,4,9,16,25,36,49,64,91,100,49]

# x = 49

# idx = 0
# for val in nums:
#     if(val == x):
#         print("number index is ",idx)
#     idx += 1
'''__________________________________________________________________'''


#! __________________________________ Range Funcation _____________________

# for i in range(0,10):
#     print (i)
'''___________________________________________'''

# for i in range(1,10,2):
#    print (i)
'''_____________________________________________'''
# n = 3
# for i in range(1,11):
#    print(n * i)
'''_______________________________________________'''

#! ______________________ pass statement ________________________

# for i in range(5):
#     pass   # used for empty print...
# print("Ali is a gentleman.")
'''__________________________________________________'''
n = 1
while n <= 5:
     print(n)
     n += 1
















































































   