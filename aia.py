
import random


enemies = {
    "goblin": {
        "hp": 25,
        "damage": 5,
        "description": "A small goblin.",
        "drop_chance": 0.25,
        "drops": ["dagger"]
    },
    "guards": {
        "hp": 35,
        "damage": 8,
        "description": "The village guard",
        "drop_chance": 0.95,
        "drops": ["guards shield"]
    },
    "king": {
        "hp": 135,
        "damage": 15,
        "description": "The villages tirannic king"
    },
    "ghost": {
        "hp": 2,
        "damage": 0,
        "description": "an immaterial ghost that cant be touched",
        "attackable": False
    },
    "necromancer": {
        "hp": 100,
        "damage": 12,
        "description": "A dark mage who commands the dead.",
        "special_ability": {
            "name": "Soul Drain",
            "trigger_chance": 0.3,
            "effect": "drains 20 HP from you and heals himself"
        },
    "use_items": {
        "healing potion": {
            "heal_amount": 30,
            "uses": 1
        }
    },
    "drop_chance": 1.0,
    "drops": ["necromancer staff"]
}

}

items = {
    "sword": {
        "description": "an old rusty blade.",
        "type": "weapon",
        "damage": 7
    },
    "key": {
        "description": "A big key maybe it opens something.",
        "type": "key"
    },
    "guards shield": {
        "description": "A shield carried by the village Guards.",
        "type": "armor",
        "defense": 5
    },
    "gold chest": {
        "description": "A chest filled with gold coins.",
        "type": "treasure",
        "value": 100
    },
    "dagger": {
        "description": "A small, quick blade.",
        "type": "weapon",
        "damage": 6
    },
    "health potion": {
        "description": "Restores 50 HP when used.",
        "type": "healing",
        "heal_amount": 50
    },
    "magic robe": {
        "description": "A shimmering robe imbued with protective magic. Increases your defense.",
        "type": "armor",
        "defense": 8,
    },
    "pendant":{
        "description":"an old shiny pendant",
        "type":"quest"
    },
    "necromancer staff": {
        "description": "A dark staff that drains life from enemies.",
        "type": "weapon",
        "damage": 5,
        "effect": "soul_drain"
    },
    "better sword":{
        "description":"a great sword",
        "type":"weapon",
        "damage":8
    },
    "bone":{
        "description":"a bone",
        "type":"quest"

    }
}




def create_player():
    player = {
        "name": input("whats your name? "),
        "hp": 100,
        "max_hp": 100,
        "xp": 0,
        "level": 1,
        "inventory": {},
        "location": "0",
        "current_enemy": None,
        "flags": {"ghost_block": True},
        "gold": 0,  
        "quests": {}
    }
    return player

def load_map():
    rooms = {
        "0": {
            "description": "You are in a forest surrounded by trees.",
            "exits": {"north": "1"},
            "items": ["sword", "health potion"],
            "enemy": None,
            "details": {
                "tree": "its just a tree"
            }
        },
        "1": {
            "description": "A crossway point between the merchant and the town.",
            "exits": {"east": "2", "north": "3"},
            "items": [],
            "enemy": None,
            "details":{
                "crossway":"A simple crossway it leads to the merchant (east) or the village whom is further north",
            }
        },
        "2": {
            "description": "The Merchants Adobe! Buy anything you want.",
            "exits": {"west": "1"},
            "items": [],
            "enemy": None,
            "details":{
                "merchant": "A wandering merchant.",
            },
            "npcs":{
                "merchant":{
                    "dialogue":"interested in buying something?"
            },
            },
            "merchant_inventory" : {
                "health potion": 25,
                "better sword": 50
            },
            
            
        },
        "3": {
            "description": "your path diverges in 3 , village to the east , cave to the east and a cimitary to the north.(hint:go there once strong enough)",
            "exits": {"east": "6", "west": "4","north": "12","south":"1"},
            "items": [],
            "enemy": None,
            "details":{
                "cave entrance": "exactly what the name suggests",
                "village ligths":"the ligths of the village whom is to your west",
                "village": "the village , migth be interesting to go there"

            }
        },
        "4": {
            "description": "You are at the village you can see a monk some villagers and a mage.",
            "exits": {"east": "3", "south": "5"},
            "items": [],
            "enemy": None,
            "details":{
                "villagers": "They are talking and doing village stuff.",
            },
            "npcs":{
                "villager":{
                    "dialogue":"hello there adventurer you look like you come from bertada is that rigth?"
                },
                "monk":{
                    "dialogue":"if you give me some bones ill give you gold"
                },
                "mage":{
                    "dialogue":"i can give you a magic robe if you give me the pendant",
                    "quest_given":True,
                    "quest_completed":False
                }
            }
        },
        "5": {
            "description": "You are at the palace gates. You'll need a key to enter.",
            "exits": {"north": "4", "south": "11"},
            "items": ["guards shield"],
            "enemy": None,
            "locked": True,
            "details":{
                "palace gates": "the gates of the palace , they are locked ",
                "gates":"the gates of the palace , they are locked "
            }
        },
        "6": {
            "description": "You are at the cave entrance.",
            "exits": {"west": "3", "east": "7"},
            "items": [],
            "enemy": None,
            "details":{
                "cave entrance":"it is exactly what the name suggests",
                "cave":"it is exactly what the name suggests"
            }
        },
        "7": {
            "description": "You have entered the cave and immediatly smell the smell of a rotting corpse ,see two paths. Which do you take?",
            "exits": {"north": "8", "south": "9","west": "6"},
            "items": ["dagger"],
            "enemy": "goblin",
            "details":{
                "paths":"there are 2 ways you can go north or south",
                "two paths":"there are 2 ways you can go north or south"
            }
        },
        "8": {
            "description": "you see a chest full of coins.",
            "exits": {"south": "7"},
            "items": ["gold chest"],
            "enemy": None,
            "details":{}
        },
        "9": {
            "description": "you can see a skeleton in the next room.",
            "exits": {"north": "7", "east": "10"},
            "items": [],
            "enemy": "ghost",
            "details":{
                "ghost":"the ghost is blocking your path maybe try talking to it"
            },
            "npcs":{
                "ghost":{
                   "dialogue":"ill let you pass if you tell me the name of the king"
                }
            },
            "blocked_exits":{
                "east":{
                    "condition":"ghost_block",
                    "fail_text": "the ghost blocks your path it wont let you pass"
                }
            }
        },
        "10": {
            "description": "You see a skeleton wearing an armor a pendant and a key , you also think you can take a bone from it.",
            "exits": {"west": "9", "east": "11"},
            "items": ["key", "pendant", "bone"],
            "enemy": None,
            "details":{
                "skeleton":"this must have been the reason for the smell , you also think you could grab a bone",
                "armor":"the armor is too fragile to use , maybe use the shield?"
            }
        },
        "11": {
            "description": "You are at the throne room and see the king!",
            "exits": {"west": "10"},
            "items": [],
            "enemy": "king",
            "details":{
                "throne":"its a throne what did you expect",
                "throne room":"exactly what the name suggests"
            },
            "npcs":{
                "king":{
                    "dialogue":"what do you want"
            }
        }
    },
        "12":{
            "description":"you are in a cimitary , it reeks like death here",
            "exits":{"south":"3"},
            "items":[],
            "enemy":"necromancer"
        }
    }
    
    return rooms

def buy_item(player, item_name):
    location = player["location"]
    room = rooms[location]

    if "merchant_inventory" not in room:
        print("There is no merchant here to buy from.")
        return

    merchant_inventory = room["merchant_inventory"]

    if not item_name:
        print("Buy what?")
        return

    item_name = item_name.lower()

    if item_name not in merchant_inventory:
        print(f"The merchant does not have {item_name} for sale.")
        return

    price = merchant_inventory[item_name]

    if player.get("gold", 0) < price:
        print(f"You don't have enough gold to buy {item_name}. It costs {price} gold.")
        return

   
    player["gold"] -= price
    player["inventory"][item_name] = player["inventory"].get(item_name, 0) + 1

    print(f"You bought a {item_name} for {price} gold.")



def show_merchant_inventory(player, arg=None):
    location = player["location"]
    room = rooms[location]

    if "merchant_inventory" not in room:
        print("There is no merchant here.")
        return

    merchant_inventory = room["merchant_inventory"]

    print("The merchant sells:")
    for item, price in merchant_inventory.items():
        print(f"  {item.capitalize()} - {price} gold")

def examine_item(player, item_name):
    if not item_name:
        print("Look at what?")
        return

    item_name = item_name.lower()
    current_room = rooms[player["location"]]
    room_items = [i.lower() for i in current_room.get("items", [])]
    inventory_items = [i.lower() for i in player["inventory"].keys()]
    details = current_room.get("details", {})

    
    if item_name in inventory_items:
        real_item = list(player["inventory"].keys())[inventory_items.index(item_name)]
        data = items.get(real_item)
        if data:
            print(f"{real_item.capitalize()}: {data.get('description', 'No description.')}")
        return

    
    elif item_name in room_items:
        real_item = current_room["items"][room_items.index(item_name)]
        data = items.get(real_item)
        if data:
            print(f"{real_item.capitalize()}: {data.get('description', 'No description.')}")
        return

    
    elif item_name in details:
        print(f"{item_name.capitalize()}: {details[item_name]}")
        return

    else:
        print(f"You don't see a {item_name} here.")




def show_stats(player, arg=None):
    print("=== Player Stats ===")
    print(f"Name: {player['name']}")
    print(f"HP: {player['hp']} / {player['max_hp']}")
    print(f"Level: {player['level']}")
    print(f"XP: {player['xp']}")
    print(f"Gold: {player['gold']}")
    print(f"Location: {player['location']}")
    print("Inventory:")
    if player['inventory']:
        for item, qty in player['inventory'].items():
            print(f"  {item}: {qty}")
    else:
        print("  (empty)")
    print("====================")

def quit_game(player, arg=None):
    print(f"Goodbye, {player['name']}")
    exit()

def turn_based_combat(player):
    enemy = player["current_enemy"]
    if not enemy:
        return

    enemy_data = enemies.get(enemy["name"], {})

    while player["hp"] > 0 and enemy["hp"] > 0:
        print(f"\nYour HP: {player['hp']}/{player['max_hp']}")
        print(f"{enemy['name'].capitalize()} HP: {enemy['hp']}")

        raw_action = input("Do you want to [attack] or [use <item>]? ").strip().lower()
        parts = raw_action.split(maxsplit=1)
        action = parts[0]
        item_arg = parts[1] if len(parts) > 1 else ""

        if action == "attack":
            weapon_name = player.get("equipped_weapon")
            weapon = items.get(weapon_name, {}) if weapon_name else {}
            base_damage = weapon.get("damage", 5)

            enemy["hp"] -= base_damage
            print(f"You attack the {enemy['name']} for {base_damage} damage.")

            if weapon.get("effect") == "soul_drain":
                drain_amount = 5
                player["hp"] = min(player["hp"] + drain_amount, player["max_hp"])
                print(f"The {weapon_name} drains {drain_amount} HP and heals you.")

        elif action == "use":
            if not item_arg:
                item_arg = input("Which item? ").strip().lower()

            if item_arg in player["inventory"]:
                use_item(player, item_arg)
            else:
                print(f"You don't have a {item_arg}.")
                continue
        else:
            print("Invalid action.")
            continue

        if enemy["hp"] <= 0:
            print(f"You defeated the {enemy['name']}!")

            if enemy.get("drops") and random.random() < enemy.get("drop_chance", 0):
                drop = random.choice(enemy["drops"])
                print(f"The {enemy['name']} dropped a {drop}!")
                rooms[player["location"]]["items"].append(drop)

            rooms[player["location"]]["enemy"] = None
            player["current_enemy"] = None
            break

        enemy_damage = enemy.get("damage", 0)
        player["hp"] -= enemy_damage
        print(f"The {enemy['name']} attacks you for {enemy_damage} damage!")
        print(f"Your HP is now {player['hp']}/{player['max_hp']}.")

        if player["hp"] <= 0:
            print("You were defeated. Game over.")
            exit()

        
        if "use_items" in enemy_data:
            for item, data in list(enemy_data["use_items"].items()):
                if enemy["hp"] <= 30 and data["uses"] > 0:
                    heal = data["heal_amount"]
                    enemy["hp"] += heal
                    data["uses"] -= 1
                    print(f"The {enemy['name']} uses a {item} and heals {heal} HP!")
                    continue

        
        if "special_ability" in enemy_data:
            special = enemy_data["special_ability"]
            if random.random() < special.get("trigger_chance", 0):
                print(f"The {enemy['name']} uses {special['name']}! {special['effect']}")
                
                player["hp"] -= 20
                enemy["hp"] += 20
                if enemy["hp"] > enemy_data["hp"]:
                    enemy["hp"] = enemy_data["hp"]

        
        else:
            dmg = enemy["damage"]
            player["hp"] -= dmg
            print(f"The {enemy['name']} attacks you for {dmg} damage!")

        if player["hp"] <= 0:
            print("You have been defeated. Game over.")
            exit()


def equip_item(player, item_name):
    if item_name not in player["inventory"]:
        print(f"You don't have a {item_name}.")
        return

    item = items.get(item_name)
    if item and item.get("type") == "weapon":
        player["equipped_weapon"] = item_name
        print(f"You equipped the {item_name}.")
    else:
        print(f"You can't equip the {item_name}.")

def look_around(player, rooms):
    location = player["location"]
    room = rooms[location]
    print(room["description"])
    if room["items"]:
        print("You see:", ", ".join(room["items"]))
    else:
        print("Nothing of interest to take.")
    if room["enemy"]:
        print(f"There is a {room['enemy']} here!")
    exits = ", ".join(room["exits"].keys())
    print("Directions: " + exits)

def handle_look(player, arg):
    if not arg or arg == "around":
        look_around(player, rooms)
    else:
        examine_item(player, arg)

def show_help(player, arg=None):
    print("=== Available Commands ===")
    print("move/go <direction>    → Move to another room (e.g., move north)")
    print("look [object]   → Describe your surroundings or object specified")
    print("show stats           → Show your player stats")
    print("quit                 → Exit the game")
    print("help / ?            → Show this help menu")
    print("take   [object]     → Take specified object")
    print("inv/inventory       → Shows inventory")
    print("use    [object]     → Uses an object if it is in your inventory")
    print("fight/kill/attack <enemy> → Starts combat against specified enemy")
    print("talk <npc name>      →talks to selected npc ")
    print("equip <item>        →preferred to use this instead of use item for weapons")
    print("buy   <item>        → buys item if enough money ")
    print("shop <item> → shows what the merchant sells")
    print("========================")

def talk_to_npc(player, npc_name):
    location = player["location"]
    room = rooms[location]
    
    if "npcs" not in room or npc_name not in room["npcs"]:
        print(f"There is no {npc_name} here to talk to.")
        return

    npc = room["npcs"][npc_name]

    if npc_name == "mage":
        
        quest_status = player["quests"].get("magic_robe", None)

        if quest_status is None:
            print(npc["dialogue"])
            player["quests"]["magic_robe"] = "pending"
        elif quest_status == "pending":
            if "pendant" in player["inventory"]:
                print("Thank you for bringing the pendant! Here, take this magic robe.")
                player["inventory"]["magic robe"] = player["inventory"].get("magic robe", 0) + 1
                player["quests"]["magic_robe"] = "completed"
                
                player["inventory"]["pendant"] -= 1
                if player["inventory"]["pendant"] == 0:
                    del player["inventory"]["pendant"]
            else:
                print("You still need to bring me the pendant from the skeleton.")
        else:
            print("Thank you again for your help.")

    elif npc_name == "ghost":
        
        if player["flags"].get("ghost_block", True):
            answer = input("Ghost asks: What is the name of the king? ").strip().lower()
            if answer == "alfredus":
                print("Ghost: You may pass.")
                player["flags"]["ghost_block"] = False
                room["enemy"] = None
                player["current_enemy"] = None
            else:
                print("Ghost: That's not correct. You shall not pass.")
        else:
            print("The ghost has already let you pass.")

    elif npc_name == "monk":
        quest_status = player["quests"].get("monk_quest", None)

        if quest_status is None:
            print(npc.get("dialogue", "I have a favor to ask."))
            player["quests"]["monk_quest"] = "pending"

        elif quest_status == "pending":
            
            if "bone" in player["inventory"]:
                print("Thank you for completing my favor. Here is 50 gold as promised.")
                player["gold"] = player.get("gold", 0) + 50
                player["quests"]["monk_quest"] = "completed"
            else:
                print("Please bring me the bone to complete the quest.")

        else:  
            print("Thanks again for your help.")

    else:
        
        print(npc.get("dialogue", "They have nothing to say."))





def move_player(player, direction):
    if not direction:
        print("Move where?")
        return

    current_room = rooms[player["location"]]
    if direction in current_room["exits"]:
        
        blocked = current_room.get("blocked_exits", {}).get(direction)
        if blocked:
            condition = blocked["condition"]
            if player["flags"].get(condition, True):  
                print(blocked["fail_text"])
                return

        new_location = current_room["exits"][direction]
        target_room = rooms[new_location]

        if target_room.get("locked", False):
            if "key" in player["inventory"]:
                print("You use the key to unlock the door.")
                player["location"] = new_location
                look_around(player, rooms)
                start_encounter(player, rooms)
            else:
                print("It's locked. You need a key.")
        else:
            player["location"] = new_location
            look_around(player, rooms)
            start_encounter(player, rooms)
    else:
        print("You can't go that way.")

def take_item(player, item_name):
    location = player["location"]
    room = rooms[location]

    if not item_name:
        print("Take what?")
        return

    item_name = item_name.lower()
    available_items = [i.lower() for i in room["items"]]
    if item_name in available_items:
        real_item = room["items"][available_items.index(item_name)]
        room["items"].remove(real_item)

        if real_item in player["inventory"]:
            player["inventory"][real_item] += 1
        else:
            player["inventory"][real_item] = 1

        print(f"You picked up: {real_item}")
    else:
        print(f"There is no {item_name} here.")

def use_item(player, item_name):
    if not item_name:
        print("Use what?")
        return

    item_name = item_name.lower()

    if item_name not in player["inventory"] or player["inventory"][item_name] == 0:
        print(f"You don't have a {item_name}.")
        return

    item_data = items.get(item_name)
    if not item_data:
        print(f"The {item_name} can't be used.")
        return

    item_type = item_data.get("type")

    if item_type == "weapon":
        print(f"You brandish the {item_name}")
    elif item_type == "key":
        print(f"You look at the {item_name}. Maybe it can be used for something.")
    elif item_type == "armor":
        print(f"You equip the {item_name} it increased your defense.")
    elif item_type == "treasure":
        print(f"You admire the {item_name}. It's valuable, but you can't use it.")
    elif item_type == "healing":
        heal_amount = item_data.get("heal_amount", 0)
        player["hp"] += heal_amount
        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]
        print(f"You use the {item_name} and restore {heal_amount} HP. Current HP: {player['hp']}/{player['max_hp']}")
    elif item_type == "armor":
        defense = item_data.get("defense", 0)
        player["defense"] += defense
        print(f"You equip the {item_name}. Defense increased by {defense}. Current defense: {player['defense']}")
    elif item_type == "weapon":
        player["equipped_weapon"] = item_name
        print(f"You equipped the {item_name}.")

        player["inventory"][item_name] -= 1
        if player["inventory"][item_name] == 0:
            del player["inventory"][item_name]
    else:
        print(f"You can't use the {item_name} right now.")

def show_inventory(player, arg=None):
    print("=== Inventory ===")
    if player["inventory"]:
        for item, qty in player["inventory"].items():
            desc = items.get(item, {}).get("description", "No description.")
            print(f"{item} x{qty} - {desc}")
    else:
        print("(empty)")
    print("=================")

def start_encounter(player, rooms):
    location = player["location"]
    room = rooms[location]
    enemy_name = room.get("enemy")

    if enemy_name and player.get("current_enemy") is None:
        enemy_data = enemies.get(enemy_name)
        if enemy_data:
            if not enemy_data.get("attackable", True):
                print(f"There is a {enemy_name} here. {enemy_data.get('description', '')}")
                return

            player["current_enemy"] = {
                "name": enemy_name,
                "hp": enemy_data["hp"],
                "damage": enemy_data["damage"],
                "attackable": True,
                "drops": enemy_data.get("drops", []),
                "drop_chance": enemy_data.get("drop_chance", 0)
            }

            print(f"{enemy_name} appears! {enemy_data['description']}")
            turn_based_combat(player)  # <- Starts combat immediately

def combat_loop(player):
    enemy = player.get("current_enemy")
    if not enemy:
        print("There is nothing to fight here.")
        return

    if not enemy.get("attackable", True):
        print(f"The {enemy['name']} can't be attacked!")
        return

    print(f"Combat started with {enemy['name']} (HP: {enemy['hp']})")

    while enemy["hp"] > 0 and player["hp"] > 0:
        print("\nYour turn! Choose an action:")
        print("1. Attack")
        print("2. Use Item")
        action = input("Enter 1 or 2: ").strip()

        if action == "1":
            damage = 10  
            enemy["hp"] -= damage
            print(f"You attack the {enemy['name']} for {damage} damage. Enemy HP: {max(enemy['hp'],0)}")

            if enemy["hp"] <= 0:
                print(f"The {enemy['name']} has been defeated!")
                # drop
                if enemy["drops"] and random.random() < enemy["drop_chance"]:
                    drop = random.choice(enemy["drops"])
                    print(f"The {enemy['name']} dropped a {drop}!")
                    rooms[player["location"]]["items"].append(drop)
                else:
                    print(f"The {enemy['name']} dropped nothing.")
                rooms[player["location"]]["enemy"] = None
                player["current_enemy"] = None
                return

        elif action == "2":
            item_name = input("Which item do you want to use? ").lower().strip()
            use_item(player, item_name)
        else:
            print("Invalid action, try again.")
            continue

        # Enemy turn 
        if enemy["hp"] > 0:
            enemy_damage = enemy["damage"]
            player["hp"] -= enemy_damage
            print(f"The {enemy['name']} attacks you for {enemy_damage} damage! Your HP: {max(player['hp'],0)}")
            if player["hp"] <= 0:
                print("You have been defeated. Game over.")
                exit()

commands = {
    "move": move_player,
    "go": move_player,
    "show": show_stats,
    "quit": quit_game,
    "look": handle_look,
    "look around": lambda p, a: look_around(p, rooms),
    "help": show_help,
    "?": show_help,
    "take": take_item,
    "inventory": show_inventory,
    "inv": show_inventory,
    "use": use_item,
    "attack": lambda p, a: combat_loop(p),
    "fight": lambda p, a: combat_loop(p),
    "kill": lambda p, a: combat_loop(p),
    "talk": talk_to_npc,
    "equip": equip_item,
    "buy": buy_item,
    "shop":show_merchant_inventory,
    
}

def show_menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Start Game")
        print("2. Help")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            main_game_loop()
            break
        elif choice == "2":
            show_help(my_player)
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice.")




def main_game_loop():
    while True:
        raw_input = input(">>> ").lower().strip()
        parts = raw_input.split(maxsplit=1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        if command in commands:
            commands[command](my_player, argument)
        else:
            print("i don't understand that.")
            
def main_game_loop():
    while True:
        raw_input = input(">>> ").lower().strip()
        parts = raw_input.split(maxsplit=1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        if command in commands:
            commands[command](my_player, argument)
        else:
            print("i don't understand that.")

# ###
# Main
# ###

if __name__ == "__main__":
    my_player = create_player()
    rooms = load_map()

    show_menu()