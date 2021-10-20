import time, os, sys

#print slow from sabastion on stackoverflow, good lad
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
   
#clears screen after given time
def clearScreen(sleepTime):
  time.sleep(sleepTime)
  os.system("cls")

def invalidInput(text):
    #empty string prints the default text
    if text == "":
        print("\ninvalid input, exeting program")
    else:
        print(text)
    time.sleep(0.2)
    exit()

def listPrint(List):
  roomCount = len(List)
  for i in range(roomCount):
    time.sleep(0.12)
    print(List[i])