#ROCK-PAPER-SCISSORS

def game() :
    List1 = ["ROCK","PAPER","SCISSORS"]
    number = random.randint(0,2)
    return List1[number]

#Main Program

import random
import time
from tabulate import tabulate
print("ROCK-PAPER-SCISSORS")
print("Loading...Pls wait")
for i in range(7):
    print(".",end = "" )
    time.sleep(2)
print()
print("Now shall we start ? (Yes/No) : ")
inp = input().upper()
time.sleep(2)
if inp == "YES" :
    print("Good")
    name = input("Enter your name : ")
    time.sleep(2)
    print("Alright.First you go!!")
    n = random.randint(6,10)
    u = 0
    p = 0
    for i in range(n):
        inp1 = input(">").upper()
        if inp1 not in ["ROCK","PAPER","SCISSORS"] :
            print("Please enter a valid element...")
            continue
        inp2 = game()
        time.sleep(2)
        print(">>"+inp2)
        time.sleep(2)
        if inp1 == inp2 :
            print("Same to same")
        elif (inp1 == "ROCK" and inp2 == "SCISSORS") or (inp1 == "SCISSORS" and inp2 == "PAPER") or (inp1 == "PAPER" and inp2 == "ROCK"):
            List2 = ["Cool!!","Great!!","Good!!","Way to go!!"]
            print(List2[random.randint(0,3)])
            u = u+1
        else :
            List3 = ["Ha..Ha..got you..","Try again.."]
            print(List3[random.randint(0,1)])
            p = p+1
        time.sleep(2)
    time.sleep(2)
    print("OK.Shall we know the results?!!")
    for i in range(7) :
        print(".",end = "" )
        time.sleep(2)
    print()
    print()
    table = tabulate([[name,u],["Program",p]],headers = ["Player","Points"],tablefmt = "fancy_grid")
    print(table)
    print()
    time.sleep(2)
    if u>p :
        print("Congradulations!!You win")
    elif u == p :
        print("The match is draw")
    else :
        print("You lose.But don't worry!You can try next time")
    time.sleep(2)
    print("Thanks for playing")
elif inp == "NO" :
    print("OK.See you next time")
else :
    print("Please Re-run the program and enter a valid choice..")
