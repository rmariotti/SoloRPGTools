from game import game_manager
from render import swade_character as character_render

def main():
    game = game_manager.GameManager()
    character_render.print(game.character)