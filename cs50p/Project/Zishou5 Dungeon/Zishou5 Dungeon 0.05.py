# Practice combat for more bit
warrior = {
    "name": "Cave man",
    "hp":20,
    "action": {
        "attack":10,
        "bigbonk": 15,
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
        "attack":5,
        "fireball": 200000
    },
    "win": "It shouldn't be this easy . . according to your calculation ofcourse.",
    "lost": "Outdated data . .",
    "hit": "C'mon, it will work this time !!"
}

skeleton = {
    "name": "Bone Man",
    "hp":30,
    "attack":2,
    "taunting": "I got a bone to pick with ya ~~",
    "hit": "A slash of shining metal slice barely pass you.",
    "dead": "He got no more bone to pick with you. ."
}

weird_man = {
    "name": "A tall man, wearing a chef hat",
    "hp":50,
    "attack":4,
    "tauting": "Huh.. you make a good soup alright. . COME HERE ~~",
    "hit": "His attack aim to chopped of your limbs.",
    "dead": "It shouldn't have ended like this. ."
}

map = {
        "startingroom",
        "boneroom" 
    }

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

def combat_command (player):
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
    return player['action'][action]

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
    
def intro():
    print('-' * 5)
    print("You on time . . get in before you collapse kid.")
    print("Stand before you is a huge grey stone door, the more you look at it, the more unsettling it become . . ")

intro()
player = class_select("Warrior ? or those disgusting mage ?")
   
def combat_command (player):
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
    return player['action'][action]

def player_turn (player, enemy):
    damage = combat_command(player)
    enemy['hp'] -= damage
    if enemy['hp'] > 0:
        print('-' * 5)
        print(player['hit'])
        print(f"Your attack connected ! It hit for {damage} damage !")
        print(f"{enemy['name']}'s hp remaining is: {enemy['hp']}!")
    else:
        print('-' * 5)
        print(enemy['dead'])
    return enemy['hp']

def enemy_turn (player, enemy):
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

def combat(player, enemy):
    clear = None
    turn = 1
    while True:
        print("Turn:", turn)
        player_turn(player, enemy)
        if enemy['hp'] <= 0:
            clear = "WON"
            break
        enemy_turn(player, enemy)
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
    

def kitchen(player):
    clear = False
    death = False
    if death == True:
        print("You fucking CAN'T did it. . ")
        return clear, player
    enemy = weird_man.copy()
    print('A kitchen ? In the middle of this dark dungeon ?')
    print('Suddently you sense a chilling wind slip across your shoulder, weirdly chilling in this unbelievable scenery')
    print('Human. . faces ? everywhere in this kitchen.. you move as yourself try to not step on any of them')
    print('-' * 5)
    print(f"In the far corner near the freezer you saw a {enemy['name']}!")
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
        dungeon_master["kitchen"]['fight'] = True
        print('-' * 5)
        print('The man started to run toward you screaming.. prepare to fight !')
        print(enemy['tauting'])
        while True:
            enemy = weird_man.copy()
            clear = combat(player, enemy)
            if clear == "LOST":
                answer = retry("Wanna give it another go ? YES/NO")
                if answer == "NO":
                    print("Cool, now die bitch !")
                    death = True
                    clear = False
                    break
            elif clear == "WON":
                print('-' * 5)
                print(player['win'])
                clear = True
                break
        return clear, player
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
    death = False
    if death == True:
        print("You fucking CAN'T did it. . ")
        return clear, player
    enemy = skeleton.copy()
    print('-' * 5)
    print(f"You encounter {enemy['name']}!")
    print('-' * 5)
    print(enemy['taunting'])
    while True:
        enemy = skeleton.copy()
        clear = combat(player, enemy)
        if clear == "LOST":
            answer = retry("Wanna give it another go ? YES/NO")
            if answer == "NO":
                print("Cool, now die bitch !")
                death = True
                clear = False
                break
        elif clear == "WON":
            print('-' * 5)
            print(player['win'])
            clear = True
            break
    return clear, player

def room2(player):
    if dungeon_master["boneroom2"]['flag']:
        print('-' * 5)
        print("There is not thing here for you to see.")
        print("Still, this is your first room, special isn't it ?")
        clear = True
        return clear, player
    clear = False
    death = False
    enemy = skeleton.copy()
    print('-' * 5)
    print('Fuck ! Another skeleton, again ??')
    if death == True:
        print("You fucking CAN'T did it. . ")
        return clear, player
    print(f"You encounter {enemy['name']}!")
    print('-' * 5)
    print(enemy['taunting'])
    while True:
        enemy = skeleton.copy()
        clear = combat(player, enemy)
        if clear == "LOST":
            answer = retry("Wanna give it another go ? YES/NO")
            if answer == "NO":
                print("Cool, now die bitch !")
                death = True
                clear = False
                break
        elif clear == "WON":
            print('-' * 5)
            print(player['win'])
            clear = True
            break
    return clear, player

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

def game(player):
    current_location = dungeon_master["zeroroom"]['path']
    while True:
        print('-' * 5)
        print("As you stand in this cold dark room, there is only one way forward.")
        answer = location(current_location) 
        current_location = dungeon_master[answer]['path']
        dungeon_master[answer]['flag'], player = dungeon_master[answer]['room'](player)
game(player)