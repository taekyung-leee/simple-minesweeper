# Creating a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot.
# Return a grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot 
# i.e. (horizontally, vertically, and diagonally).

# '#' represents mine
# '-' represents mine-free spot
mine_grid = [ ["-", "#", "-", "-", "-"],
              ["#", "-", "#", "#", "-"],
              ["-", "-", "-", "-", "#"],
              ["-", "-", "-", "#", "-"],
              ["#", "-", "#", "-", "-"],]

# expected grid =
'''
['2', '#', '3', '2', '1']
['#', '3', '#', '#', '2']
['1', '2', '3', '4', '#']
['1', '2', '2', '#', '2']
['#', '2', '#', '2', '1']
'''

def minesweeper(mine_grid):
    rows = len(mine_grid)
    cols = len(mine_grid[0])
    result_grid = [["0"] * cols for _ in range(rows)]
    for i, row in enumerate(mine_grid):
        for j, spot in enumerate(row):
            if spot == "#":
                result_grid[i][j] = "#"
            else:
                count = 0
                for x in range(max(i-1, 0), min(i+2, rows)):
                    for y in range(max(j-1, 0), min(j+2, cols)):
                        if mine_grid[x][y] == "#":
                            count += 1
                result_grid[i][j] = str(count)
    return result_grid

result_grid = minesweeper(mine_grid)

print("Final grid based on the example mine grid will be: ")
for row in result_grid:
    print(row)