# First game baby !!!!!!!
print("Welcome to Zishou 5! Make your way in ?")
choice = input("Choose YES/NO: ").strip().upper()

player_class = None
Heath = 0
# Warrior class
Warrior_heath = 10
Big_Bonk = 15
Warrior_attack = 10
# Mage class
Mage_heath = 7
Fireball = 20
Mage_attack = 8
Mana = 6 
#Enemy
Ske_heath = 15
Ske_attack = 1

he_is_here = 0
he_death = False
ready = False

while True:
    while  choice not in ["YES", "NO"]:
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
            break
        elif x == "MAGE":
            print("-" * 5)
            player_class = "MAGE"
            heath = player_class
            print("Your class is: ", player_class)
            ready = True
            break
        else:
            print("-" * 5)
            print("By the dungeon door, people spotted foul smell reeked the air, as if something is burning and decaying as the same time.")
            print("-" * 5)
            print("ENDING: Don't make unknow entity angry.")
    elif he_death == True:
        print("-" * 5)
        print("Later, people rumor that a corpse have been found near the dungeon gate, his nail and teeth all getting stolen.")
        print("Another victim failed to enter the dungeon once again.")
        break
    else:
        print("-" * 5)
        print("As you turn back, you saw a strange firgure close the gap between you and him in a flash,")
        print("I should've goes inside, you thought as your teeth and nail being pulled violently out of your cold body.")
        print("Game over.")
        print("-" * 5)
        print("ENDING: Hesitated")
        break

# Done setting up, here we go.

command = None
hesitate = 0 
damage = 0
death = False
room1_clear = False
# Skeleton room
while True:
    if room1_clear:
        break
    if death == True:
        print("-" * 5)
        print("Keep going ? She is waiting for you still . .")
        retry = input("YES/NO ? ").strip().upper()
        if retry == "YES":
            death = False
            continue
        elif retry == "NO":
            print("Fine.")
            print("ENDING: FORGOTTEN")
            break
        else: 
            print("-" * 5)
            print("By the dungeon door, people spotted foul smell reeked the air, as if something is burning and decaying as the same time.")
            print("-" * 5)
            print("ENDING: Don't make unknow entity angry.")
    while ready and death == False:
        if room1_clear:
            break   
        print("-" * 5)
        print("Stand before you is a huge stone door, the more you look at it the more settling it become,")
        print("As your passed throught, you felt a freezing wind slip across your shoulder.")
        print("Like a welcome, for what have inside.")
        print("-" * 5)
        print("The room you stand on is empty, but calm, you feel like you can go forward now.")
        he_is_here = 0
        direction = input("Forward ? YES/NO: ").strip().upper()
        Ske_heath = 15
        mana = 6
        while direction not in ["NO", "YES",]:
            print("-" * 5)
            print("The more you stand, the colder the wind")
            direction = input("Forward ?").strip().upper()
            he_is_here += 1
            if he_is_here == 2:
                print("-" * 5)
                print("Like a flash, you saw your whole life rewind before your eyes as you watches your neck without a head")
                print("ENDING: Wrong turn.")
                death = True
                break
        if direction == "YES":
            hesitate = 0 
            print("-" * 5)
            print("You marched onward, you saw a small firgure in the corner of the room.")
            print("A skeleton ! There is no way you can avoid fighting it, prepare to fight !")
            print(Ske_heath)
            #Turn-based while:
            while Ske_heath > 0:
                if player_class == "MAGE":
                    command = input("Attack ? or Fireball ? ").strip().upper()
                    while command not in ["ATTACK", "FIREBALL"]:
                        print("Quick ! It's coming !")
                        hesitate += 1
                        command = input("Attack ? or Fireball ? ").strip().upper()
                        if hesitate == 2:
                            print("-" * 5)
                            print("It attack connect a landed a critical strike into your skull before you decide to do anything.")
                            print("ENDING: COWARD")
                            death = True
                            Ske_heath = 0
                            room1_clear = False
                            break
                    if command == "FIREBALL":
                        damage = Fireball
                        Mana -= 2
                        Ske_heath -= damage
                        if Ske_heath <= 0:
                            print("-" * 5)
                            print("Holy fuck ! I did it !")
                            print("You scream the cry of vitory as the smell the bone of your enemy burning in flame.")
                            death = False
                            room1_clear = True
                            break
                        elif Ske_heath > 0:
                            print("-" * 5)
                            print("Your attack laned, but your enemy still moving !")
                            print("It hit back ! You barely dodge it..")
                            Mage_heath -= Ske_attack
                            continue
                    if command == "ATTACK":
                        damage = Mage_attack
                        Ske_heath -= damage
                        if Ske_heath <= 0:
                            print("-" * 5)
                            print("Your battle was hard fought.")
                            print("Sweat cover your whole body and dagger as the sensation of victory running throught your body rightfully so.")
                            death = False
                            room1_clear = True
                            break
                        elif Ske_heath > 0:
                            print("-" * 5)
                            print("You tried, but your enemy still survive.")
                            print("It hit back ! You barely dodge it..")
                            Mage_heath -= Ske_attack
                            continue                                  
                if player_class == "WARRIOR":
                    command = input("Attack ? or Bigbonk ? ").strip().upper()
                    while command not in ["ATTACK", "BIGBONK"]:
                        print("-" * 5)
                        print("Quick ! It's coming !")
                        hesitate += 1
                        command = input("Attack ? or Counter ? ").strip().upper()
                        if hesitate == 2:
                            print("-" * 5)
                            print("It attack connect a landed a critical strike into your skull before you decide to do anything.")
                            print("ENDING: COWARD")
                            death = True
                            Ske_heath = 0
                            room1_clear = False
                            break
                    if command == "ATTACK":
                        damage = Warrior_attack
                        Ske_heath -= damage
                        if Ske_heath <= 0:
                            print("-" * 5)
                            print("Hooo Weee ! That's how I do stuff babe !")
                            print("It's was a good exercise for just you.")
                            death = False
                            room1_clear = True
                            break
                        elif Ske_heath > 0:
                            print("-" * 5)
                            print("Your attack landed, but your enemy still moving !")
                            Warrior_heath -= Ske_attack
                            continue
                    if command == "BIGBONK":
                        damage = Big_Bonk
                        Ske_heath -= damage
                        if Ske_heath <= 0:
                            print("-" * 5)
                            print("Your battle was hard fought.")
                            print("Sweat cover your whole body and dagger as the sensation of victory running throught your body, rightfully so.")
                            death = False
                            room1_clear = True
                            break
                        elif Ske_heath > 0:
                            print("-" * 5)
                            print("You tried, but your enemy still survive.")
                            Warrior_heath -= Ske_attack
                            continue
        if direction == "NO":
            print("-" * 5)
            print("Like a flash, you saw your whole life rewind before your eyes as you watches your neck without a head")
            print("ENDING: Wrong turn.")
            death = True
            break