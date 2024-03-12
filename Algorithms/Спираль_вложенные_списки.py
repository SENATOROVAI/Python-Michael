n = int(input())
mas = [[0] * n for i in range(n)]
i = 1
x = 0
y = -1
d_row = 0  # -1 0 1 - ход по рядам
d_colum = 1  # -1 0 1 - ход по колонкам
while i <= n**2:
    # print(i)
    # i += 1
    if 0 <= x + d_row < n and 0 <= y + d_colum < n and mas[x + d_row][y + d_colum] == 0:
        x += d_row
        y += d_colum
        mas[x][y] = i
        i += 1
    else:
        if d_colum == 1:
            d_colum = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_colum = -1
        elif d_colum == -1:
            d_colum = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_colum = 1
for row in mas:
    for elem in row:
        print(elem, end=" ")
    print()
