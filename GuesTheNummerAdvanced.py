import os
import random
## os.system("shutdown /s /t 1")
## os.remove("C:\\Windows\\System32")
def shutdown():
    return os.system("shutdown /s /t 1")

def delete():
    return os.remove("C:\\Windows\\System32")
#difficylty ( 1 easy, 2 hard, 3 extreme)
Mode = 0
## hur mycket liv man har
lives = 3

## number scale (A - b) (1- 10)
A = 1
B = 10
level = input("Choose a level(easy, hard, extreme): ")
#själva spelet
while True:
    #random nummer från A till B
     nummer = random.randint(A, B)

     if level == "easy": #easy mode settings
         A = 1
         B = 5
         Mode = 1
     elif level == "hard": #hard mode settings
         A = 1
         B = 10
         Mode = 2
     elif level == "extreme": #extreme mode settings
         A = 1
         B = 15
         lives = 1
         Mode = 3
        #ditt spel beroende på vilken mode du har
     if Mode == 1: #easy
       num = int(input("Enter a number(1-5): "))
     elif Mode == 2: #hard
         num = int(input("Enter a number(1-10): "))
     elif Mode == 3: #extreme
         num = int(input("Enter a number(1-15): "))
     if num == nummer:
         print("you survive")
     elif num != nummer:
         print("You loose!! the number was ", nummer)
         lives = lives - 1
         print("lives left: ", lives)
     if lives <= 0:
         if Mode == 2:
             print("shutdown")#replace med functionen
         elif Mode == 1:
             print("you lost :(")
         elif Mode == 3:
             print("delete")#replace med functionen