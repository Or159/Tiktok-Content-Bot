from editor import *

import time

def print_title():
    print(rf" _______ __   __       __     _____          __           __    ___       __ ")
    print(rf"/_  __(_) /__/ /____  / /__  / ___/__  ___  / /____ ___  / /_  / _ )___  / /_")
    print(rf" / / / /  '_/ __/ _ \/  '_/ / /__/ _ \/ _ \/ __/ -_) _ \/ __/ / _  / _ \/ __/")
    print(rf"/_/ /_/_/\_\\__/\___/_/\_\  \___/\___/_//_/\__/\__/_//_/\__/ /____/\___/\__/ ")
    print(rf"                                                                             ")
    print(rf"                                                                             ")

def menu():
    os.system("cls")
    print_title()
    script = input("Enter Your Script > ")
    voice = input("Enter Your Voice > ")

    try:
        os.system("cls")
        create_video(script, voice)
        time.sleep(3)
        #menu()
    except:
        os.system("cls")
        print("There Was An Error.")
        time.sleep(3)
        #menu()

#print(TextClip.list("font"))

menu()