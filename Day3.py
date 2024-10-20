#print("Even or odd")
#number_1=int(input("insert one number"))
#result= number_1%2
#if result==0:
#    print("your number is even")
#else:
#    print("your number is odd")

# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print("You are underweight")
# elif bmi <= 24.9:
#     print ("you are normal")
# else:
#     print ("you are overweight")

# print("Welcome to pypizza deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese= input("Do you want extra cheese? Y or N: ")
# prize=0
# if size == "S":
#     prize=15
#     if pepperoni == "Y":
#         prize+=2    
# elif size== "M":
#     prize=20
#     if pepperoni == "Y":
#         prize+=3      
# else: 
#     prize=25
#     if pepperoni == "Y":
#         prize+=2
    
#     if extra_cheese== "Y":
#         prize+=1;   
# print(f"Your total is: ${prize}")    
       
print('''                   ,,__
           ..  ..   / o._)                   .---.
          /--'/--\  \-'||        .----.    .'     '.
         /        \_/ / |      .'      '..'         '-.
       .'\  \__\  __.'.'     .'          i-._
         )\ |  )\ |      _.'
        // \\ // \\
       ||_  \\|_  \\_
   mrf '--' '--'' '--''')
print("Welcome to treeasure Sahara \n Your mission is find the treasure. \n You're on a cross road what do you select?")
Direction= input("Select right or left ")
if Direction == "right":
    Oasis= input ("You found and Oasis select stay or walk ")
    print("Oasis")
    if Oasis == "stay":
        print("A camel arrive and go with you to the ruins. ")
        ruins = input("In the ruins are 3 doors what do you selct? 1, 2 or 3 ")
        if ruins == "1":
            print("The snakes killed you. Game over.")
        elif ruins == "2":
            print("You found the treasure. Congratulations!")
        else:
            print("You fall in a hole. Game over.")
    else:
        print("You die because dehydration. Game over.")
else:
    print("You are lost in the desert. Game over.")