# neg_nums_in_matrix.py


def countNegatives(grid):
    rv = 0
    for x in grid:
        for y in x:
            if y < 0:
                rv += 1
    return rv


if __name__ == '__main__':
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(countNegatives(grid))
