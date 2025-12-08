
def getGrid():
    grid = []
    while True:
        try:
            line = input()
            grid.append([char for char in line])
        except EOFError:
            break
    return grid

def simulate(grid):
    # we keep track of the indices of the beams
    beam_indices = []
    splits = 0

    # find the S which is where the beam starts
    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            beam_indices.append(i)

    # go for each row after this
    for row in range(1, len(grid) - 1):
        #print("Our input beams are", beam_indices)
        next_row = []

        # go through each column
        for col in range(len(grid[row])):
            # if there's a beam here, and a splitter below us, then put a beam on two locations
            if col in beam_indices and grid[row + 1][col] == '^':
                splits += 1
                if (col - 1) >= 0:
                    next_row.append(col - 1)
                if (col + 1) < len(grid[row]):
                    next_row.append(col + 1)

                # otherwise the beam just moves down
            elif col in beam_indices:
                next_row.append(col)

        # move this down to the next row of beasm
        #print(next_row)
        beam_indices = next_row[:]
    return splits

def main():
    grid = getGrid()
    for line in grid:
        for c in line:
            print(c, end="")
        print()
    print(simulate(grid))


main()

