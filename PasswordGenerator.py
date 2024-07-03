import random 
letters=["A", "B", "C", "D", "E", "F", "G", "H","I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U","V", "W", "X","Y", "Z","a", "b", "c", "d", "e", "f",
        "g", "h", "i", "j", "k", "l","m","n", "o", "p", "q", "r", "s", "t", "u","v","w","x","y","z"]
numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
print("*****************************************************************************")
print("This is a Password Generator!")
numberofletters=int(input("How many letters would you like in your password?\n")) 
numberofsymbols=int(input(f"How many symbols would you like in your password?\n"))
numberofdigits=int(input("how many numbers do u want in your password?\n"))

passwordlist=[]

for _ in range(numberofletters):
    passwordlist.append(random.choice(letters))

for _ in range(numberofsymbols):
    passwordlist.append(random.choice(symbols))

for _ in range(numberofdigits):
    passwordlist.append(random.choice(numbers))

random.shuffle(passwordlist)

password = ''.join(passwordlist)
print("Your generated password is", password)