n = int(input("Enter odd size of magic square matrix: "))
a = []
for i in range(n):          
    row = []
    for j in range(n):     
        row.append(0)
    a.append(row)
i = 0
j = n//2
num = 1
for k in range(n*n):
    a[i][j] = num
    num =num + 1
    r = i - 1
    c = j + 1
    if r < 0:
        r = n - 1
    if c == n:
        c = 0
    if a[r][c] != 0:
        i = i + 1
    else:
        i = r
        j = c
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
