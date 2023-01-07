# //Modules

import os
import pickle
import time
import winsound
from pygame import mixer
from sys import platform
from colorama import init, Fore

# //Config


mixer.pre_init(44100, 16, 2, 4096)
mixer.init()
init(autoreset=True)
lvl = 0
red = Fore.RED
red2 = Fore.LIGHTRED_EX
grn = Fore.GREEN
cyan = Fore.CYAN
white = Fore.WHITE
ylw = Fore.YELLOW
blu = Fore.CYAN
dev = "ScribblesINK"
gname = "The Lost Island"
ver = "0.1.3"
info = cyan + "INFO: "
end_count = "7"
player = "Marcus"
endmes = f"End of {gname} beta :("
unfound_file = None
ae=[
    "Trapped Forever",
    "Lore", 
    "3rd Ending", 
    "Missing the point", 
    "Hospital - Good Ending?",
    "Hospital - Bad Ending",
    "7th Ending",
    "It was her"]

os.system(f"title {gname} - {dev}")

# //Error Messages

er_ii = red + "Invalid Input"
er_m = red + "This file is not meant to be imported"
not_find = ylw + "You don't find anything"
er_in = red+"Invalid Name"
er_fnf = red+"Error while loading files"

# //Main Check

if __name__ == "__main__":
    pass
else:
    print(er_m)
    while True:
        pass

# //Functions

def cs():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def save():
    pickle.dump(lvl, open("DATA/save/save.dat", "wb"))
    pickle.dump(bag, open("DATA/save/bag.dat", "wb"))
    pickle.dump(endings, open("DATA/save/end.dat", "wb"))

def erasedata():
    if os.path.exists("DATA/save/save.dat"):
        os.remove("DATA/save/save.dat")
    else:pass
    if os.path.exists("DATA/save/bag.dat"):
        os.remove("DATA/save/bag.dat")
    else:pass
    if os.path.exists("DATA/save/end.dat"):
        endings = []
        pickle.dump(endings, open("DATA/save/end.dat", "wb"))
    else:pass

def onhold():
    print("\n")
    input("Press enter to continue...")
    cs()

def take(obj):
    if obj in bag:
        pass
    else:
        ask = input(f"Take {obj}? ")
        ask.lower()
        if ask == "y":
            bag.append(obj)
        elif ask == "n":
            pass
        else:
            print(er_ii)

def inbag():
    print(f"{player}'s bag: {bag}")

# //Functions

# Quick check

if os.path.exists("DATA/save/end.dat") and os.path.exists("DATA/save/snd/scream1.wav"):
    endings = pickle.load(open("DATA/save/end.dat", "rb"))
else:
    print(er_fnf)
    print(red+"Check if 'DATA/end.dat'")

# /Quick check


# Main Menu
cs()
print(red+"""
   ____        _ __   __   __        _____  ____ __
  / __/_______(_) /  / /  / /__ ___ /  _/ |/ / //_/
 _\ \/ __/ __/ / _ \/ _ \/ / -_|_-<_/ //    / ,<   
/___/\__/_/ /_/_.__/_.__/_/\__/___/___/_/|_/_/|_|  
                        Games
""")
time.sleep(1)
cs()
allow = False
while allow !=True:
    print(f"""
████████╗██╗░░██╗███████╗  ██╗░░░░░░█████╗░░██████╗████████╗  ██╗░██████╗██╗░░░░░░█████╗░███╗░░██╗██████╗░
╚══██╔══╝██║░░██║██╔════╝  ██║░░░░░██╔══██╗██╔════╝╚══██╔══╝  ██║██╔════╝██║░░░░░██╔══██╗████╗░██║██╔══██╗
░░░██║░░░███████║█████╗░░  ██║░░░░░██║░░██║╚█████╗░░░░██║░░░  ██║╚█████╗░██║░░░░░███████║██╔██╗██║██║░░██║
░░░██║░░░██╔══██║██╔══╝░░  ██║░░░░░██║░░██║░╚═══██╗░░░██║░░░  ██║░╚═══██╗██║░░░░░██╔══██║██║╚████║██║░░██║
░░░██║░░░██║░░██║███████╗  ███████╗╚█████╔╝██████╔╝░░░██║░░░  ██║██████╔╝███████╗██║░░██║██║░╚███║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝░╚════╝░╚═════╝░░░░╚═╝░░░  ╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░
{ver}
""")

    if os.path.exists("please.txt"):
        print("\n\n1. N̷̨̨̢̨̢̡͖͕̘̜͕̤͇̤͕̲̹̻̻̙͚̞̣̰̙̪̠̗͔̼̖̭̮̘̺̮̍̎̉̎̾̏́̉̿̃͛̏͒̂͗̀̕̚͝ȩ̴̧̡̧̗̟̘̳͙͓͈̟͉̠̮͖͉̙̩̟̭͚̜͖̺̭̮̠̟̞͓͇͔͍͍͈̖͈̩̜̺͇̺̜͖̗̈̿͋w̶̡̧̨̨̢̨̢̟͔̟̬͚͇̩̤̭̘̻͕̱̭͎̜͉͍̼͎̹͍͍̞̜̩͙̣̭̗̦̟̙̪̽͊̈̃͋̓͑̈́̊̏̕͘̚͜ Game")


    else:
        print("\n\n1. New Game")
    print("2. Load Game")
    print("3. About")
    print("4. Quit")

    main_menu = input()
    if main_menu == "1":
        cs()
        if os.path.exists("please.txt"):
            if os.path.exists("DATA/save/player.dat"):
                lvl = pickle.load(open("DATA/save/save.dat", "rb"))
                bag = pickle.load(open("DATA/save/bag.dat", "rb"))
                endings = pickle.load(open("DATA/save/end.dat", "rb"))
                readd = open("please.txt")
                check = readd.read()
                if check == "TAKEMETOTHEDOOR":
                    lvl="TAKEMETOTHEDOOR"
                else:
                    print(red+"Err: please.txt")
                    while True: pass
                allow=True
            else: print(red+"Err: please.txt requires DATA/*files")
        else:
            if os.path.exists("DATA/save/save.dat"):
                print(grn + "A save file already exists. Do you want to overwrite it?")
                overwrite = input("[Y/N] ")
                overwrite = overwrite.lower()
                if overwrite == "y":
                    cs()
                    os.remove("DATA/save/save.dat")
                    if os.path.exists("DATA/save/bag.dat"):
                        os.remove("DATA/save/bag.dat")
                    else: pass
                    lvl="prologue"
                    bag=[]
                    allow = True
                elif overwrite == "n":
                    cs()
                else:
                    cs()
                    print(er_ii)
            else:
                lvl="prologue"
                bag = []
                allow = True
        
    elif main_menu == "2":
        cs()
        if os.path.exists("DATA/save/save.dat"):
            lvl = pickle.load(open("DATA/save/save.dat", "rb"))
            bag = pickle.load(open("DATA/save/bag.dat", "rb"))
            endings = pickle.load(open("DATA/save/end.dat", "rb"))
            allow = True
        else:
            print(red + "No save found")
    elif main_menu == "3": # END LIST


        cs()
        print(f"{gname} (v{ver}) by {dev}")
        print()
        print("\nENDINGS:")
        if ae[0] in endings:
            print(f"1. {ae[0]}")
        else: print(f"1. " + red + "locked")
        if ae[1] in endings:
            print(f"2. {ae[1]}")
        else: print(f"2. " + red + "locked")
        if ae[2] in endings:
            print(f"3. {ae[2]}")
        else: print(f"3. " + red + "locked")
        if ae[3] in endings:
            print(f"4. {ae[3]}")
        else: print(f"4. " + red + "locked")
        if ae[4] in endings:
            print(f"5. {ae[4]}")
        else: print(f"5. " + red + "locked")
        if ae[5] in endings:
            print(f"6. {ae[5]}")
        else: print(f"6. " + red + "locked")
        if ae[6] in endings:
            print(f"7.{ae[6]}")
        else: print(f"7. " + red + "locked")
        if ae[7] in endings:
            print(f"Secret Ending: {ae[7]}")
        else: print(f"Secret Ending: " + red + "locked")
        
        erase = input("\nType DEL to erase all data\n")
        erase = erase.lower()
        erase = erase.replace(" ", "")
        if erase == "del":
            erasedata()
            endings = pickle.load(open("DATA/save/end.dat", "rb"))
        else:
            pass
        cs()


    elif main_menu == "4":
        exit()
    else:
        cs()
        print(er_ii)

# Level-0 Script

if lvl == "prologue":
    cs()
    allow = False
    while allow !=True:
        lvl="start"
        save()
        print(f"""

░█▀▀█ █▀▀█ █▀▀█ █── █▀▀█ █▀▀▀ █──█ █▀▀ ▄ 
░█▄▄█ █▄▄▀ █──█ █── █──█ █─▀█ █──█ █▀▀ ─ 
░█─── ▀─▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀▀ ─▀▀▀ ▀▀▀ ▀

You, {player}, were on a cruise with your friends. 
When you were asleep, your cruise's room window had smashed and you woke up to take a closer look. 
At that point the cruise had turned left and you fell out of the window you were inspecting.
You manage to find some cargo crates floating around and you pass out from the coldness of the water.
When you wake up, you are on an island.
""")
        onhold()
        cs()
        allow = True
else:
    pass

# Level-1 Script

if lvl == "start":
    cs()
    print(f"""

░█─░█ █▀▀█ █───█    ▀▀█▀▀ █▀▀█    ░█▀▀█ █── █▀▀█ █──█ ▄ 
░█▀▀█ █──█ █▄█▄█    ─░█── █──█    ░█▄▄█ █── █▄▄█ █▄▄█ ─ 
░█─░█ ▀▀▀▀ ─▀─▀─    ─░█── ▀▀▀▀    ░█─── ▀▀▀ ▀──▀ ▄▄▄█ ▀

- To move around, type the x,y coordinates of where you want to go.
- Your bag will show up at the top of the screen most of the time but if it does not you can type '!bag' to see what's inside it
- if you get this message: Take object? [Y/N]. Enter Y to add to your bag or N to not.
- The game will also automatically save (but doesn't say when).

Good luck :)
""")
    onhold()
    allow = True
    cs()
    allow = False
    
    while allow != True:
        inbag()
        if "Wooden Plank" in bag:
            print("""
- is coastline
= is water
| = hill line
(  ) = cave
anything else are items

MAP:
    ____________________________________
13 |===========================        |   
12 |===-------===========------======  |
11 |-----------------------------------|
10 |       |                           |
9  |       |                           |
8  |       /                           |
7  |      /                            |
6  |============== ====================|
5  |===================================|
4  |   (  )                            |
3  |                                   |
2  |                                   |
1  |___________________________________|
   1    2    3   4   5   6   7   8   9

""")
        else:
            print("""
- is coastline
= is water
| = hill line
(  ) = cave
anything else are items

MAP:
    ____________________________________
13 |===========================        |   
12 |===-------===========------======  |
11 |-----------------------------------|
10 |    ~  |                           |
9  |       |                           |
8  |       /                           |
7  |      /                            |
6  |============== ====================|
5  |===================================|
4  |   (  )                            |
3  |                                   |
2  |                                   |
1  |___________________________________|
   1    2    3   4   5   6   7   8   9

""")
        go = input("x,y = ")
        go = go.lower()
        go = go.replace(" ", "")

        if go == "2,4":
            allow2 = False
            while allow2 !=True:
                cs()
                go2 = input("There is a cave. Go in cave?\n[Y/N]")
                go2.lower()
                if go2 == "y":
                    print("You go in the cave but suddenly fall down below into a hole. You meet some other people who are also trapped in the hole")
                    print("You eventually realize you can't escape and are stuck forever")
                    if "Trapped Forever" in endings:
                        pass
                    else:
                        endings.append("Trapped Forever")
                    save()
                    print(grn + f"\nTrapped Forever\nEnding 1/{end_count}")
                    while True:
                        pass
                if go == "n":
                    allow2 = True
                else:
                    cs()
                    print(er_ii)
        elif go == "2,10":
            print("You spot a Wooden Plank on top of a hill")
            take("Wooden Plank")
            save()
            cs()
        elif go == "4,6":
            cs()
            print("You see a small spot in the river,")
            print("However it is too big for you to jump.")
            if "Wooden Plank" in bag:
                print("You use your wooden plank to make a bridge and cross it")
                bag.remove("Wooden Plank")
                lvl = "islands"
                save()
                onhold()
                allow = True
        else:
            cs()
            print(not_find)
else:
    pass


if lvl == "islands":
    cs()
    allow = False
    while allow !=True:
        print("You find a small raft that you can use. Unfortunately it is too small and too weak to travel far.")
        print("Fortunately, there are 2 islands where you can get resources.")
        go = input("Which island will you go to?\n[1/2]")
        if go == "1":
            # island1
            allow2 = False
            while allow2 !=True:
                print("Once you go to the island your raft breaks. You go further to the island and find the path splitting up")
                go2 = input("Where to go?\n[L/R]")
                go2 = go2.lower()
                if go2 == "l":
                    lvl = "path_l"
                    save()
                    allow = True
                    allow2 = True
                elif go2 == "r":
                    lvl = "path_r"
                    save()
                    allow = True
                    allow2 = True
                elif go2 == "!bag":
                    inbag()
                    onhold()
                else:
                    cs()
                    er_ii
        elif go == "2":
            lvl = "prison"
            save()
            allow = True
        elif go == "!bag":
            cs()
            inbag()
        else:
            cs()
            print(er_ii)
else:
    pass

if lvl == "path_r":
    basement_door = "locked"
    cs()
    print("Once you head in deep enough into the path, you find a village")
    print("However, there aren't any people in it")
    print("You decide to explore the abandoned village")
    onhold()

    allow = False
    while allow !=True:
        inbag()
        print("""
A = House
(  ) = Cave
   _______________________
6 | A                     |
5 |         A             |
4 |     A                 |
3 |                       |
2 |            (  )       |
1 |_______________________|
    1   2   3   4   5   6
""")
        go = input("x,y = ")
        go = go.lower()
        go = go.replace(" ", "")
        if go == "1,6":
            cs()
            print("You enter the house. There is a desk and a door inside in the main room")
            allow2=False
            while allow2 !=True:
                print("1. Open the door")
                print("2. Check the desk")
                print("3. Leave")
                go2 = input(">")
                go2 = go2.lower()
                go2 = go2.replace(" ", "")
                if go2 == "1":
                    cs()
                    print("You try to open the door but realised it's locked.")
                    if "Unknown Key" in bag:
                        bag.remove("Unknown Key")
                        basement_door = "unlocked"
                    else: pass
                    if basement_door == "unlocked":
                        print("You proceed to try your key you found and it worked successfully")
                        print("There are a set of stairs leading down to a basement. You decide to go in")
                        if "lantern" in bag:
                            lvl="basement"
                            save()
                            allow = True
                            allow2 = True
                        else:
                            print("However it is too dark to go in. So you quickly retreat")
                    else: pass
                elif go2 == "2":
                    if "Shard" in bag:
                        cs()
                        print(ylw+"There is nothing else on the desk")
                    else:
                        cs()
                        print("There is a note on the desk. It reads:")
                        print("""
______________________________________
|I don't how it got here.            |
|                                    |
|One day I was farming crops and it  |
|came to my house demanding for      |
|shelter. I didn't know what to do.  |
|I couldn't just say 'no' because it |
|hurt me. I had to feed it. Not the  |
|crops though. It's not a hermivore. |
|It didn't want to eat anything I    |
|gave it though. It demanded for     |
|something I never thought I would   |
|eat. I had to do it. Now all the    |
|village people are gone. Now I have |
|avenge my people. However i can't.  |
|It's coming for me next.            |
|                                    |
|To however reads this take the shard|
|and kill it. It's the only weakness |
|it has.                             |
|                                    |
|                                    |
|-Johnathon Brown                    |
|____________________________________|
""")
                        take("Shard")
                        save()
                        cs()
                elif go2 == "3":
                    cs()
                    allow2=True
                elif go2 == "!bag":
                    cs()
                    inbag()
                else:
                    cs()
                    print(er_ii)


        elif go == "2,4":
            if "Unknown Key" in bag:
                cs()
                print(ylw + "Checking the house for a second time, you find nothing")
            elif basement_door == "unlocked":
                cs()
                print(ylw + "Checking the house for a second time, you find nothing")
            else:
                cs()
                print("You enter the house and find a key. The key says:\n TAKE the key\n just like ME\nfind it TO THE DOOR \nand "+grn+"please"+grn+"."+white+" the "+grn+"t"+white+"e"+grn+"xt"+white+" once more\n")
                take("Unknown Key")
                save()

                if "Unknown Key" in bag:
                    winsound.Beep(800, 1000)
                    cs()
                else: cs()
        elif go == "3,5":
            if "lantern" in bag:
                cs()
                print(ylw + "Checking the house for a second time, you find nothing")
            else:
                cs()
                print("You enter the house and find the lantern")
                take("lantern")
                cs()
                save()
        elif go == "4,2":
            print("There is a cave. Go in cave?")
            go2 = input("[Y/N]")
            go2 = go2.lower()
            if go2 == "y": lvl="cave_vil"
            elif go2 == "n": cs()
            else: print(er_ii)
        else:
            cs()
            print(not_find)
else: pass
if lvl == "prison":
    cs()
    print(endmes)
    while True: pass


else: pass

if lvl == "basement":
    cs()
    if "Shard" in bag:
        print("You enter the room.")
        time.sleep(3)
        print("Your shard starts glowing then the glow disappers")
        time.sleep(3)
        print("...")
        time.sleep(3)
        print("""
I'm here {player}.
Do you remember me?
I remember you.
I remember what you did.
Why did you do that {player}?
Why did you do all that?
Soon I can meet you.
Maybe you will remember what you did then...
""")
        mixer.music.load("DATA/save/snd/scream1.wav")
        mixer.music.play()
        time.sleep(16)
        cs()
        bag.remove("Shard")
        lvl = "hospital"
        save()
    else:
        print("Just as you head in, you are greated by 10 foot huge blob monster with tentacles coverd in blood.\nYou try to defend yourself however you get eaten by the blob.")
        if "Missing the point" in endings: pass
        else:
            endings.append("Missing the point")
            save()
        print(grn + f"\nMissing the point\nEnding 4/{end_count}")
        while True:
            pass
else: pass

if lvl == "path_l":
    print(endmes)
    while True:pass
else: pass

if lvl == "hospital":
    cs()
    print("You wake up.")
    print(f"You are in a hospital. You get up and look at the clipboard attatched to your bed.\nIt reads:\nname: {player}\nDIAGNOSIS: Coma")
    onhold()
    allow = False
    while allow !=True:
        inbag()
        print("""
} = doors
H = beds
# = chairs
+ = desk
anything else are items
   _____________________________________
9  |#                                  |
8  |#                          ++++++++|
7  |#                                  }
6  |#.                                 }
5  |________                           |
4          |                           |
3          |                           |
2          |  H      H      H      H   |
1          |___________________________|
    1 2 3 4 5 6 7 8 9 10 11 12 13  14 15
""")
        go = input("x,y= ")
        go = go.lower()
        go = go.replace(" ", "")

        if go == "1,6":
            print("Next to the chair you find a key with 'WARD-203' written on it")
            take("WARD-203 Key")
            save()
            cs()
        elif go == "1,9":
            cs()
            print("""
__________________________________________________________________
|Dear Josh,                                                       |
|                                                                 |
|My dear friend, I have just been informed you are in hospital    |
|because you have encountered what was hiding in Johnathons house.|
|I did not believe you at first so i went to go check myself.     |
|                                                                 |
|Big mistake.                                                     |
|                                                                 |
|I don't know what he's keeping in there but it's not pretty.     |
|It's some sort of big blob creature with tentacles.              |
|It's eyes are blacker than coal.                                 |
|It's mouth filled with sharp razer teeth ready to bite down.     |
|                                                                 |
|I tried telling the police but it's like talking to a wall.      |
|                                                                 |
|I will find out more and alert you later.                        |
|                                                                 |
|                                                                 |
|                                                                 |
|-Sam Brander                                                     |
|_________________________________________________________________|
""")
            onhold()
            cs()
        elif go == "6,2":
            print("There is a keycard labbled '203-A'")
            take("203-A Keycard")
            save()
            cs()
        elif go == "14,2":
            print("There is a copper wire on the bed")
            take("Copper Wire")
            save()
            cs()
        elif go == "15,6" or go == "15,7":
            cs()
            double_doors = "locked"
            if "WARD-203 Key" in bag:
                double_doors="unlocked"
            else:
                print(red + "The doors are locked")
            
            if double_doors == "unlocked":
                allow2=False
                while allow2!=True:
                    inbag()
                    print("""
    _____
    | | |Stairs  1
 ___  _____________
|        |         |
|        {    2    |
|        |         |
|        |_________|
|        |______
}5       {Ele- 3|
}5       {_vator|
|        |
|        |______________
|        {              |
|        |       4      |
|________|______________|

""")
                    go2=input("> ")
                    if go2=="1":
                        stairway = "locked"
                        if "STAIRWAY Key" in bag:
                            stairway = "unlocked"
                        else:
                            pass
                        if stairway == "unlocked":
                            cs()
                            print("You unlock the stairway with your key")
                            enter = input("Enter stairway? [Y/N] ")
                            enter = enter.lower()
                            enter = enter.replace(" ", "")
                            if enter == "y":
                                print("You enter the stairway and close the door behind you...")
                                time.sleep(3)
                                print("Something is off...")
                                time.sleep(3)
                                print("Despite the sign on the door telling you it was a stairway. There is no stairway.\n You try to open the door but it's locked.\n You survive off eating insects and rats when eventually a rescue team finds you. But something tells you that they weren't here to look for you, but something else...")
                                if "Hospital - Good Ending?" in endings:
                                    pass
                                else:
                                    endings.append("Hospital - Good Ending?")
                                save()
                                print(grn + f"\nHospital - Good Ending?\nEnding 5/{end_count}")
                                while True:
                                    pass
                            elif enter=="n":
                                cs()
                            else:
                                cs()
                                print(er_ii)
                        else:
                            cs()
                            print(red + "The door is locked")
                    elif go2 == "2":
                        room2="locked"
                        if "203-A Keycard" in bag:
                            room2="unlocked"
                        else:
                            pass

                        if room2 == "unlocked":
                            cs()
                            allow3=False
                            while allow3 !=True:
                                inbag()
                                print("""
+ = desk
{ = door
anything else are items
   __________
4  |   +++   |
3  {         |
2  |        '|
1  |_________|
    1 2 3   4
""")
                                go3=input("x,y= ")
                                go3==go3.replace(" ", "")
                                go3=go3.lower()
                                if go3 == "1,3":
                                    cs()
                                    allow3=True
                                elif go3 == "brush":
                                    print("You spot a brush taped to the wall")
                                    take("brush")
                                    save()
                                    cs()
                                elif go3 == "3,4":
                                    cs()
                                    print("""
____________________________________________________________________
|To Dr.Sean,                                                        |
|                                                                   |
|I am writting this to say please give Josh his pain pills at 12:30.|
|I would myself however I am too busy BRUSHing my beautiful pink    |
|moustache and need to go record another fnaf episode.              |
|                                                                   |
|                                                                   |
|Yours truly,                                                       |
|                                                                   |
|Markimoo                                                           |
|___________________________________________________________________|

""")
                                    onhold()
                                elif go3 == "4,2":
                                    print("You see a keypad with up and down arrows on it.")
                                    take("Keypad")
                                    save()
                                    cs()
                                else:
                                    cs()
                                    print(not_find)
                    elif go2 == "3":
                        cs()
                        elevator=0
                        print(ylw+"You go inside the elevator but there is a hole where the keypad should be")
                        if "Keypad" in bag:
                            if "Copper Wire" in bag:
                                elevator=1
                            else:
                                print(ylw+"You insert the keypad into the missing slot however there is a wire ripped clean off so you cannot insert it fully")
                        else:
                            pass

                        if elevator==1:
                            cs()
                            print("You enter the elevator and push the button to go down")
                            time.sleep(4)
                            print("it starts going down")
                            time.sleep(6)
                            print("The elevator seperates from the rusted hooks and you fall to your death")
                            if "Hospital - Bad Ending" in endings:
                                pass
                            else:
                                endings.append("Hospital - Bad Ending")
                            save()
                            print(grn + f"\nHospital - Bad Ending\nEnding 6/{end_count}")
                            while True:
                                pass
                    elif go2 == "4":
                        cs()
                        allow3=False
                        while allow3!=True:
                            inbag()
                            if "STAIRWAY Key" in bag:
                                print("""
_______________________________________
|                                     |
|                                     |
|2                                    |
|                                     |
|                                     |
|                                     |
|                                     |
|_____________________________________|
""")
                            else:
                                print("""
_______________________________________
|                       .             |
|                       1             |
|2                                    |
|                                     |
|                                     |
|                                     |
|                                     |
|_____________________________________|
""")
                            go3=input("> ")
                            go3 = go3.replace(" ", "")
                            if go3=="1":
                                if "STAIRWAY Key" in bag:
                                    cs()
                                else:
                                    print(blu + "Hold it.")
                                    time.sleep(2)
                                    if "brush" in bag:
                                        print(blu+"a brush indeed? You are worthy")
                                        take("STAIRWAY Key")
                                        save()
                                        cs()
                                    else:
                                        print(blu+"You are not worthy. Come back later")
                                        onhold()
                                        allow3=True
                            elif go3=="2":
                                cs()
                                allow3=True
                            else:
                                cs()
                                print(er_ii)
                    elif go2 == "5":
                        cs()
                        allow2=True
        else:
            cs()
            print(not_find)

else: pass

# Unrecognized save
print(ylw + f"If your seeing this then your save is probably corrupted. Please start a new game\nDATA:\nsave={lvl}\nendings={endings}\nbag={bag}")
while True:
    pass
