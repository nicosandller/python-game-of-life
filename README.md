# python-game-of-life
### Python object-oriented TDD implementation of Conway's game of life.


To create a new board `Board(dimension)`

| Method        | Description           | Arguments  |
| ------------- |:-------------:| ----------|
|`.add_cell(pos = (x,y))`| Adds an alive cell at the defined position| pos = (x,y) |
|`.insert_random_cells(n)`| Adds n alive cells at random positions| n = number |
|`.insert_blinker()`| Inserts a Blinker figure to the board at a random position| **Takes no argument** |
|`.insert_toad()`| Adds an alive cell at the defined position| **Takes no argument** |
|`.next()`| Moves one period in time to the next generation of cells| **Takes no argument** |
|`.show()`| Shows the board with living cells marked with an 'X'.| **Takes no argument** |


## Sample Code:

```python
from board import Board
import time 

game = Board(15)
game.insert_blinker()
game.insert_toad()
game.add_random_cells(20)

while True:
  game.show()
  game.next()
  time.sleep(1)
```

## Screenshots:

![Alt text](/img1.jpg?raw=true "Optional Title")
  
