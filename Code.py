# Program-to-Shutdown-PC
3import os module
import os
# print these things
print("1. Shutdown Computer")
print("2. Restart Computer")
print("3. Exit")
#choice
choice = int(input("\nEnter your choice: "))
# if else statement
if(choice>=1 and choice<=2):
    #nested if else
    if choice == 1:
        os.system("shutdown /s /t 1")
    else:
        os.system("shutdown /r /t 1")
else:
    exit()
