warrior= {
    "name": "Cave man",
    "hp": 20,
    "attack": 10,
    "bigbonk": 15
}

mage = {
    "name": "Mana Spitter",
    "hp":15,
    "mana": 6,
    "attack": 8,
    "fireball": 20
}

skeleton = {
    "name": "Scary Bone Man",
    "hp":15,
    "attack":2
}

def combat(attacker, defender):
    damage = attacker['attack']
    defender['hp'] -= damage
    print(f"{attacker['name']} hits {defender['name']} for {damage} damage!")
    if defender['hp'] > 0:
        print(f"{defender['name']}'s HP is now {defender['hp']}.")
    else:
        print(f"{defender['name']} FUCKING DEAD !")
    return defender["hp"]

while defender["hp"] > 0:
    

player = None
def ask_class(question):
    answer = input(question).strip().upper()
    while answer not in ["WARRIOR", "MAGE"]:
        print("INVALID")
        answer = input(question).strip().upper()
    return answer

def create_player(chose):
    if chose == "WARRIOR":
        return warrior
    if chose == "MAGE":
        return mage
    
chosen = ask_class("Chose class: ")
player = create_player(chosen)

print(player)
print(f"{combat(player, skeleton)}")

def ask_yes_no(x):
    answer = input(x).strip().upper()
    while answer not in ["YES", "NO"]:
        print("INVALID")
        answer = input(x).strip().upper()
    return answer

def ask_class(x):
    answer = input(x).strip().upper()
    while answer not in ["WARRIOR", "MAGE"]:
        print("INVALID")
        answer = input(x).strip().upper()
    return answer