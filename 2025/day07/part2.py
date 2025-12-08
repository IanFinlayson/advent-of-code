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

    # find the S which is where the beam starts
    beam_indices = [0 for i in range(len(grid[0]))]
    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            beam_indices[i] = 1

    # go for each row after this
    for row in range(1, len(grid) - 1):
        next_row = [0 for i in range(len(grid[0]))]

        # go through each column
        for col in range(len(grid[row])):
            # if there's a beam here, and a splitter below us, then put a beam on two locations
            if beam_indices[col] >= 1 and grid[row + 1][col] == '^':
                if (col - 1) >= 0:
                    next_row[col - 1] += beam_indices[col]
                if (col + 1) < len(grid[row]):
                    next_row[col + 1] += beam_indices[col]

                # otherwise the beam just moves down
            elif beam_indices[col] >= 1:
                next_row[col] += beam_indices[col]

        # move this down to the next row of beasm
        beam_indices = next_row[:]
        #print(beam_indices)

    # now we return the sum of the last row
    return sum(beam_indices)


def main():
    grid = getGrid()
    for line in grid:
        for c in line:
            print(c, end="")
        print()
    print(simulate(grid))


main()

