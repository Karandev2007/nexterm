import os
import random
import time
import keyboard

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def start_game():
    width = 30
    height = 10
    player_pos = width // 2
    enemies = []
    bullets = []
    score = 0

    print("🚀 Space Dodge Game\n➡️ Move: Arrow Keys | 🅿️ Fire: Space | ❌ Quit: Q")
    print("Starting in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

    game_over = False
    last_enemy_time = time.time()

    while not game_over:
        clear()
        # add enemies randomly
        if time.time() - last_enemy_time > 0.5:
            if random.randint(0, 1):
                enemies.append([0, random.randint(0, width - 1)])
            last_enemy_time = time.time()

        # move enemies
        for enemy in enemies:
            enemy[0] += 1

        # move bullets
        for bullet in bullets:
            bullet[0] -= 1

        # check bullet collisions
        bullets = [b for b in bullets if b[0] >= 0]
        new_enemies = []
        for e in enemies:
            hit = False
            for b in bullets:
                if b[0] == e[0] and b[1] == e[1]:
                    score += 1
                    hit = True
                    bullets.remove(b)
                    break
            if not hit:
                new_enemies.append(e)
        enemies = new_enemies

        # check player collision
        for e in enemies:
            if e[0] == height - 1 and e[1] == player_pos:
                game_over = True

        # input handling
        if keyboard.is_pressed("left"):
            player_pos = max(0, player_pos - 1)
        if keyboard.is_pressed("right"):
            player_pos = min(width - 1, player_pos + 1)
        if keyboard.is_pressed("space"):
            bullets.append([height - 2, player_pos])
        if keyboard.is_pressed("q"):
            print("👋 Exiting...")
            return

        # draw the game screen
        for row in range(height):
            line = ""
            for col in range(width):
                symbol = " "
                for e in enemies:
                    if e[0] == row and e[1] == col:
                        symbol = "X"
                for b in bullets:
                    if b[0] == row and b[1] == col:
                        symbol = "^"
                if row == height - 1 and col == player_pos:
                    symbol = "A"
                line += symbol
            print(line)

        print(f"🎯 Score: {score}")
        time.sleep(0.1)

    print("\n💀 Game Over! Final Score:", score)
    input("Press Enter to exit...")