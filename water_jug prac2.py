MAX = 1000

# Input
a = int(input("Enter capacity of Jug A: "))
b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

# Stacks
stackA = [0] * MAX
stackB = [0] * MAX

# Visited states (assuming max capacity <= 20 like your C code)
visited = [[0 for _ in range(20)] for _ in range(20)]

top = -1

# Initial state (0,0)
top += 1
stackA[top] = 0
stackB[top] = 0

while top != -1:
    x = stackA[top]
    y = stackB[top]
    top -= 1

    # Invalid state check
    if x < 0 or y < 0 or x > a or y > b:
        continue

    # Already visited
    if visited[x][y] == 1:
        continue

    visited[x][y] = 1
    print("Jug A =", x, ", Jug B =", y)

    # Target check
    if x == target or y == target:
        print("Target achieved!")
        break

    # Fill Jug A
    top += 1
    stackA[top] = a
    stackB[top] = y

    # Fill Jug B
    top += 1
    stackA[top] = x
    stackB[top] = b

    # Empty Jug A
    top += 1
    stackA[top] = 0
    stackB[top] = y

    # Empty Jug B
    top += 1
    stackA[top] = x
    stackB[top] = 0

    # Pour A -> B
    pour = x if x < (b - y) else (b - y)
    top += 1
    stackA[top] = x - pour
    stackB[top] = y + pour

    # Pour B -> A
    pour = y if y < (a - x) else (a - x)
    top += 1
    stackA[top] = x + pour
    stackB[top] = y - pour
