# i = 1
# while i <= 10:
#     print(i,end=" ")
#     i += 1
#10 se 1 tak reverse numbers print karo
# i = 10
# while i >= 1:
#     print(i,end=' ')
#     i -= 1
#3 User se ek number lo aur 1 se us number tak print karo
# n = int(input("enter the number: "))
# i = 1
# while i <= n:
#     print(i,end=' ')
#     i += 1
#a4 1 se 20 tak sirf even numbers print karo
# while True:
#     x = input("Type stop to exit: ")
#     if x == "stop":
#         break
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# num = int(input("Enter a number: "))

# store the original number
# original = num
# reverse = 0

# #reverse the number using while loop
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# # check palindrome
# if original == reverse:
#     print("Palindrome Number")
# else:
    
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# # start from the greater number
# lcm = max(a, b,c)

# while True:
#     if lcm % a == 0 and lcm % b == 0 and lcm % c == 0:
#         print("LCM =", lcm)
#         break
#     lcm += 1
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# lcm = max(a, b, c)

# while True:
#     if lcm % a == 0 and lcm % b == 0 and lcm % c == 0:
#         print("LCM =", lcm)
#         break
#     lcm += 1
# num = int(input("Enter a number: "))
# original = num
# sum_sq = 0

# while num > 0:
#     digit = num % 10
#     sum_sq += digit * digit
#     num //= 10

# if sum_sq == original:
#     print("Perfect (Square-Digit Type) Number")
# else:
#     print("Not Perfect (Square-Digit Type) Number")
# num = int(input("Enter a number: "))

# num = int(input("Enter a number: "))

# i = 1
# sum_factors = 0

# # find factors using while loop
# while i < num:
#     if num % i == 0:
#         sum_factors += i
#     i += 1

# # check perfect number
# if sum_factors == num:
#     print(num, "is a Perfect Number")
# else:
#     print(num, "is NOT a Perfect Number")
# decimal to binary , binary to decimal
# num = int(input("Enter decimal number: "))
# original = num
# binary = ""

# while num > 0:
#     remainder = num % 2
#     binary = str(remainder) + binary
#     num //= 2

# print("Binary of", original, "=", binary)
# num = int(input("Enter a number: "))

# num = int(input("Enter a number: "))

# i = 2
# while i < num:
#     if num % i == 0:
#         print("Not prime")
#         break
#     i += 1
# else:
#     print("Prime")


# n = int(input("enter "))
# i = 2 
# while (i < n):
#     if(n%i==0):
#         print("not prime")
#         break
#     else:
#         print("prime")
#         break
#     i+=1



# a = int(input("Enter number: "))
# b = int(input("Enter power: "))

# result = 1
# i = 0

# while i < b:
#     result = result * a
#     i += 1

# print(result)

# x,y = input("enter two values: ").split()
# print(x)
# print(y)
# 
# n = 4
# for row in range(1,n+1):
#     for col in range(1,row+1):
#       if(col == 1 or col == row or row == n):
#         print("*",end=' ')
#       else:
#         print(" ",end=' ')
#     print()
# n = 4
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()
# n = 4
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if(row == 1 or col == 1 or col == 4 or row == 4):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n = 4
# for row in range(1,n+1):
#     for col in range(1,row+1):
#       if(col == 1 or col == row or row == n):
#         print("*",end=' ')
#       else:
#         print(" ",end=' ')
#     print()
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# sum = num1 + num2 
# print(sum)
# diff = num1 - num2
# print(diff)
# product = num1 * num2
# print(product)
# divsion = num1/num2
# print(divsion)
# a = int(input("enter a number: "))
# if(a % 2 == 0):
#     print("even")
# else:
#     print("odd")
# 90+ → A  
# 75–89 → B  
# 60–74 → C  
# 33–59 → D  
# <33 → Fail
# marks = int(input("enter your marks: "))
# if(marks >= 90):
#     print("A")
# elif(marks >= 75):
#     print("B")
# elif(marks >= 60):
#     print("C")
# elif(marks >= 33):
#     print("D")
# else:
#     print("fail")
# for i in range(1,11):
#     print(i,end=' ')
# n = int(input("enter number: "))
# i = 1
# while(i <= 10):
#     print(n,"*",i,'=',n*i)
#     i += 1
# n = int(input("enter number: "))
# if(n > 0):
#     print("positive")
# elif(n == 0):
#     print("zero")
# else:
# #     print("negative")
# age = int(input("enter your age: "))
# if(age < 13):
#     print("child")
# elif(age <= 19):
#     print("teen")
# elif(age <= 59):
#     print("adult")
# else:
#     print("seniour")
# reverse number
# num = int(input("enter your number: "))

# rev = 0
# while(num > 0):
#     last = num % 10
#     rev = rev*10+last
#     num = num//10
#     print(rev)
# n = 5

# for i in range(1, n + 1):
#     # Print spaces
#     print(" " * (n - i), end="")
    
#     # Print stars
#     print("*" * (2*i - 1))
# s = "hello world"
# print(s[0:6])
# s = input("enter string: ")
# print(s[1:-1])
# s = 'pythonprogramming'
# print(s[:6])
# print(s[6:])
# s = input("enter a string: ")
# print(s[0::2])
# s = input('enter string')
# print(s[1::2])
# s = "LearningPython"
# print(s[-6:])      # Python
# s = input("enter string: ")
# mid = len(s) // 2
# print(s[:mid])
# print(s[mid:])

# Variables + Input ka basic code
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print("Hello,", name)
# print("You are", age, "years old.")

# If–Else even/odd code
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# Loops ka simple example
# for i in range(1, 6):
#     print("Counting:", i)

# Basic Function example
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

