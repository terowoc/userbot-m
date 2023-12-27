import random

bios = [
    'I cant remember the last time that anynoe kept shit real!',
    'Pixel slayer, heartbreaker. 💔🎮',
    'Ctrl + Alt + Obliterate. 🚀🎮',
    'Gaming\'s my weapon, armed to the teeth. 🔫🎮',
    'Master of the game, destroyer of norms. ⚔️🎮',
    'In a world of amateurs, I\'m the hardcore. 🏆🎮',
    'Loading... Unleashing ruthless domination. 💣🎮',
    'Controller in hand, world at my mercy. 🔥🎮',
    'Living on the edge of brutality and brilliance. ⚡🎮',
    'No respawn for the weak-hearted. 💀🎮',
    'Game on, haters off. 😈🎮',
]

class Bio:
    def get_bio():
        return random.choice(bios)
    