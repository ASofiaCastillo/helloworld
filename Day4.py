import random
# head_tail=random.randint(1,2)

# if head_tail== 1:
#     print("Head")
# else:
#     print("Tails")
# friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
# friends_random = random.choice(friends)
# print(friends_random)
1


print("Welcome to the game!")
game= input("Select 0 (rock), 1 (Scissors) or 2 (paper) ")
game_selection=random.randint(0,2)
if game=="0":
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
elif game=="1":

    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)    
elif game=="2":
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
else:
    print("Error x.x. Try again with another value")
    
print("computer selection")

if game_selection==0:
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
if game_selection==1:

    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)    
if game_selection==2:
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)

    
if game_selection == 0 and game == "0":
    print("Draw -.- try again.")
elif game_selection == 1 and game == "1":
    print("Draw -.- try again.")
elif game_selection == 2 and game == "2":
    print("Draw -.- try again.")
elif game_selection == 1 and game == "0":
    print("Congrats! You're a winner :D")
elif game_selection == 2 and game == "0":
    print("You're a loser, Keep trying :()")
elif game_selection == 0 and game == "1":
    print("You're a loser, Keep trying :()")
elif game_selection == 0 and game == "2":
    print("Congrats! You're a winner :D")
elif game_selection == 2 and game== "1":
    print("Congrats! You're a winner :D")
else:
    print("You're a loser, Keep trying :()")