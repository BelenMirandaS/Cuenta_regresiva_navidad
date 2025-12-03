import os
import time
import datetime
import random

# Colores ANSI para terminal
RESET = "\033[0m"
GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BROWN = "\033[33m"
GOLD = "\033[93m"
MAGENTA = "\033[95m"

TREE_WIDTH = 25

TREE_LINES = [
    "           ^           ",
    "          ***          ",
    "         *****         ",
    "        *******        ",
    "       *********       ",
    "      ***********      ",
    "     *************     ",
    "    ***************    ",
    "   *****************   ",
    "  *******************  ",
    " ********************* ",
    "  *******************  ",
    "   *****************   ",
    "    ***************    ",
    "     *************     ",
    "      |||||||||||      ",
    "       ||||||||||       ",
    "        ||||||||        ",
    "         ||||||         ",
    "        /|||||||\\        ",
    "       | [][][][] |       "
]

TREE_LINES = [line.ljust(TREE_WIDTH) for line in TREE_LINES]

LIGHT_POS = [
    (1,6),(1,18),
    (2,5),(2,19),
    (3,4),(3,20),
    (4,3),(4,21),
    (5,2),(5,22),
    (6,5),(6,19),
    (7,4),(7,20),
    (8,3),(8,21),
    (9,2),(9,22),
    (10,1),(10,23),
    (11,2),(11,22),
    (12,3),(12,21),
    (13,4),(13,20),
    (14,5),(14,19)
]

BAUBLE_POS = [
    (3,8),(3,16),
    (4,7),(4,17),
    (5,6),(5,18),
    (6,9),(6,15),
    (7,8),(7,16),
    (8,7),(8,17),
    (9,6),(9,18),
    (10,5),(10,19)
]

def print_tree():
    print(GOLD + "     🎄 Árbol Navideño con Luces Parpadeantes 🎄     ".center(TREE_WIDTH) + RESET)
    print()
    
    for r, line in enumerate(TREE_LINES):
        colored_line = ''
        for c, char in enumerate(line):
            pos = (r, c)
            if pos in BAUBLE_POS:
                bcolor = random.choice([RED, GREEN, GOLD, MAGENTA])
                colored_line += bcolor + 'o' + RESET  # o for bauble
            elif pos in LIGHT_POS:
                if random.random() < 0.7:
                    lcolor = random.choice([YELLOW, RED, BLUE, CYAN, WHITE])
                    sym = random.choice(['*', '.'])
                    colored_line += lcolor + sym + RESET
                else:
                    colored_line += ' '
            elif char == '^':
                colored_line += YELLOW + '^' + RESET
            elif char == '*':
                colored_line += GREEN + '*' + RESET
            elif char == '|':
                colored_line += BROWN + '|' + RESET
            elif char in '/\\':
                colored_line += BROWN + char + RESET
            elif char in '[]':
                colored_line += CYAN + char + RESET
            else:
                colored_line += char
        print(colored_line)
    print()

def get_target():
    now = datetime.datetime.now()
    target = datetime.datetime(now.year, 12, 25, 0, 0, 0)
    if target <= now:
        target = datetime.datetime(now.year + 1, 12, 25, 0, 0, 0)
    return target

def format_countdown():
    target = get_target()
    delta = target - datetime.datetime.now()
    if delta.total_seconds() <= 0:
        return "¡Feliz Navidad! 🎄🎁✨"
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    return f"Quedan {days} días, {hours:02d} horas, {minutes:02d} minutos, {seconds:02d} segundos."

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_tree()
        countdown = format_countdown()
        print(countdown.center(TREE_WIDTH))
        delta = get_target() - datetime.datetime.now()
        if delta.total_seconds() <= 0:
            print("\n" + YELLOW + "¡Feliz Navidad! 🎄🎁✨" + RESET)
            time.sleep(5)
            break
        time.sleep(1)

if __name__ == "__main__":
    main()