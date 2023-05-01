# simple-minesweeper

Creating a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot.
Return a grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot 
i.e. (horizontally, vertically, and diagonally).

The function uses 2D List, for loops and def function. 

For example, when the input 2D mine grid represents:
[["-", "#", "-", "-", "-"],\
["#", "-", "#", "#", "-"],\
["-", "-", "-", "-", "#"],\
["-", "-", "-", "#", "-"],\
["#", "-", "#", "-", "-"],]\

The output will be:
['2', '#', '3', '2', '1']\
['#', '3', '#', '#', '2']\
['1', '2', '3', '4', '#']\
['1', '2', '2', '#', '2']\
['#', '2', '#', '2', '1']\

in this code. 
