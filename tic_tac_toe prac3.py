import random
b = [" "]*9
while True:
    print(b[0],"|",b[1],"|",b[2])
    print(b[3],"|",b[4],"|",b[5])
    print(b[6],"|",b[7],"|",b[8])
    print()
    p = int(input("Enter position (1-9): ")) - 1
    if b[p] != " ":
        print("Invalid")
        continue
    b[p] = "X"
    if (b[0]==b[1]==b[2]=="X") or (b[3]==b[4]==b[5]=="X") or \
       (b[6]==b[7]==b[8]=="X") or (b[0]==b[3]==b[6]=="X") or \
       (b[1]==b[4]==b[7]=="X") or (b[2]==b[5]==b[8]=="X") or \
       (b[0]==b[4]==b[8]=="X") or (b[2]==b[4]==b[6]=="X"):
        print("You win")
        break
    if " " not in b:
        print("Draw")
        break
    ai = random.randint(0,8)
    while b[ai] != " ":
        ai = random.randint(0,8)
    b[ai] = "O"
    if (b[0]==b[1]==b[2]=="O") or (b[3]==b[4]==b[5]=="O") or \
       (b[6]==b[7]==b[8]=="O") or (b[0]==b[3]==b[6]=="O") or \
       (b[1]==b[4]==b[7]=="O") or (b[2]==b[5]==b[8]=="O") or \
       (b[0]==b[4]==b[8]=="O") or (b[2]==b[4]==b[6]=="O"):
        print("AI wins")
        break
    if " " not in b:
        print("Draw")
        break
 