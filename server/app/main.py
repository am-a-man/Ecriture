import os

scripts = os.listdir("/app/calls")


def colored(text, r=255, g=0, b=0):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


for i in scripts:
    status = os.system(f"python app/calls/{i}")
    if status is not 0:
        print(colored(f"1. check: {i}, it's returning errors, also add error handling"))
    else:
        print(colored(f"1. check: {i} succeded, however check if it's returning the desired data", 0,255,0))
    