import os

scripts = os.listdir("/app/calls")


def colored(text, r=255, g=0, b=0):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def write(base, target):
    with open(target, 'w', encoding="utf-8") as targetFile:
        targetFile.write('''
import sys
import os
sys.stdout = open(os.devnull, "w")        
''')
        with open(base , 'r', encoding="utf-8") as baseFile:
            for i in baseFile:
                targetFile.write(i)
            baseFile.close()
        targetFile.close()


k = 1
for i in scripts:
    write(f"app/calls/{i}", "run.py")
    print(colored(f"[{k}/{len(scripts)}]: starting {i}", 0, 255 , 0),flush=True)
    status = os.system("python3 run.py")
    if status != 0:
        print(colored(f"[{k}/{len(scripts)}] check: {i}, it's returning errors, also add error handling"))
    else:
        print(colored(f"[{k}/{len(scripts)}] check: {i} succeded, however check if it's returning the desired data", 0,255,0))
    os.remove("run.py")
    k+=1


