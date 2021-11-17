import time, os, sys
# For relative imports to work in Python 3.6
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# from pathlib import Path
# print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

#When testing new function put it here
def _test():
    pass

if __name__ == '__main__':
    _test()

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

def intConvert(num):
    numConvert = False
    for i in range(10):
        if str(i) in num:
            numConvert = True
    if numConvert == True:
        return int(num)
    else:
        print('Niet een getal.')
        exit()