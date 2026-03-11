from itertools import permutations
equation = input("Enter equation (e.g., SEND + MORE = MONEY): ")
equation = equation.replace(" ", "")
left, right = equation.split("=")
words = left.split("+")
words.append(right)
letters = set() 
for word in words:
    for letter in word:
        letters.add(letter)
letters = list(letters)
if len(letters) > 10:
    print("Too many letters (maximum 10 allowed)")
else:
    digits = "0123456789"
    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))
        valid = True
        for word in words:
            if mapping[word[0]] == '0':
                valid = False
                break
        if not valid:
            continue  
        new_equation = equation
        for letter in letters:
            new_equation = new_equation.replace(letter, mapping[letter])       
        left_part, right_part = new_equation.split("=")      
        if eval(left_part) == eval(right_part):
            print("\nSolution Found!")
            print("Mapping:", mapping)
            print("Equation:", new_equation)
            break