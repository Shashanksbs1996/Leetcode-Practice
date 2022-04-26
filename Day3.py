print('''Welcome to Tresure Island

 ________                                                                            ______            __                            __ 
|        \                                                                          |      \          |  \                          |  \
 \$$$$$$$$______    ______    ______    _______  __    __   ______    ______         \$$$$$$  _______ | $$  ______   _______    ____| $$
   | $$  /      \  /      \  |      \  /       \|  \  |  \ /      \  /      \         | $$   /       \| $$ |      \ |       \  /      $$
   | $$ |  $$$$$$\|  $$$$$$\  \$$$$$$\|  $$$$$$$| $$  | $$|  $$$$$$\|  $$$$$$\        | $$  |  $$$$$$$| $$  \$$$$$$\| $$$$$$$\|  $$$$$$$
   | $$ | $$   \$$| $$    $$ /      $$ \$$    \ | $$  | $$| $$   \$$| $$    $$        | $$   \$$    \ | $$ /      $$| $$  | $$| $$  | $$
   | $$ | $$      | $$$$$$$$|  $$$$$$$ _\$$$$$$\| $$__/ $$| $$      | $$$$$$$$       _| $$_  _\$$$$$$\| $$|  $$$$$$$| $$  | $$| $$__| $$
   | $$ | $$       \$$     \ \$$    $$|       $$ \$$    $$| $$       \$$     \      |   $$ \|       $$| $$ \$$    $$| $$  | $$ \$$    $$
    \$$  \$$        \$$$$$$$  \$$$$$$$ \$$$$$$$   \$$$$$$  \$$        \$$$$$$$       \$$$$$$ \$$$$$$$  \$$  \$$$$$$$ \$$   \$$  \$$$$$$$
                                                                                                                                        
                                                                                                                                        
''')
print("Your Mission is to Find the Hidden Tresure")
door = input("Enter the direction R for Right L for Left").lower()
if(door == "r"):
    print("Zombies surrounds you from all the direction and eat you up.")
elif(door =="l"):
    print("Welcome to the second level.\n")
    d2=input("Do you want to Swim or wait ").lower()
    if(d2 =="swim"):
        print("A wormhole opens up in the ocean and you are drowned")
    elif (d2=="wait"):
        print("Welcome to the to third Level\n")
        d3=input("Choose the Door you want to enter 1. red 2. Blue 3. yellow")
        if(d3== "1" or d3== "2"):
            print("You are doomed in Hell")
        else:
            print("Congratulation! you won the game")