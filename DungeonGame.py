import random
import time

class Player:
    def __init__(self):
        self.health = 100
        self.attack_power = 15
        self.gold = 0
        self.potions = 2
        self.position = [0, 0]  # Start at the top-left corner

    def attack(self, enemy):
        damage = random.randint(5, self.attack_power)
        enemy.health -= damage
        print(f"You attack the {enemy.name} for {damage} damage!")

    def use_potion(self):
        if self.potions > 0:
            self.health += 20
            self.potions -= 1
            print("You used a health potion! (+20 HP)")
        else:
            print("You have no potions left!")

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        damage = random.randint(5, self.attack_power)
        player.health -= damage
        print(f"The {self.name} attacks you for {damage} damage!")

def encounter_enemy(player):
    enemy_types = [
        Enemy("Goblin", 30, 10),
        Enemy("Skeleton", 40, 12),
        Enemy("Orc", 50, 15)
    ]
    enemy = random.choice(enemy_types)
    print(f"\n⚔️ A wild {enemy.name} appeared! Prepare for battle!")

    while enemy.health > 0 and player.health > 0:
        action = input("\nDo you want to (A)ttack or (P)otion? ").lower()
        if action == 'a':
            player.attack(enemy)
            if enemy.health > 0:
                enemy.attack(player)
        elif action == 'p':
            player.use_potion()
        else:
            print("Invalid action! Try again.")

        time.sleep(1)

    if player.health > 0:
        print(f"🎉 You defeated the {enemy.name}!")
        player.gold += random.randint(5, 20)
    else:
        print("💀 You were defeated... Game Over!")

def find_treasure(player):
    rewards = ["gold", "potion", "trap"]
    found = random.choice(rewards)

    if found == "gold":
        gold_amount = random.randint(10, 50)
        player.gold += gold_amount
        print(f"💰 You found a treasure chest with {gold_amount} gold!")
    elif found == "potion":
        player.potions += 1
        print("🧪 You found a health potion!")
    else:
        damage = random.randint(5, 15)
        player.health -= damage
        print(f"⚠️ Oh no! The chest was trapped! You lost {damage} health.")

def dungeon_game():
    player = Player()
    dungeon_size = 5
    exit_point = [dungeon_size - 1, dungeon_size - 1]

    print("\n🗺️ Welcome to the Dungeon! Find the exit and escape!\n")
    
    while player.position != exit_point and player.health > 0:
        print(f"\n📍 You are at position {player.position}.")
        move = input("Move (W)Up (S)Down (A)Left (D)Right: ").lower()

        if move == 'w' and player.position[0] > 0:
            player.position[0] -= 1
        elif move == 's' and player.position[0] < dungeon_size - 1:
            player.position[0] += 1
        elif move == 'a' and player.position[1] > 0:
            player.position[1] -= 1
        elif move == 'd' and player.position[1] < dungeon_size - 1:
            player.position[1] += 1
        else:
            print("❌ Invalid move! Stay within the dungeon walls.")
            continue

        event = random.choice(["nothing", "enemy", "treasure"])
        if event == "enemy":
            encounter_enemy(player)
        elif event == "treasure":
            find_treasure(player)
        else:
            print("🔎 The area is quiet...")

    if player.health > 0:
        print("\n🏆 You found the exit! But a boss stands in your way...")
        boss = Enemy("Dungeon Lord", 80, 20)
        encounter_enemy(player)

        if player.health > 0:
            print("\n🎉 Congratulations! You escaped the dungeon with", player.gold, "gold!")
        else:
            print("\n💀 You were defeated just before escaping!")

if __name__ == "__main__":
    dungeon_game
