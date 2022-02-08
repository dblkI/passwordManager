#dblkl_
### Password Manager
import random

def passwordGenerator():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = MAYUS + MINUS + NUMS

    password = ['y','o','u','r','o','w','n','c','o','m','m','a','n','d','_']

    for i in range(4):
        random_chars = random.choice(CHARS)
        password.append(random_chars)
        
    password = "".join(password)

    return password
        

def run():
    password = passwordGenerator()
    print('Your new Password is: ' + password)


if __name__ == '__main__': 
    run()