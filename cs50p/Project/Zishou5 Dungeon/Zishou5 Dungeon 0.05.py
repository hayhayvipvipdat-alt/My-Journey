#Spells

def nothing(player, enemies):
    return player, enemies

def fireball(player, enemies):
    print('-' * 5)
    print("As you channel your magic, they only get to look.")
    print('-' * 5)
    damage = 30
    for enemy in enemies:
        enemy['hp'] -= damage
        print(f"Your attack connected ! It hit for {damage} damage !")
    print('-' * 5)
    print("It just that cool isn't it ?")
    print("Your fire consume the whole room, blazzing everything in sigh !")  
    print('-' * 5)  
    for enemy in enemies:
        print(f"{enemy['name']}'s hp remaining is: {enemy['hp']}!")
    return player, enemy['hp']

def attack(player, enemies):
    enemy = pick_enemy(enemies)
    print('-' * 5)
    print(player['hit'])
    print('-' * 5)
    damage = 15
    enemy['hp'] -= damage
    print(f"Your attack connected ! It hit for {damage} damage !")
    print('-' * 5)
    print("Melee wasn't your cup of tea, but a wand is as good as any stick !")
    print(f"{enemy['name']}'s hp remaining is: {enemy['hp']}!")
    return player, enemy['hp']

#Inventory

def potion(player, enemies):
    if ipotion['flag'] == True:
        print('-' * 5)
        print("You remembered yourself used it earlier. Now it just a hole in your backpocket.")
        return player, enemies
    heal = 10
    print('-' * 5)
    print("You only got one of these, but it time to use it.")
    player['hp'] += heal
    print(f"That was refreshing ~ You healed for {heal} hp !")
    ipotion['flag'] = True
    return player['hp'], enemies

def firebolt(player, enemies):
    enemy_number = len(enemies)
    dead_enemy = 0
    for enemy in enemies:
        if enemy['hp'] <= 0:
            dead_enemy += 1
    if enemy_number == dead_enemy:
        return nothing
    if ifirebolt['flag'] == True:
        print('-' * 5)
        print("You reached into your pocket..these's nothing there.")
        return player, enemies
    print("You got this from a backstreet store, hope it is a wise decision.")
    enemy = pick_enemy(enemies)
    damage = 10
    enemy['hp'] -= damage
    print('-' * 5)
    print(f"You throw the bottle ! The stuff spread quickly !")
    print(f"It hit for {damage} damage !")
    ifirebolt['flag'] = True
    return player, enemy['hp']

def pick_item(inventory):
    all_item = len(inventory)
    used_item = 0
    for item in inventory:
            if item['flag']:
                used_item += 1
    if all_item == used_item:
        return nothing
    while True:
        print('-' * 5)
        x = input("Wanna use item ? y/n ").strip().lower()
        while x not in ["y", "n", "yes", "no"]:
            print('-' * 5)
            print("just answer me ~")
            x = input("Wanna use item ? y/n ").strip().lower()
        if x in ["n", "no"]:
            return nothing
        if x in ["y", "yes"]:
            print('-' * 5)
            for number, item in enumerate(inventory):
                if item['flag'] == False:
                    print(number + 1,"-", item['name'])
            try:
                answer = int(input("Which one ? enter a number: "))
                valid_choice = list(range(1, len(inventory) + 1))
            except ValueError:
                print('-' * 5)
                print("Pick the enemy number dude ~")
                continue
            while answer not in valid_choice:
                print('-' * 5)
                print("Huh, don't be lazy like that ~")
                for number, item in enumerate(inventory):
                    if item['flag'] == False:  
                        print(number + 1,"-", item['name'])
                answer = int(input("Which one ?"))
            return inventory[answer - 1]['use']
    
    
ipotion = {
     "name": "A fucking potion",
     "flag": False,
     "use": potion
}


ifirebolt = {
     "name": "A bottle of red gooey liquid",
     "flag": False,
     "use": firebolt
}

inventory = [ipotion, ifirebolt]

# Stats for stuff here 

warrior = {
    "name": "Cave man",
    "hp":20,
    "action": {
        "attack",
        "bigbonk"
    },
    "win": "It just another exercise for you !",
    "lost": "You got a cramped today. .",
    "hit": "All that training .. time to prove yourself !!"
}

mage = {
    "name": "Mana Vomiter",
    "hp":10,
    "mana":6,
    "action": {
        "attack": attack,
        "fireball": fireball,
    },
    "win": "It shouldn't be this easy . . according to your calculation ofcourse.",
    "lost": "Outdated data . .",
    "hit": "C'mon, it will work this time !!"
}

skeleton = {
    "name": "Bone Man",
    "hp":30,
    "attack":1,
    "taunting": "I got a bone to pick with ya ~~",
    "hit": "A slash of shining metal slice barely pass you.",
    "dead": "He got no more bone to pick with you. .",
    "S-dead": "Just another pile of bones."
}

weird_man = {
    "name": "A tall man, wearing a chef hat",
    "hp":60,
    "attack":4,
    "tauting": "Huh.. you make a good soup alright. . COME HERE ~~",
    "hit": "His attack aim to chopped of your limbs.",
    "dead": "It shouldn't have ended like this. .",
    "S-dead": "The chef hat lying on the ground."
}

slime = {
    "name": "Slimy Ball",
    "hp":20,
    "attack":1,
    "taunting": "The gooey ball seem exited to meet you.",
    "hit": "It tried to hug you, but can't",
    "dead": "You kill the poor thingy. .",
    "S-dead": "A gooey puddle of liquid."
}

# Navigation

def location(x):
    dungeon = x
    print('-' * 5)
    for place in dungeon:
        print("-", place)
    print('-' * 5)
    answer = input("Where next ?").strip().lower()
    while answer not in x:
        print('-' * 5)
        print("Wasting your time is fine, but just not now.")
        print('-' * 5)
        for place in dungeon:
            print("-", place)
        answer = input("Where next ?").strip().lower()
    return answer

#Class selection

def class_select(question):
    print('-' * 5)
    answer = input(question).strip().lower()
    while answer not in ["warrior", "mage"]:
        print('-' * 5)
        print("You better than this . .")
        answer = input(question).strip().lower()
    if answer == "mage":
        return mage
    elif answer == "warrior":
        return warrior

#Start of the game  

def intro():
    print('-' * 5)
    print("You on time . . get in before you collapse kid.")
    print("Stand before you is a huge grey stone door, the more you look at it, the more unsettling it become . . ")

intro()
player = class_select("Warrior ? or those disgusting mage ? ")

#Combat

def pick_enemy(enemies):
    while True:
        print('-' * 5)
        for number, enemy in enumerate(enemies):
            if enemy['hp'] > 0:
                print(number + 1,"-", enemy['name'])
        try:
            answer = int(input("Who first ? enter a number: "))
            valid_choice = list(range(1, len(enemies) + 1))
        except ValueError:
            print('-' * 5)
            print("Pick the enemy number dude ~")
            continue
        while answer not in valid_choice:
            print("Huh, don't be lazy like that ~")
            for number, enemy in enumerate(enemies):
                if enemy['hp'] > 0:
                    print(number + 1,"-", enemy['name'])
            answer = int(input("Who first ?"))
        return enemies[answer - 1]
   
def combat_command(player):
    skill = player['action']
    print('-' * 5)
    print("What you want to do ?")
    for action in skill:
        print("-", action)
    print('-' * 5)
    action = input("").strip().lower()
    while action not in player['action']:
        print('-' * 5)
        print("You better than this . .")
        print('-' * 5)
        print("What you want to do ?")
        for action in skill:
            print("-", action)
        action = input("").strip().lower()
    return action

def player_turn(player, enemies):
    answer = combat_command(player)
    player['action'][answer](player, enemies)
    pick_item(inventory)(player, enemies)
    return player, enemies

def enemy_turn (player, enemy):
    if enemy['hp'] <= 0:
        print('-' * 5)
        print(enemy['S-dead'])
        return player['hp']
    damage = enemy['attack']
    player['hp'] -= damage
    if player['hp'] > 0:
        print('-' * 5)
        print(enemy['hit'])
        print(f"{player['name']}'s hp remaining is: {player['hp']}! it dealt {damage} damage ~")
    else:
        print('-' * 5)
        print(player['lost'])
    return player['hp']

def combat(player, enemies):
    clear = None
    turn = 1
    enemy_number = len(enemies)
    dead_enemy = 0
    while True:
        if dead_enemy == enemy_number:
            clear = "WON"
            return clear
        print("Turn:", turn)
        player_turn(player, enemies)
        dead_enemy = 0
        for enemy in enemies:
            if enemy['hp'] <= 0:
                dead_enemy += 1
                continue
        for enemy in enemies:
            enemy_turn(player, enemy)
        print('-' * 5)
        turn += 1
        if player['hp'] <= 0:
            clear = "LOST"
            break
    return clear

def retry(question):
    answer = input(question).strip().upper()
    while answer not in ["YES", "NO"]:
        print('-' * 5)
        print("You better than this . .")
        answer = input(question).strip().upper()
    if answer == "YES":
        return "YES"
    elif answer == "NO":
        return "NO" 
    
    
#Room

def kitchen(player):
    clear = False
    enemy_list = [weird_man.copy(), slime.copy(), slime.copy()]
    enemies = list(enemy_list)
    print('-' * 5)
    print('A kitchen ? In the middle of this dark dungeon ?')
    print('Suddently you sense a chilling wind slip across your shoulder, weirdly chilling in this unbelievable scenery')
    print('Human. . faces ? everywhere in this kitchen.. you move as yourself try to not step on any of them')
    print('-' * 5)
    print(f"In the far corner near the freezer you saw a strange man!")
    print('What are you doing in my kitchen ? The huge figure ask, hold tightly the kitchen knife in his hand')
    if player == mage:
        print('-' * 5)
        print('A. I try to find another ingredient for my newly made cake, can you help me ?')
        print('B. Not much, just wandering around man, what yo doing there ?')
        print('C. Your face is my ass')
    if player == warrior:
        print('-' * 5)
        print('A. Finding my way out of here, wanna help ?')
        print('B. Who know ? but what are you doing there man ?')
        print('C. Your face is my ass')
    answer = input('').strip().upper()
    if answer not in ['B']:
        print('-' * 5)
        print('The man started to run toward you screaming.. prepare to fight !')
        print(weird_man['tauting'])
        print('-' * 5)
        while True:
            current_player = player.copy()
            enemy_list = [weird_man.copy(), slime.copy(), slime.copy()]
            enemies = list(enemy_list)
            clear = combat(current_player, enemies)
            if clear == "LOST":
                answer = retry("Wanna give it another go ? YES/NO")
                while answer not in ['YES', 'NO']:
                    answer = retry("Wanna give it another go ? YES/NO")
                if answer == "NO":
                    print("Cool, now die bitch !")
                    clear = False
                    break
                elif answer == "YES":
                    continue
            elif clear == "WON":
                print(player['win'])
                clear = True
                break
        return clear, current_player
    else:
        print('-' * 5)
        print("Ho Ho Ho ~ The truth is i just found the perfect spice for ALL of my food, I'm busy")
        print("He disappeared into a huge iron door, it seem to be your only way forward too")
        clear = True
        return clear, player    
   
def room1(player):
    if dungeon_master["boneroom"]['flag']:
        print('-' * 5)
        print("There is not thing here for you to see.")
        print("Still, this is your first room, special isn't it ?")
        clear = True
        return clear, player
    clear = False
    enemy_list = [skeleton.copy(), skeleton.copy()]
    enemies = list(enemy_list)
    for enemy in enemies:
        print('-' * 5)
        print(f"You encounter {enemy['name']}!")
        print(enemy['taunting'])
        print('-' * 5)
    while True:
        current_player = player.copy()
        enemy_list = [skeleton.copy(), skeleton.copy()]
        enemies = list(enemy_list)
        clear = combat(current_player, enemies)
        if clear == "LOST":
            answer = retry("Wanna give it another go ? YES/NO")
            while answer not in ['YES', 'NO']:
                answer = retry("Wanna give it another go ? YES/NO")
            if answer == "NO":
                print("Cool, now die bitch !")
                clear = False
                break
            elif answer == "YES":
                continue
        elif clear == "WON":
            print(player['win'])
            clear = True
            break
    return clear, current_player

def room2(player):
    if dungeon_master["boneroom2"]['flag']:
        print('-' * 5)
        print("There is not thing here for you to see.")
        print("but it your second room thou, sadly.")
        clear = True
        return clear, player
    clear = False
    enemy_list = [skeleton.copy(), slime.copy()]
    enemies = list(enemy_list)
    for enemy in enemies:
        print('-' * 5)
        print(f"You encounter {enemy['name']}!")
        print(enemy['taunting'])
        print('-' * 5)
    while True:
        current_player = player.copy()
        enemy_list = [skeleton.copy(), slime.copy()]
        enemies = list(enemy_list)
        clear = combat(current_player, enemies)
        if clear == "LOST":
            answer = retry("Wanna give it another go ? YES/NO")
            while answer not in ['YES', 'NO']:
                answer = retry("Wanna give it another go ? YES/NO")
            if answer == "NO":
                print("Cool, now die bitch !")
                clear = False
                break
            elif answer == "YES":
                continue
        elif clear == "WON":
            print(player['win'])
            clear = True
            break
    return clear, current_player

#Map (Kinda)

dungeon_master = {
    "zeroroom": {
        "path": { "boneroom", "zeroroom" },
    },
    "boneroom": {
        "path": { "boneroom", "boneroom2" },
        "room": room1,
        "flag": False,
    },
    "kitchen": {
        "path": { "boneroom2", "kitchen" },
        "room": kitchen,
        "flag": False,
        "fight": False
    },
    "boneroom2": {
        "path": { "boneroom", "boneroom2", "kitchen" },
        "room": room2,
        "flag": False,
    },

}

#The real game

def game(player):
    current_location = dungeon_master["zeroroom"]['path']
    while True:
        if dungeon_master["kitchen"]['flag']:
            print('-' * 5)
            print("That's it, I still planted for more stuff but that's all for now, thanks for playing")
            return player
        print('-' * 5)
        print("As you stand in this cold dark room, there is only one way forward.")
        answer = location(current_location) 
        current_location = dungeon_master[answer]['path']
        dungeon_master[answer]['flag'], player = dungeon_master[answer]['room'](player)
game(player)