import os, sys, datetime, time
from termcolor import colored

HOURS_IN_SECONDS = 60**3
ONE_DAY_IN_SECONDS = 24*HOURS_IN_SECONDS

#Customize the program to your wish by tweking these 3 const variables
#Config Variables>
DEBUG = True
INTERVALS_BETWEEN_RUNTIME_SECONDS = (12*HOURS_IN_SECONDS)
ALLOWED_TIME = datetime.timedelta(
    days=15,
    hours=0,
    minutes=0,
    seconds=0
)

def OperationFailed(text:str):
    if DEBUG: print(colored("* [FAILED] ", 'red'), text)

def OperationSucceeded(text:str):
    if DEBUG: print(colored("* [Succeeded] ", 'green'), text)

def OperationFinished(text:str):
    if DEBUG: print(colored("* [Finished] ", 'blue'), text)


def checkLastaccessTime(pathToFile:str):
    last_access_time = os.path.getatime(pathToFile)
    if last_access_time != None:
        OperationSucceeded(checkLastaccessTime)
        return datetime.datetime.fromtimestamp(last_access_time)
    else:
        OperationFailed(checkLastaccessTime)
        return None

def DeleteFile(file):
    if os.path.exists(file):
        try:
            os.remove(file)
            OperationSucceeded(f"{DeleteFile} [FILE]:{file}")
        except Exception:
            OperationFailed(f"{DeleteFile} [FILE]:{file}")
    else:
        OperationFailed(f"{DeleteFile} [FILE NOT FOUND]:{file}")


def CheckDir(dirToSort:str="") -> bool:

    listOfFiles = os.listdir(dirToSort)

    for file in listOfFiles:
        pathToFile = f"{dirToSort}/{file}"
        time_accesss = (checkLastaccessTime(pathToFile))
        current_time = (datetime.datetime.today())
        
        # print(f"{file} was last access {time_accesss}")
        # print(f"Amount of time since the file was oppend: {current_time - time_accesss}")
        # print(f"current date and time: {current_time}")
        
        if ((current_time - time_accesss) > ALLOWED_TIME):
            DeleteFile(pathToFile)
        print("")

    return True #os.listdir(dirToSort)

def main() -> None:
    while True:
        print(f"Preforming check every {INTERVALS_BETWEEN_RUNTIME_SECONDS}s")
        program_starting_time = datetime.datetime.today()
        print(f"Cleaing directory current time[{program_starting_time}]: ")
        
        CheckDir(sys.argv[1])
        
        program_ending_time = datetime.datetime.today()
        OperationFinished(f"Program finished in {program_ending_time - program_starting_time}")
        time.sleep(INTERVALS_BETWEEN_RUNTIME_SECONDS)

if __name__ == "__main__":
    main()
    # print(os.scandir(sys.argv[1])[0])
