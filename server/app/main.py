import os
import sys
path = sys.path
path.append("/app/")
from common.common import colored
from multiprocessing import Lock, Process
scripts = os.listdir("/app/calls")







def createRunPy():
    with open("test.py", "w", encoding="utf-8") as runPy:
        runPy.write('''
from multiprocessing import Lock
from multiprocessing.context import Process

import os

from multiprocessing import Lock, Process, Pool
processLock = Lock()
import sys
path = sys.path
path.append("/app/calls/")
path.append("/app/common/")
''')
        scriptList = os.listdir("/app/calls")
        for i in scriptList:
            if i != "__pycache__":
                with open("./app/calls/"+i, 'r',encoding = 'utf-8') as scripts:
                    runPy.write(f"def scrapeBot_{i.split('.')[0]}(processLock):\n")
                    for j in scripts.readlines():
                        runPy.write("   "+j+"\n")
                    scripts.close()
        
        runPy.write('''

  

def main():
    
    scriptList = os.listdir("./app/calls")
    
    processes = []

    for i in scriptList:
        if i != "__pycache__":
            processes.append(Process(target = eval("scrapeBot_"+i.split('.')[0]), args={processLock} ))

    # with Pool(len(scriptList), initializer=init, initargs=(Lock(),)) as p:
    #     p.map(startProcess, scriptList)
    #     p.close()
    #     p.join()

    for i in processes:
        i.start()

    for i in processes:
        i.join()
        

if __name__ == "__main__" :

    main()
    exit(0)

        ''')


        runPy.close()
        



def printTest():
    with open("test.py","r",encoding="utf-8") as runPy:
        j = 1
        for i in runPy.readlines():

            print(str(j)+" "+i)
            j+=1


if __name__ == "__main__" :

    createRunPy()
    os.system("python3 test.py")
    os.remove("test.py")
    # printTest()
    exit(0)

