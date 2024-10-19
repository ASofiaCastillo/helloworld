#contar=len("hellos")
#print("hellos"[contar-1])
#debug=len("12345")
#print(debug)
#print(type ("Hola"))
#print(type (123_456))
#print(type (3.1415))
#print(type (True))
#print("Number of letters in your name:"+ str(len(input("What's your name?"))))
#height = 1.65 
#weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
#bmi = 84/(1.65**2)

#print(bmi)

print("Welcome to the tip calculator! \n")
total_bill=float(input("What was the total bill? $ \n"))
tip=float(input("How much tip would you like to give? 5, 15 or 20 \n"))
total_people=float(input("How many people to split the bill? \n"))
total= round((total_bill*tip/100+total_bill)/total_people, 2)
print(f"Each person should pay: {total}")
