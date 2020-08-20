# SoloRPGTools

### 1. Installation

### 2. Usage
Run the following command inside the folder where you want to place your game notebook:

```shell script
solorpgtools --new-game
```

This will create a configuration file in the current folder, called `game.xml`

Create a new Jupyter Notebook, if SoloRPGTools was installed using `venv` remember 
to set the default python interpreter for the notebook accordingly.  

Inside the notebook copy the following lines in the first python cell:

```python
from game.game_manager import GameManager

game = GameManager('./game.xml')
```