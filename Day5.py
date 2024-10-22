# students_score = [100, 98, 95, 72, 5, 48, 52, 369, 244, 258,  2, 524, 5, 54, 25, 25, 14, 159, 258, 105]

# for maxim in students_score:
#     if maxim == max(students_score):
#         print(maxim)
# sum=0
# for number in range (1, 101):
#     sum+=number
# print(sum)
# valor=0

# for number in range (1,101):
#     valor=number
#     if valor%3==0:
#         print("Fizz")
#     elif valor%5==0:
#         print("Buzz")
#     elif valor%3==0 and valor%5==0:
#         print("FizzBuzz")
#     else:
#         print(valor)
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
 
 
password= []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for letter in random.sample(letters, nr_letters):
        password.append(letter)
for symbol in random.sample(symbols, nr_symbols):
        password.append(symbol)
for number in random.sample(numbers, nr_numbers):
        password.append(number)    
print(password) 
print(random.sample(password, len(password)))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passw = ""
for without_list in password:
    passw += without_list
print(f"Your Password is:{passw}")
