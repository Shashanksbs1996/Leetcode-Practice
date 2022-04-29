import random
win = ('''                                                        88              
                                                          ""              
                                                                          
8b       d8  ,adPPYba,  88       88    8b      db      d8 88 8b,dPPYba,   
`8b     d8' a8"     "8a 88       88    `8b    d88b    d8' 88 88P'   `"8a  
 `8b   d8'  8b       d8 88       88     `8b  d8'`8b  d8'  88 88       88  
  `8b,d8'   "8a,   ,a8" "8a,   ,a88      `8bd8'  `8bd8'   88 88       88  
    Y88'     `"YbbdP"'   `"YbbdP'Y8        YP      YP     88 88       88  
    d8'                                                                   
   d8'                                                                    ''')


lose =('''
               _..._
             ,'     `.
           ,'         `.
         ,'    _   ,-.  `.
         |    (_)  `-'   |
         |        >      |
         |     ,----.    |
         |    /,-""-.\   |
         `.  |/      "  ,'
           `.         ,'
             `._____,'  ''')



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




userc =int(input("What do you choose? Type 0 for Rock,1 for paper or 2 for scissors\n"))
if userc == 0:
  print(f"You Choose {rock}Rock")
elif userc == 1:
  print(f"You Choose {paper}Paper")
elif userc == 2:
  print(f"You Chooose {scissors}Scissor")
else:
  print("Please Choose correctly")
  

comp=random.randint(0,2)

if comp == 0:
  print(f"Computer Choose {rock} Rock")
elif comp == 1:
  print(f"Computer Choose {paper}Paper")
elif comp == 2:
  print(f"Computer Chooose {scissors}Scissor")

if userc ==0:
  if comp == 2:
    print(f"{win}")
  elif comp==1:
    print(f"{lose}")
  elif comp == 0:
    print ("Match Draw!")

elif userc ==1:
  if comp == 0:
    print(f"{win}")
  elif comp==2:
    print(f"{lose}")
  elif comp == 1:
    print ("Match Draw!")

elif userc ==2:
  if comp == 1:
    print(f"{win}")
  elif comp==0:
    print(f"{lose}")
  elif comp == 2:
    print ("Match Draw!")
