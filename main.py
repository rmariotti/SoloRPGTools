from src.game import game_manager
from render import character as character_render

def main():
    game = game_manager.GameManager()
    character_render.print(game.character)