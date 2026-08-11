print("Welcome to my First game")
print(input("What is your name?"))
aggey = int(input("What is your age?"))
print(aggey)
health = 10

if aggey >= 18:
    print("You are old enough to play this game")

    wants_to_play = input("Do you want to play? (yes/no)").lower()
    if wants_to_play == "yes":
        print("You are starting with {} health".format(health))
        print("Let's play!")

        left_and_right = input("First choice... Left or Right (left/right)?").lower()
        if left_and_right == "left":
            ans = input("Nice, you follow the path and reach a lake...   Do you want to swim across or go around (across/around)?").lower()

            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health")
                health -= 5
            ans = input("You notice a house and a river. Which do you go to (house/river)?").lower()
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

            if health <= 0:
                print("You now have 0 health and you lost the game")
            else:
                print("You survived and have {} health left".format(health))

        elif left_and_right == "right":
            print("You fell down and lost")
    
    elif wants_to_play == "no":
        print("GoodbyeJake")




else:
    print("Sorry you are not old enough to play this game")
