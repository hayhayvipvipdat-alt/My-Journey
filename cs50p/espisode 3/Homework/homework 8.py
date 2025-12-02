# First game baby !!!!!!!
print("Welcome to Zishou 5! Make your way in ?")
choice = input("Choose YES/NO: ").strip().upper()

player_class = None
Heath = 0
# Warrior class
Warrior_heath = 10
Counter = 10
Warrior_attack = 15
# Mage class
Mage_heath = 7
Fireball = 20
Mage_attack = 8
Mana = 6 
#Enemy
Ske_heath = 20

he_is_here = 0
he_death = False
ready = False


while choice not in ["YES", "NO"]:
    print("He is coming, make your choice !")
    choice = input("Choose YES/NO: ").strip().upper()
    he_is_here += 1
    if he_is_here == 2:
        print("-" * 5)
        print("Like a flash, you saw your whole life rewind before your eyes as you watches your neck without a head")
        print("ENDING: Wrong turn.")
        he_death = True
        break
if "YES" in choice:
    print("-" * 5)
    print("Good, now who are you ?")
    print("Warrior or a weak disgusting Mage ?")
    x = input("What are you ? ").strip().upper()
    if x == "WARRIOR":
        print("-" * 5)
        player_class = "WARRIOR"
        heath = player_class
        print("Your class is: ", player_class)
        ready = True
    elif x == "MAGE":
        print("-" * 5)
        player_class = "MAGE"
        heath = player_class
        print("Your class is: ", player_class)
        ready = True
    else:
        print("-" * 5)
        print("By the dungeon door, people spotted foul smell reeked the air, as if something is burning and decaying as the same time.")
        print("-" * 5)
        print("ENDING: Don't make unknow entity angry.")
elif he_death == True:
    print("-" * 5)
    print("Later, people rumor that a corpse have been found near the dungeon gate, his nail and teeth all getting stolen.")
    print("Another victim failed to enter the dungeon once again.")
else:
    print("-" * 5)
    print("As you turn back, you saw a strange firgure close the gap between you and him in a flash,")
    print("I should've goes inside, you thought as your teeth and nail being pulled violently out of your cold body.")
    print("Game over.")
    print("-" * 5)
    print("ENDING: Hesitated")

# Done setting up, here we go.

command = None
hesitate = 0 

if ready == True:
    print("-" * 5)
    print("Stand before you is a huge stone door, the more you look at it the more settling it become,")
    print("As your passed throught, you felt a freezing wind slip across your shoulder.")
    print("Like a welcome, for what have inside.")
# Direction 
    print("-" * 5)
    print("The room you stand on is empty, but calm, you feel like you can go forward now.")
    he_is_here = 0
    direction = input("Forward ? YES/NO: ").strip().upper()
    while direction not in ["NO", "YES",]:
        print("The more you stand, the colder the wind")
        direction = input("Forward ?").strip().capitalize()
        he_is_here += 1
        if he_is_here == 2:
            print("-" * 5)
            print("Like a flash, you saw your whole life rewind before your eyes as you watches your neck without a head")
            print("ENDING: Wrong turn.")
            break
    if direction == "YES":
        hesitate = 0 
        Ske_heath = Ske_heath() - command()
        print("-" * 5)
        print("You marched onward, you saw a small firgure in the corner of the room.")
        print("A skeleton ! There is no way you can avoid fighting it, prepare to fight !")
        if player_class == "MAGE":
            command = input("Attack ? or Fireball")
            while command not in ["Attack", "Fireball"]:
                print("Quick ! It's coming !")
                hesitate += 1
                command = input("Attack ? or Fireball").strip().capitalize()
                if hesitate == 3:
                    print("It attack connect a landed a critical strike into your skull before you decide to do anything.")
                    print("ENDING: COWARD")
            if command == "Fireball" and Ske_heath == 0:
                print("Wow ! My first win ! I fucking did it !")
                print("You said as you watch the burning bone of your enemy crumble beneath your feet, the smell of victory.")
        elif player_class == "WARRIOR":
            command = input("Attack ? or Counter")
    elif direction == "NO":
        print("-" * 5)
        print("As you turn back, you saw a strange firgure close the gap between you and him in a flash,")
        print("I should've goes inside, you thought as your teeth and nail being pulled violently out of your cold body.")
        print("Game over.")
        print("-" * 5)
        print("ENDING: Hesitated")