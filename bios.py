import random

bios = [
    'I cant remember the last time that anynoe kept shit real!',
    'Pixel slayer, heartbreaker. 💔🎮 | Life\'s a battlefield, and I\'m the warlord.',
    'Ctrl + Alt + Obliterate. 🚀🎮 | Living on the edge of chaos and caffeine.',
    'Gaming\'s my weapon, armed to the teeth. 🔫🎮 | Life\'s a game, and I\'m the final boss.',
    'Master of the game, destroyer of norms. ⚔️🎮 | Code harder, game harder, live harder.',
    'In a world of amateurs, I\'m the hardcore. 🏆🎮 | Caffeine-fueled, chaos-infused, and loving it.',
    'Loading... Unleashing ruthless domination. 💣🎮 | Crushing limitations and sipping on the bitterness of victory.',
    'Controller in hand, world at my mercy. 🔥🎮 | Code, conquer, repeat | No room for the weak.',
    'Living on the edge of brutality and brilliance. ⚡🎮 | Code like a savage, game like a legend.',
    'No respawn for the weak-hearted. 💀🎮 | Life\'s not fair, get used to it.',
    'Game on, haters off. 😈🎮 | Conquering pixels and crushing dreams with a smirk.',
]

class Bio:
    def get_bio():
        return random.choice(bios)
    