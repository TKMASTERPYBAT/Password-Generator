import random
from colorama import Fore, init

init(autoreset=True)

def passwords_gen(length=12):
    characters = "1234567890abcdefghijklmnopqrstuvwxyz=-+_:;@'~#?/>.<,"
    while True:  
        yield ''.join(random.choices(characters, k=length))

if __name__ == "__main__":
    gen = passwords_gen(length=50)  
    print(Fore.GREEN + "Generating random passwords...")

    with open("SavedPass.txt", 'a') as logkey:
        for _ in range(10): 
            password = next(gen)
            print(Fore.CYAN + password)  
            logkey.write(password + '\n')  
    print(Fore.YELLOW + "\nPasswords Saved To 'SavedPass.txt'")
    
    input(Fore.RED + "Press [ENTER] Key To Continue...")
