#!/usr/bin/env python2.7

from time import *
from random import *
import os

global money
money = 1000
global HP
HP = 50
global namechoice
namechoice = ["Edward", "Claire", "Andrew", "Annie", "Kevin", "Ken", "Mater", "Finn", "Roger", "Tom", "Jerry"]
shuffle(namechoice)
def goon1():
        ans = raw_input("Where to now? ")
        if ans == "n":
                print "You choose to go north."
                enemy()
        elif ans == "e":
                print "You choose to go east."
                enemy()
        elif ans == "w":
                print "You choose to go west."
                enemy()
def setup():
        wepons = []
        global name
        name = raw_input("What is your name? ")
        if name == "":
                print "Didn't catch that."
                re()
        else:
                name = name
        print "Type \"y\" for YES and \"n\" for NO"
        ans = raw_input("Would you like to get your wepons and armour? ")
        if ans == "y":
                wepons.append("Sword ")
                wepons.append("Shield ")
                wepons.append("Chestplate ")
                wepons.append("Helmet")
                print "You have "+str(wepons)+" with you"
        else:
                print "You go out empty"
                print "You may want to stop at the village as you go out."
        print "As you walk out, your dad, king, gives you $1000"
        print "You have "+str(HP)+" of HP(Health Points)."
        print "You have $"+str(money)+" with you."
def re():
        setup()
def enemy():
        print "Suddenly, you see an orge coming towards you."
        print "ROARRR"
        print "I SMELL YOU, BOY!"
        OHP = randint(5, 20)
        damage = randint(5, 10)
        print "He swings his club at you."
        print "That causes "+str(damage)+" hearts of damage to you"
        HP-damage
        print "You have "+str(HP)+" HP left."
def buy():
        print "["+str(namechoice[0])+": ] We have Health drinks, Arrows, Bows, Swords, Meat and a Helmet"
        buy = raw_input("What do you want?  ")
        if buy == "Health drinks":
                print "["+str(namechoice[0])+": ] You used $50 on it"
                money-50
                print "you have $"+str(money)+" left"
                print "Thanks!"
                goon1()
        elif buy == "Arrows":
                print "["+str(namechoice[0])+": ] You used $35 on it"
                money-35
                print "you have $"+str(money)+" left"
                print "Thanks!"
                goon1()
        elif buy == "Bows":
                print "["+str(namechoice[0])+": ] You used $10 on it"
                money-10
                print "you have $"+str(money)+" left"
                print "Thanks!"
                goon1()
        elif buy == "Swords":
                print "["+str(namechoice[0])+": ] You used $100 on it"
                money-100
                print "you have $"+str(money)+" left"
                print "Thanks!"
                goon1()
        elif buy == "Meat":
                print "["+str(namechoice[0])+": ] You used $5 on it"
                money-5
                print "you have $"+str(money)+" left"
                print "Thanks!"
                goon1()
        elif buy == "Helmets":
                print "["+str(namechoice[0])+": ] You used $250 on it"
                money-250
                print "you have $"+str(money)+" left"
                print "Thanks!"
                goon1()
        else:
                print "Unkown option"
                rbuy()
def rbuy():
        buy()
def meet():
        print "Enter y to chat or n to leave."
        print "["+str(namechoice[0])+": ] Hi, hero, would you like to talk?"
        if raw_input() == "y":
                print "["+str(namechoice[0])+": ] What is your name?"
                print "["+str(namechoice[0])+": ] Oh, your name is "+str(name)
                print "["+str(namechoice[0])+": ] Would you like to buy something?"
                if raw_input() == "y":
                        buy()
                else:
                        print "["+str(namechoice[0])+": ] Bye!"
                        goon1()
        else:
                print "["+str(namechoice[0])+": ] Bye!"
                goon1()

def clear_screen():
        os.system("clear")
def title():
        print "   _      ______ _____ ______ _   _ _____     ____  ______   _    _ ______ _____   ____  ______  _____ "
        print "  | |    |  ____/ ____|  ____| \ | |  __ \   / __ \|  ____| | |  | |  ____|  __ \ / __ \|  ____|/ ____|"
        print "  | |    | |__ | |  __| |__  |  \| | |  | | | |  | | |__    | |__| | |__  | |__) | |  | | |__  | (___  "
        print "  | |    |  __|| | |_ |  __| | . ` | |  | | | |  | |  __|   |  __  |  __| |  _  /| |  | |  __|  \___ \ "
        print "  | |____| |___| |__| | |____| |\  | |__| | | |__| | |      | |  | | |____| | \ \| |__| | |____ ____) |"
        print "  |______|______\_____|______|_| \_|_____/   \____/|_|      |_|  |_|______|_|  \_\\\____/|______|______/ "
        sleep(1)
        setup()
def run():
        print "You walk out of your castle looking for something to fight..."
        print "Press n to go north"
        print "Press s to go south"
        print "Press e to go east"
        print "Press w to go west"
        print "As you walk out, you enter a village and meet a villager."
        meet()
def main():
        clear_screen()
        title()
        run()
main()
