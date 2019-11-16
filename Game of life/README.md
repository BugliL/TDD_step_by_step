# Conway's Game of life
Part of the project created to experiment techniques and/or approaces using the "game of life".
Each chapter explore something starting from the basic implementation. 
[Wipedia page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Rules
The world is a big chessboard where "cells" born, live and die using specific rules.
A god (in this case, the programmer) create the cells in first place and applying rules 
to the chessboard instance let cells configuration change.
This process is called EVOLUTION.
The game is finished when all cells are dead.

The rules are:
 - Any live cell with two or three neighbors survives.
 - Any dead cell with three live neighbors becomes a live cell.
 - All other live cells die in the next generation. Similarly, all other dead cells stay dead.