n = int(input())
matrix = []
check = 0
count = 0  # счетчик ходов, для отслеживания зода игрока
for i in range(10):
    row = list("*" * 10)
    matrix.append(row)
for i in range(n):
    r, c = map(int, input().split())
    if count % 2 == 0:
        matrix[r][c] = "x"
        count += 1
    else:
        matrix[r][c] = "0"
        count += 1
row = -1
col = 0
for i in matrix:

    row += 1
    if "x" in i:
        col = i.index("x")

        break


def diagonaly(row, col):
    one = 0
    for i in range(10):
        if matrix[row][col] == "x":  # Проверка по диагонали
            one += 1
            row += 1
            col += 1
    return one


def vertikal(row, col):
    one = 0
    for i in range(10):
        if matrix[row][col] == "x":  # Проверка по диагонали
            one += 1
            row += 1
    return one


def goeizont(row, col):
    one = 0
    for i in range(10):
        if matrix[row][col] == "x":  # Проверка по диагонали
            one += 1
            col += 1
    return one


y = diagonaly(row, col)
y2 = vertikal(row, col)
y3 = goeizont(row, col)
if y == 5:
    print("First")
