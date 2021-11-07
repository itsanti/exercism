def annotate(minefield):
    if len(minefield) == 0:
        return []

    cols = len(minefield[0])
    for row in minefield[1:]:
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")

    for row, data in enumerate(minefield):
        for cell, data_cell in enumerate(data):
            if not (data_cell in ' *' or data_cell.isdigit()):
                raise ValueError("The board is invalid with current input.")
            if data_cell == '*':
                increment(minefield, row, cell)
    return minefield


def increment(field, row, cell):
    width = len(field[0])
    height = len(field)

    if cell - 1 >= 0 and row - 1 >= 0:
        cell_update(field, cell - 1, row - 1)
    if row - 1 >= 0:
        cell_update(field, cell, row - 1)
    if cell + 1 < width and row - 1 >= 0:
        cell_update(field, cell + 1, row - 1)
    if cell - 1 >= 0:
        cell_update(field, cell - 1, row)
    if cell + 1 < width:
        cell_update(field, cell + 1, row)
    if cell - 1 >= 0 and row + 1 < height:
        cell_update(field, cell - 1, row + 1)
    if row + 1 < height:
        cell_update(field, cell, row + 1)
    if cell + 1 < width and row + 1 < height:
        cell_update(field, cell + 1, row + 1)


def cell_update(field, cell, row):
    if field[row][cell] == '*':
        return
    s = list(field[row])
    if field[row][cell] == ' ':
        s[cell] = '1'
    else:
        s[cell] = str(int(s[cell]) + 1)
    field[row] = ''.join(s)


if __name__ == '__main__':
    annotate(["   ", " * ", "   "])  # ["111", "1*1", "111"]
