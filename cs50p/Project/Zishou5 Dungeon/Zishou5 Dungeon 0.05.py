import random

#Spells

def nothing(player, enemies):
    return player, enemies

def fireball(player, enemies):
    print('-' * 5)
    print("As you channel your magic, they only get to look.")
    print('-' * 5)
    damage = 30
    if player['awaken'] >= 3 and player['awaken'] < 5:
        print('-' * 5)
        print("You no longer as fragile as those mortal.")
        print("No longer have you beg for a place to live !")
        print('-' * 5)
        print("Your fire consume the whole room, blazzing everything in sigh !")
        for enemy in enemies:
            enemy['hp'] -= damage
            print(f"Your attack connected ! It hit for {damage} damage !")
        damage += 10
        player['awaken'] += 1
        return player, enemy['hp']
    if player['awaken'] >= 5:
        print('-' * 5)
        print("No need to pretend anymore.")
        print("Because you are NOT their equal.")
        print('-' * 5)
        print("Multiple blast of infernal run throught the whole room, consume everything in sigh !")
        damage += 10
        for _ in range(3):
            for enemy in enemies:
                enemy['hp'] -= damage
                print(f"Your attack connected ! It hit for {damage} damage !")
        player['awaken'] += 1
        return player, enemy['hp']
    for enemy in enemies:
        enemy['hp'] -= damage
        print(f"Your attack connected ! It hit for {damage} damage !")
    print('-' * 5)
    print("It just that cool isn't it ?") 
    print('-' * 5)
    player['awaken'] += 1
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
    return player, enemy['hp']

#Enemy Spells

def banish(ally, enemy):
    damage = 5
    print('-' * 5)
    print('As following his will, he granted me the power to command the light itself !')
    print('He hold his sword up like a spear, pointing to the sun beyond these stone !')
    print('A burning light ! Pushes down any shadow !')
    for member in ally[:]:
        member['hp'] -= damage
        if member['class'] == "Summon":
            print('-' * 5)
            ally.remove(member)
            print(member['dead'])
        elif member['hp'] > 0:
            print('-' * 5)
            print("It BURNING !")
            print(f"{member['name']}'s hp remaining is: {member['hp']}! it dealt {damage} damage ~")
        else:
            print('-' * 5)
            ally.remove(member)
            print(member['dead'])
    return ally, enemy

def quickjab(ally, enemy):
    damage = enemy['attack']
    target = random.choice(ally)
    print('It nothing personal, really')
    print('He ambush your back in in quick succession of dashes.')
    for _ in range (3):
        target['hp'] -= damage
        if target['hp'] > 0:
            print('-' * 5)
            print('Hit moments only leave a trail of fain light behind each strike !')
            print(f"{target['name']}'s hp remaining is: {target['hp']}! it dealt {damage} damage ~")
    else:
        print('-' * 5)
        ally.remove(target)
        print(target['dead'])
    return ally, enemy

def darkdrain(ally, enemy):
    damage = 5
    heal = 0
    print('-' * 5)
    print("The shadow open it mouth ! Revealed so many teeth that you don't bother checking ~")
    for member in ally[:]:
        member['hp'] -= damage
        heal += 5
        if member['hp'] > 0:
            print('-' * 5)
            print("It sucking the air outside in !")
            print(f"{member['name']}'s hp remaining is: {member['hp']}! it dealt {damage} damage ~")
        else:
            print('-' * 5)
            ally.remove(member)
            print(member['dead'])
    enemy['hp'] += heal
    print(f"The shadow grow stronger and bigger ! it healed {heal} hp !")
    return ally, enemy

def eattack(ally, enemy):
    if not ally:
            print('-' * 5)
            print("There is nothing for them to destroy anymore.")
            return ally, enemy
    damage = enemy['attack']
    target = random.choice(ally)
    target['hp'] -= damage
    if target['hp'] > 0:
        print('-' * 5)
        print(enemy['hit'])
        print(f"{target['name']}'s hp remaining is: {target['hp']}! it dealt {damage} damage ~")
    else:
        print('-' * 5)
        ally.remove(target)
        print(target['dead'])
    return ally, enemy

#Inventory

def potion(player, enemies):
    if ipotion["number"] <= 0:
        print('-' * 5)
        print("You remembered yourself used it earlier. Now it just a hole in your backpocket.")
        return player, enemies
    heal = 10
    print('-' * 5)
    print("You only got one of these, but it time to use it.")
    player['hp'] += heal
    print(f"That was refreshing ~ You healed for {heal} hp !")
    ipotion['number'] -= 1
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
                    print(number + 1,"◈", item['name'], ":", item['number'], "Items")
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
                        print(number + 1,"◈", item['name'])
                answer = int(input("Which one ?"))
            return inventory[answer - 1]['use']
    
    
ipotion = {
     "name": "A fucking potion",
     "flag": False,
     "use": potion,
     "number":1,
}


ifirebolt = {
     "name": "A bottle of red gooey liquid",
     "flag": False,
     "use": firebolt,
     "number":1,
}

inventory = [ipotion, ifirebolt]

# Stats for stuff here 

mage = {
    "class": "player",
    "job": "mage",
    "name": "Mana Vomiter",
    "hp":50,
    "mana":6,
    "awaken":0,
    "attack":0,
    "action": {
        "attack": attack,
        "fireball": fireball,
    },
    "win": "It shouldn't be this easy . . according to your calculation ofcourse.",
    "dead": "Outdated data . .",
    "hit": "C'mon, it will work this time !!"
}

npc_mage = {
    "class": "NPC",
    "name": "Old man with a big hat",
    "skill": {
        "eattack": eattack
    },
    "skillist" : ['eattack'],
    "hp":30,
    "attack":3,
    "taunting": "W-What ? Why are you attack us ?",
    "hit": "Please. . Why are you doing this ?",
    "dead": "You don't have to do this . . we just wanted to get out . .",
    "S-dead": "Just another pile of flesh."
}

npc_warrior = {
    "class": "NPC",
    "name": "Old man with a big axe",
    "skill": {
        "eattack": eattack
    },
    "skillist" : ['ettack'],
    "hp":30,
    "attack":3,
    "taunting": "You will pay for this !!",
    "hit": "Wake the fuck up ! What's wrong with ya ?",
    "dead": "I promised to his wife . . I promised I'll bring hi- . . hom-",
    "S-dead": "Just another pile of flesh."
}

skeleton = {
    "class": "Mob",
    "name": "Bone Man",
    "skill": {
        "eattack": eattack
    },
    "skillist" : ['eattack'],
    "hp":30,
    "attack":2,
    "taunting": "I got a bone to pick with ya ~~",
    "hit": "A slash of shining metal slice barely pass you.",
    "dead": "He got no more bone to pick with you. .",
    "S-dead": "Just another pile of bones."
}

weird_man = {
    "class": "Event",
    "name": "A tall man, wearing a chef hat",
    "skill": {
        "eattack": eattack
    },
    "skillist" : ['eattack'],
    "hp":60,
    "attack":4,
    "taunting": "Huh.. you make a good soup alright. . COME HERE ~~",
    "hit": "His attack aim to chopped off your limbs.",
    "dead": "It shouldn't have ended like this. .",
    "S-dead": "The chef hat lying on the ground."
}

slime = {
    "class": "Mob",
    "name": "Slimy Ball",
    "skill": {
        "eattack": eattack
    },
    "skillist" : ['eattack'],
    "hp":20,
    "attack":1,
    "taunting": "The gooey ball seem exited to meet you.",
    "hit": "It tried to hug you, but can't",
    "dead": "You kill the poor thingy. .",
    "S-dead": "A gooey puddle of liquid."
}

shadow_guardian= {
    "class": "Summon",
    "name": "Shadow Guardian",
    "skill": {
        "eattack": eattack
    },
    "skillist" : ['eattack'],
    "hp":10,
    "attack":15,
    "taunting": "You don't get to see it face, as it giant armor looming over you.",
    "hit": "Direct Stike ! it spear penetrade even the hardest material ! ",
    "dead": "It dissapear into the wind, as quickly as you summon it.",
    "S-dead": "It armor, lying on the ground to remind one who was."
}

shadow = {
    "class": "Summon",
    "name": "Shadow Creature",
    "skill": {
        "eattack": eattack
    },
    "skillist" : ['eattack'],
    "hp":10,
    "attack":1,
    "taunting": "A husk of their formal self, still linger in the mist of darkness",
    "hit": "A flash slash ! Leave a veil of shadow.",
    "dead": "The creature melted into a puddle.",
    "S-dead": "It armor, lying on the ground to remind one who was."
}

#Boss
giant_shadow = {
    "class": "Boss",
    "name": "Shadow Apostle",
    "skill": {
        "eattack": eattack,
        "darkdrain": darkdrain
    },
    "skillist" : ['eattack', 'darkdrain'],
    "hp":150,
    "attack":4,
    "taunting": "His red spiral eyes devouring your soul as he glance toward your direction.",
    "hit": "A powerfull slash ! You barely hold your ground avoid flying far aways !",
    "dead": "The creature turn into some kind of dark liquid, only your shadow puddle remain.",
    "S-dead": "It armor, lying on the ground to remind one who was."
}

myterious_man = {
    "class": "Boss",
    "name": "A man from high above",
    "skill": {
        "eattack": eattack,
        "banish": banish
    },
    "skillist" : ['eattack', 'banish'],
    "hp":150,
    "attack":5,
    "taunting": "Why ? Why is everything so hard the way it is ? I just wanted to undo what I did.",
    "hit": "You ! Get out of my way please !",
    "dead": "He fall to the ground.",
    "S-dead": "Only his sorrow remain."
}

awaken_man = {
    "class": "Boss",
    "name": "A man from high above",
    "skill": {
        "eattack": eattack,
        "quickjab": quickjab,
    },
    "skillist" : ['eattack', 'quickjab'],
    "hp":200,
    "attack":5,
    "taunting": "I understand it now, this is what it meant to move forward !",
    "hit": "If this this the price, you and I will have to pay for it !",
    "dead": "He managed to avoid your strikes and delivery a massive ground slam, as the room dimmed with dust, He escaped.",
    "S-dead": "Only his sorrow remain."
}



# Navigation

def location(x):
    dungeon = x
    print('-' * 5)
    for place in dungeon:
        print("◈", place)
    print('-' * 5)
    answer = input("Where next ?").strip().title()
    while answer not in x:
        print('-' * 5)
        print("Wasting your time is fine, but just not now.")
        print('-' * 5)
        for place in dungeon:
            print("◈", place)
        answer = input("Where next ?").strip().title()
    return answer

#Class selection

def class_select(question):
    print('-' * 5)
    answer = input(question).strip().lower()
    while answer not in ["mage"]:
        print('-' * 5)
        print("You better than this . .")
        answer = input(question).strip().lower()
    if answer == "mage":
        return mage

#Start of the game  

def intro():
    print('-' * 5)
    print("You on time . . get in before you collapse kid.")
    print("Stand before you is a huge grey stone door, the more you look at it, the more unsettling it become . . ")

intro()
player = class_select("Your only chose is mage . . .")
main_party = []

#Combat

def pick_enemy(enemies):
    print('-' * 5)
    while True:
        for number, enemy in enumerate(enemies):
            if enemy['hp'] > 0:
                print(number + 1,"◆", enemy['name'], ":", enemy['hp'], "HP")
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
                    print(number + 1,"◆", enemy['name'])
            answer = int(input("Who first ?"))
        return enemies[answer - 1]
   
def combat_command(player):
    skill = player['action']
    print("What you want to do ?")
    for action in skill:
        print("◈", action)
    print('-' * 5)
    action = input("").strip().lower()
    while action not in player['action']:
        print('-' * 5)
        print("You better than this . .")
        print('-' * 5)
        print("What you want to do ?")
        for action in skill:
            print("◈", action)
        action = input("").strip().lower()
    return action

def player_turn(member, enemies):
    if member['class'] == "player":
        answer = combat_command(player)
        player['action'][answer](player, enemies)
        for enemy in enemies[:]:
            if enemy['hp'] <= 0:
                print(enemy['dead'])
                enemies.remove(enemy)
        pick_item(inventory)(player, enemies)
        print("")
        print("=" * 5, "Your allies Follow", "=" * 5)
    else:
        if not enemies:
            print('-' * 5)
            print("There is nothing for your ally to do now.")
            return member, enemies
        else:
            damage = member['attack']
            target = random.choice(enemies)
            target['hp'] -= damage
            print('-' * 5)
            print(member['hit'])
            print(f"{target['name']}'s hp remaining is: {target['hp']}! it dealt {damage} damage ~")
            if target['hp'] <= 0:
                enemies.remove(target)
                print('-' * 5)
                print(target['dead'])
    return member, enemies

def enemy_turn (main_party, enemy):
    if enemy['hp'] <= 0:
        print('-' * 5)
        print(enemy['S-dead'])
        return player['hp']
    spell = random.choice(enemy['skillist'])
    enemy['skill'][spell](main_party, enemy)
    return main_party, enemy

def combat(player, main_party, enemies, room_actor):
    while True:
        clear = None
        turn = 1
        current_player = player.copy()
        current_enemies = []
        for enemy in enemies:
            current_enemies.append(enemy.copy())
        main_party = []
        main_party.insert(0, current_player)
        for actor in room_actor:
            main_party.append(actor)
        for enemy in current_enemies:
            print("✮")
            print(f"You encounter {enemy['name']}!")
            print("-", enemy['taunting'])
        print('-' * 5)
        while True:
            print("=" * 19)
            print("Your Party:")
            for member in main_party:
                print("◈", member['name'], ":", member['hp'], "HP")
            print("-" * 5, "VS", "-" * 5)
            print("Their:")    
            for enemy in current_enemies:
                print("◇", enemy['name'], ":", enemy['hp'], "HP") 
            print("=" * 5, "Turn:", turn, "=" * 5)
            for member in main_party:
                player_turn(member, current_enemies)
            if not current_enemies:
                clear = "WON"
                return clear, main_party[0]
            print("")
            print("")
            print("=" * 5, "Their Actions", "=" * 5)
            for enemy in current_enemies:
                enemy_turn(main_party, enemy)
            print('-' * 5)
            turn += 1
            if not main_party:
                clear = "LOST"
                break
        if clear == "LOST":
            answer = retry("Wanna give it another go ? YES/NO")
            while answer not in ['YES', 'NO']:
                answer = retry("Wanna give it another go ? YES/NO")
            if answer == "NO":
                print('-' * 5)
                print("Cool, now die bitch !")
                clear = False
                return clear, player
            elif answer == "YES":
                clear = None
                continue
        
        
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

def gate(player):
    if dungeon_master["Gate"]['flag']:
        print("=" * 5, "Cleared", "=" * 5)
        print("You can't return.")
        print("It is your own decision after all.")
        clear = True
        return clear, player
    clear = False
    room_actor = []
    if dungeon_master['Kitchen']['fight'] == False:
        room_actor.append(weird_man.copy())
    enemies = [myterious_man.copy()]
    clear, player = combat(player, main_party, enemies, room_actor)
    not_yet = 0
    if clear:
        while True:
            for enemy in enemies:
                enemy['hp'] = 1
                enemy['taunting'] = "Not yet, I still haven't done yet.."
            clear , player = combat(player, main_party, enemies, room_actor)
            not_yet += 1
            if not_yet == 3:
                enemies = [awaken_man.copy()]
                clear, player = combat(player, main_party, enemies, room_actor)
                return clear, player
    return clear, player

def survivor(player):
    if dungeon_master["Treasure"]['flag']:
        print("=" * 5, "Cleared", "=" * 5)
        print("They all gone.")
        print("But you still remember what you did.")
        clear = True
        return clear, player
    clear = False
    print('-' * 5)
    print('Before entering the room, you heard a big explosion.')
    print('"Hey ! You ! move behind it while we lure all of them upfront, try to sneak them ! Hurry !"')
    print('-' * 5)
    print('A group of explorer try to fight againt a giant shadow creature wearing armor.')
    print('"Cmon new guy, helping us out here ~ This fucker really not wanting to roll over"')
    print('-' * 5)
    print('A. Sure ! Try lure him ~ I will fireball this fucker.')
    print('B. Why should I not fireball YOU right now ?')
    print("C. All I can hear is that's YOUR problem")
    if dungeon_master['Kitchen']['fight'] == False:
        print('D. Yo chef, help us man !')
    print('-' * 5)
    print("The giant shadow creature alone is already dangerous, but the room also fill with small shadow figure too.")
    print("Will you trust those stranger, whose you just had met your life ? made your choice wisely . .")
    answer = input('What is your answer ? ').strip().upper()
    while answer not in ["A", "B", "C", "D"]:
        print("Are you always this uninteresting ?")
        answer = input('What is your answer ? ').strip().upper()
    if answer in ["A", "D"]:
        print('-' * 5)
        room_actor = [npc_mage.copy(), npc_warrior.copy()]
        if answer == "D":
            room_actor.append(weird_man.copy())
        enemies = [giant_shadow.copy()]
        print("As they manage to lure the giant creature atention . .")
        if player['job'] == "mage":
            damage = 30
            print("You channel your wand, energy and space bend to your will !")
            print('-' * 5)
            print("Fire BALL !!!! You scream, as your greatest fireball yet fire on it direction !")
            print(f"Your attack connected ! It burning everything for {damage} damage !")
            print('-' * 5) 
            for enemy in enemies:
                enemy['hp'] -= damage
                print(f"{enemy['name']}'s hp remaining is: {enemy['hp']}!")
            if dungeon_master['Kitchen']['fight'] == False:
                print('-' * 5)
                print('The crazy chef throwing 2 flame knife')
                for enemy in enemies:
                    enemy['hp'] -= 20
                    print(f"{enemy['name']}'s hp remaining is: {enemy['hp']}!")
            print('-' * 5)
            print("'YES !!!' As the survivor cheer for a succesfull hit !")
            print("But it haven't stop moving yet, we leave this to you now ~ Bye")
            print('-' * 5)
        clear, player = combat(player, main_party, enemies, room_actor)
        if clear == "WON":
            print('-' * 5)
            print("Hey man, we glad you stumble upon this place, we wouldn't have survive without you")
            # they shoud give the plyaer some item here but it fine for now
            print("The old mage speak, small but gently.")
            print("Thanks you.")
            print('-' * 5)
            print('A. It fine, But where are you going anways ?')
            print('B. It is my duty to help people, no problem now.')
            print("C. What the fuck is that ? Why they are here ? Shadow mist leaking in ?")
            answer = input("It seem they so glad that you able to help, you can ask them one question now: ").strip().upper()
            while answer not in ["A", "B", "C"]:
                print("It is rude to make them wait.")
                answer = input("It seem they so glad that you able to help, you can ask them one question now: ").strip().upper()
            if answer == "A":
                print('-' * 5)
                print("We were looking for a artifact deep inside this dungeon.")
                print("It hold .. something we needed")
                print("The warrior slienly look at the man with big hat, as his hands shaken.")
                print("You shouldn't stay here now, see you outside later.")
            if answer == "B":
                print('-' * 5)
                print("We heard there is some noise next room.")
                print("as if there is somebody there, the old man added")
                print("becareful, they both said as the same time with worry.")
                print("You shouldn't stay here now, see you outside later.")
            if answer == "C":
                print('-' * 5)
                print("Yeah, look - the man point toward a hole in the ceilling.")
                print("it leak from there, it seem there is a 'rain' happens now")
                print("We safe, i hope so.")
                print("You shouldn't stay here now, see you outside later.")
        dungeon_master['Treasure']['fight'] == True
        return clear, player
    if answer == "B":
        print('-' * 5)
        room_actor = [giant_shadow.copy(), shadow.copy(), shadow.copy(), shadow.copy()]
        enemies = [npc_mage.copy(), npc_warrior.copy()]
        print("The shadow doesn't care about your choice, lift it own giant sword upward prepare to strike")
        print("while the survivor still confuse, they quickly try to cast a barrier spell.")
        print('-' * 5)
        print(f"The Shadow Strike quick swings it sword downward !")
        for enemy in enemies:
            enemy['hp'] = 100
            enemy['hp'] = enemy['hp'] // 2
            print(f"{enemy['name']}'s hp remaining is: {enemy['hp']}!")
        print('-' * 5)
        print("The attack criticaly wounded the old mage.")
        print("The shadow..they stand beside you ? ignore you ? But that doesn't matter.")
        print("They hold their ground for now ? But for how long they stand before your might ?")
        print('-' * 5)
        clear, player = combat(player, main_party, enemies, room_actor) 
        print('-' * 5)
        print("Without any words, as we finishing the suvivor all the shadow vanish.")
        print("Only their eery laughter remain.")
        return clear, player
    if answer == "C":
        print('-' * 5)
        print("You decided it was not worth your trouble, as you escape your way into the next room.")
        print("'A small dark puddle ?")
        print("Only your reflection remain. .")
        print('-' * 5)
        print('A. Look ?')
        print("B. Don't.")
        answer = input('What is your answer ? ').strip().upper()
        while answer not in ["A"]:
            print('-' * 5)
            print("You can't escape.")
            print('A. Look ?')
            print("B. Don't.")
            answer = input('What is your answer ? ').strip().upper()
        print("From the shadow puddle, stepping out 2 shadow with a huge shielf, they're ready to fight.")
        print("So are you.")
        room_actor = []
        enemies = [shadow_guardian.copy(), shadow_guardian.copy()]
        for enemy in enemies:
            enemy['hp'] = 100
        clear, player = combat(player, main_party, enemies, room_actor)
        print('-' * 5)
        print("What the fuck was that ?")
        print("Those enemies was even taugher than the giant shadow.")
        print("Maybe in the end, escaping was a wrong choice ?")
        return clear, player


    

def kitchen(player):
    clear = False
    print('A kitchen ? In the middle of this dark dungeon ?')
    print('Suddently you sense a chilling wind slip across your shoulder, weirdly chilling in this unbelievable scenery')
    print('Human. . faces ? everywhere in this kitchen.. you move as yourself try to not step on any of them')
    print('-' * 5)
    print(f"In the far corner near the freezer you saw a strange man!")
    print('What are you doing in my kitchen ? The huge figure ask, hold tightly the kitchen knife in his hand')
    print('-' * 5)
    print('A. I try to find another ingredient for my newly made cake, can you help me ?')
    print('B. Not much, just wandering around man, what yo doing there ?')
    print('C. Your face is my ass')
    print('-' * 5)
    print('You scared. But let make this decision fast ~')
    answer = input('What is your answer ? ').strip().upper()
    if answer not in ['B']:
        print('-' * 5)
        print('The man started to run toward you screaming.. prepare to fight !')
        print(weird_man['taunting'])
        print('-' * 5)
        dungeon_master["Kitchen"]['fight'] = True
        room_actor = []
        enemies = [weird_man.copy(), slime.copy(), slime.copy()]
        clear, player = combat(player, main_party, enemies, room_actor)
        return clear, player
    else:
        print('-' * 5)
        print("Ho Ho Ho ~ The truth is i just found the perfect spice for ALL of my food, I'm busy")
        print("He disappeared into a huge iron door, it seem to be your only way forward too")
        print("You noticed there is one potion on the desk.")
        ipotion["number"] = 2
        clear = True
        return clear, player    
   
def room1(player):
    if dungeon_master["Lobby"]['flag']:
        print("=" * 5, "Cleared", "=" * 5)
        print("There is not thing here for you to see.")
        print("Still, this is your first room, special isn't it ?")
        clear = True
        return clear, player
    clear = False
    room_actor = []
    enemies = [skeleton.copy(), skeleton.copy()]
    clear, player = combat(player, main_party, enemies, room_actor)
    return clear, player

def room2(player):
    if dungeon_master["Hallway"]['flag']:
        print("=" * 5, "Cleared", "=" * 5)
        print("There is not thing here for you to see too.")
        print("But it not even your first room too, super lame huh ?")
        clear = True
        return clear, player
    clear = False
    room_actor = []
    enemies = [skeleton.copy(), slime.copy(), slime.copy()]
    clear, player = combat(player, main_party, enemies, room_actor)
    return clear, player

#Map (Kinda)

dungeon_master = {
    "Entrance": {
        "path": { "Lobby" },
    },
    "Lobby": {
        "path": { "Lobby", "Hallway" },
        "room": room1,
        "flag": False,
    },
    "Kitchen": {
        "path": { "Hallway", "Kitchen", "Treasure" },
        "room": kitchen,
        "flag": False,
        "fight": False
    },
    "Hallway": {
        "path": { "Lobby", "Hallway", "Kitchen" },
        "room": room2,
        "flag": False,
    },
    "Treasure": {
        "path": { "Treasure", "Gate" },
        "room": survivor,
        "flag": False,
        "fight": False
    },
    "Gate": {
        "path": { "Treasure", "Gate" },
        "room": gate,
        "flag": False,
    },

}

#The real game

def game(player):
    current_location = dungeon_master["Entrance"]['path']
    while True:
        if dungeon_master["Gate"]['flag']:
            if dungeon_master['Kitchen']['fight'] == False:
                print('-' * 5)
                print("You and the chef get to know eachother better.")
                print("It turn out he just a chill guy !")
                print("ENDING C: Brother forever.")
                return player
            if dungeon_master['Treasure']['fight'] == False:
                print("What have you done ?")
                print('-' * 5)
                print("A. It was necessesary. ")
                print("B. . . .")
                print('-' * 5)
                print("How can you live with your self after this ?")
                answer = input("").strip().upper()
                while answer not in ["A", "B"]:
                    print("How can you live with your self after this ?")
                    answer = input("").strip().upper()
                if answer == "A":
                    print('-' * 5)
                    print("So be it.")
                    print("ENDING B1: No turning back")
                    return player
                if answer == "B":
                    print('-' * 5)
                    print("Don't be. It can't bring them back alive.")
                    print("ENDING B2: Regret.")
                    return player
            print('-' * 5)
            print("This is just another stepping stone for your journey.")
            print("We will move forward, again and again")
            print("ENDING A: Another dungeon.")
            return player
        print('-' * 5)
        print("As you stand in this cold dark room, there is only one way forward.")
        answer = location(current_location) 
        print('-' * 5)
        current_location = dungeon_master[answer]['path']
        dungeon_master[answer]['flag'], player = dungeon_master[answer]['room'](player)
game(player)