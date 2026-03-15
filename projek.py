import random

print("="*18)
print("Where's the Mole?")
print("="*18)

place = "|_|"
mole = [place]*5
mole_space = " ".join(mole)
number_random = random.randint(1,5)

name_user = input("Input Your Name: ")

print(f'''
Welcome {name_user}......
Look for the Mole in the cave below!

{mole_space}
''')

select_user = int(input("Search for Mole in cave number [1/2/3/4/5]: "))
confirm_user = input(f"Are you sure choosing cave {select_user}? [y/n]: ")

if confirm_user.lower() == "n": # Pakai .lower() supaya tetap jalan kalau user ketik 'N' besar
    print(f"{name_user} exited the game!")
    exit()
else:
    if number_random == select_user:
        print(f"\nWIN!!! The Mole was indeed in cave {number_random}!")
        print("Congratulations! You found the Mole!")
    else:
        print(f"\nYou Failed!!! The Mole was actually in cave {number_random}.")