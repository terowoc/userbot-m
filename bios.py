import random

bios = [
    'I cant remember the last time that anynoe kept shit real!',
    'Pixel slayer, heartbreaker. 💔🎮 | Code assassin, game overlord | Life\'s a battlefield, and I\'m the warlord.',
    'Ctrl + Alt + Obliterate. 🚀🎮 | Crushing dreams, one high score at a time | Living on the edge of chaos and caffeine.',
    'Gaming\'s my weapon, armed to the teeth. 🔫🎮 | Code master, game destroyer | Life\'s a game, and I\'m the final boss.',
    'Master of the game, destroyer of norms. ⚔️🎮 | Crushing competition, sipping tears | Code harder, game harder, live harder.',
    'In a world of amateurs, I\'m the hardcore. 🏆🎮 | Pixel perfectionist, reality wrecker | Caffeine-fueled, chaos-infused, and loving it.',
    'Loading... Unleashing ruthless domination. 💣🎮 | Code breaker, dream crusher | Crushing limitations and sipping on the bitterness of victory.',
    'Controller in hand, world at my mercy. 🔥🎮 | Life\'s not a game; it\'s my battleground | Code, conquer, repeat | No room for the weak.',
    'Living on the edge of brutality and brilliance. ⚡🎮 | Breaking barriers, setting fire to the status quo | Code like a savage, game like a legend.',
    'No respawn for the weak-hearted. 💀🎮 | Crushing mediocrity beneath my pixelated boots | Life\'s not fair, get used to it.',
    'Game on, haters off. 😈🎮 | Code disruptor, life destructor | Conquering pixels and crushing dreams with a smirk.',
]

class Bio:
    def get_bio():
        return random.choice(bios)
    